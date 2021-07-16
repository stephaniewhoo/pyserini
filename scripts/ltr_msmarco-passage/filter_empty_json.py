import json
from tqdm import tqdm
temp = []
with open('../../collections/msmarco-doc-passage-ltr/ltr-msmarco-doc.json') as f:
    for line in tqdm(f):
        doc = json.loads(line)
        if (doc['contents'] == ''):
            temp.append(doc['id'])
print(temp)
print(len(temp))
