import spacy
nlp = spacy.load("sv_core_news_lg")

with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(spacy.explain("MSR"))

doc = nlp(text)


for entity in doc.ents:
    print(entity.text, entity.label_)
