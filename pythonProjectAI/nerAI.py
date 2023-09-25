import spacy

nlp = spacy.load("./output/model-best")
doc = nlp("Vi bor på Fredrikas gård 1,414 83 Göteborg det är väldigt fint här faktiskt.")
print(doc.ents)