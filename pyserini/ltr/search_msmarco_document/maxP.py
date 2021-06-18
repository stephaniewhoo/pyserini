from tqdm import tqdm
import collections
scores = collections.defaultdict(dict)
with open('../../runs/run.ltr.msmarco-doc-passage-3.10000.trec') as fin:
    for line in tqdm(fin):
        qid, _, pid, rank, score, _ = line.split('\t')
        score = float(score)
        docid = pid.split('#')[0]
        if (scores[qid][docid] == None or score > scores[qid][docid]):
            scores[qid][docid] = score

with open('../../runs/run.ltr.msmarco-doc.tsv') as fout:
    for qid, docid_score in tqdm(scores.items()):
        rank = 1
        docid_score.sort(key=lambda x:x[1], reverse=True)
        for docid, score in docid_score:
            fout.write(f'{qid}\t{docid}\t{rank}')
            rank += 1
