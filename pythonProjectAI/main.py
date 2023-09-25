import random
import spacy
from spacy.tokens import Span, DocBin

nlp = spacy.blank("sv")


doc3 = nlp("Vi bor på Storgatan 42, 123 45 Stockholm, det är väldigt fint här faktiskt.")
doc3.ents = [Span(doc3, 3, 8, label="ADDRESS")]
# Create a Doc with entity spans
doc1 = nlp("Skrubb AB är baserade i Fredrikas gård 1, 414 83 Göteborg")
doc1.ents = [Span(doc1, 5, 11, label="ADDRESS")]
# Create another doc without entity spans
doc2 = nlp("Om oss vi är ett företag som gör prylar det är kul att göra prylar men det är ganska dyrt och vi har "
           "mycket personal att betala, men skit i det. Markus Johansson är chef på KodaSkåda AB han är också delägare i 46Elks INC"
           "Vanligtvis så brukar jag fiska med fiskespö 5000. Det låter kanske dumt och ser nog rätt dumt ut att bara skriva massa random ord"
           "För att lära en 'ner' rätt saker så måste man göra såhär. Vet inte om vi kan blanda språk men. Får fråga Jonas Tengborg"
           "eller Emma Tullvall eller kanske Johan Persson")
doc2.ents = []

docs = [doc1, doc2, doc3]  # and so on...

random.shuffle(docs)
train_docs = docs[:len(docs) // 2]
dev_docs = docs[len(docs) // 2:]

# Create and save a collection of training docs
train_docbin = DocBin(docs=train_docs)
train_docbin.to_disk("./train.spacy")
# Create and save a collection of evaluation docs
dev_docbin = DocBin(docs=dev_docs)
dev_docbin.to_disk("./dev.spacy")
