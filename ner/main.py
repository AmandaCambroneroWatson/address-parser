import json
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin
from spacy.cli.train import train


with open('annotations.json', 'r') as f:
    data = json.load(f)

nlp = spacy.blank("sv")
# nlp = spacy.load("./output/model-best")

entity_name = ["ADDRESS", "EMAIL", "PERSON", "URL", "TEL", "INCORRECT", "COMPANY"]

train_data = data['annotations']
train_data = [tuple(i) for i in train_data]
for i in train_data:
    if not i[1]['entities']:
        i[1]['entities'] = [(0, 0, entity_name)]
    else:
        i[1]['entities'][0] = tuple(i[1]['entities'][0])





db = DocBin()
for text, annot in tqdm(train_data): # data in previous format
    doc = nlp.make_doc(text) # create doc object from text
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    db.add(doc)
db.to_disk("./train.spacy")
