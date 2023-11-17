import spacy
import json

# Load the trained models
nlp1 = spacy.load("./output/model-best")  # load the best model
nlp2 = spacy.load("sv_core_news_sm")
file_path = "../test_text.txt"
output_file_path_json = "output_entities.json"
output_file_path_txt = "output_entities.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Process the text with the models
models = [nlp1]
unique_entities = set()

for model in models:
    doc = model(text)
    for ent in doc.ents:
        key = (ent.label_, ent.text)
        unique_entities.add(key)

entities = [{"label": label, "text": text} for label, text in unique_entities]

# Save entities to JSON
with open(output_file_path_json, "w", encoding="utf-8") as output_file_json:
    json.dump(entities, output_file_json, ensure_ascii=False, indent=4)

# Save entities to text file
with open(output_file_path_txt, "w", encoding="utf-8") as output_file_txt:
    for ent in entities:
        output_file_txt.write("{}\n".format(ent["text"]))

# Print entities to console
for ent in entities:
    print("{} {}".format(ent["label"], ent["text"].replace('\n', ' ')))