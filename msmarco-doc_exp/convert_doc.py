#!/usr/bin/env python
# Convert MSMARCO passage
import multiprocessing
from joblib import Parallel, delayed
import sys
import json
import argparse
from transformers import AutoTokenizer, AutoModel
import spacy
import re
from convert_common import readStopWords, SpacyTextParser, getRetokenized
from pyserini.analysis import Analyzer, get_lucene_analyzer
import time

sys.path.append('.')

parser = argparse.ArgumentParser(description='Convert MSMARCO-adhoc documents.')
parser.add_argument('--input', metavar='input file', help='input file',
                    type=str, required=True)
parser.add_argument('--output', metavar='output file', help='output file',
                    type=str, required=True)
parser.add_argument('--max_doc_size', metavar='max doc size bytes',
                    help='the threshold for the document size, if a document is larger it is truncated',
                    type=int, default=16536 )
parser.add_argument('--proc_qty', metavar='# of processes', help='# of NLP processes to span',
                    type=int, default=multiprocessing.cpu_count() - 2)

args = parser.parse_args()
print(args)
arg_vars = vars(args)

inpFile = open(args.input)
outFile = open(args.output, 'w')
maxDocSize = args.max_doc_size


def batch_file(iterable, n=10000):
    batch = []
    for line in iterable:
        batch.append(line)
        if len(batch) == n:
            yield batch
            batch = []
    if len(batch)>0:
        yield batch
        batch = []
    return

def batch_process(batch):
    stopWords = readStopWords('stopwords.txt', lowerCase=True)
    nlp = SpacyTextParser('en_core_web_sm', stopWords, keepOnlyAlphaNum=True, lowerCase=True)
    analyzer = Analyzer(get_lucene_analyzer())
    bertTokenizer =AutoTokenizer.from_pretrained("bert-base-uncased")

    def process(line):
        fields = json.loads(line.rstrip())
        pid = fields['id']
        body = fields['contents']

        text, text_unlemm = nlp.procText(body)

        entity = {}
        entity = json.dumps(entity)

        analyzed = analyzer.analyze(body)
        for token in analyzed:
            assert ' ' not in token
        contents = ' '.join(analyzed)

        doc = {"id": pid,
               "text": text,
               "text_unlemm": text_unlemm,
               'contents': contents,
               "raw": body,
               "entity": entity}
        doc["text_bert_tok"] = getRetokenized(bertTokenizer, body.lower())
        return doc
    res = []
    start = time.time()
    for line in batch:
        res.append(process(line))
        if len(res) % 1000 == 0:
            end = time.time()
            print(f'finish {len(res)} using {end-start}')
            start = end
    return res


if __name__ == '__main__':
    proc_qty = args.proc_qty
    print(f'Spanning {proc_qty} processes')
    pool = Parallel(n_jobs=proc_qty, verbose=10)
    ln = 0
    for big_batch in batch_file(inpFile, 20000*proc_qty):
        for batch_json in pool(delayed(batch_process)(batch) for batch in batch_file(big_batch)):
            for docJson in batch_json:
                ln = ln + 1
                if docJson is not None:
                    outFile.write(json.dumps(docJson) + '\n')
                else:
                    print('Ignoring misformatted line %d' % ln)

    print('Processed %d passages' % ln)

    inpFile.close()
    outFile.close()

