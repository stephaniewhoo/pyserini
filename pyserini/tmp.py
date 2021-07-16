from pyserini.index import IndexReader
#index_reader = IndexReader('./indexes/index-msmarco-passage-ltr-20210519-e25e33f')
#print(index_reader.stats())
index_reader2 = IndexReader.from_prebuilt_index('msmarco-passage-ltr')
print(index_reader2.stats())