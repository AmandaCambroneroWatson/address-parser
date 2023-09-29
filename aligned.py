import spacy

# Load your spaCy model
nlp = spacy.load("ner_model")

# Define your text and entities
text = "JiA Byggtjänst ABLomgatan 4,507 34 Brämhult 0709-82 78 82jimmy@jiabygg.se"
entities = [[17, 43, "ADDRESS"]]

# Convert offsets to BILUO tags to check alignment
doc = nlp.make_doc(text)
tags = spacy.training.offsets_to_biluo_tags(doc, entities)
print(tags)
