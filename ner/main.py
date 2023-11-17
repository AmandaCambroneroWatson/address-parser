import json
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin
from spacy.cli.train import train


with open('annotations.json', 'r') as f:
    data = json.load(f)

nlp = spacy.blank("sv")

train_data = data['annotations']
train_data = [tuple(i) for i in train_data]
for i in train_data:
    i[1]['entities'] = [tuple(entity) for entity in i[1]['entities']]


db = DocBin()
for text, annot in tqdm(train_data):
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annot["entities"]:  # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)

    doc.ents = ents
    db.add(doc)
db.to_disk("./train.spacy")
train("./config.cfg", overrides={"paths.train": "./train.spacy", "paths.dev": "./train.spacy"})
