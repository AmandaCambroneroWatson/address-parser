import spacy
import json
import re

# Load the trained models
nlp1 = spacy.load("./output/model-best")  # load the best model

file_path = "../test_text.txt"
output_file_path_json = "output_entities.json"
output_file_path_txt = "output_entities.txt"


with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

text_without_linebreaks = text.replace('\n', ' ')

new_text_file_path = "modified_text.txt"
with open(new_text_file_path, "w", encoding="utf-8") as new_text_file:
    new_text_file.write(text_without_linebreaks)

# Process the text with the models
models = [nlp1]

patterns = [
    # Email pattern
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|net|org|edu|gov|mil|int|eu|aero|coop|museum|arpa|[a-z]{2,})\b',
    # Telephone patterns
    r'([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?\s[0-9]+([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?\s[0-9]+',
    r'[0-9]+([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?\s[0-9]+\s[0-9]+',
    r'(([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?( ([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?)+)',
]

pattern_names = [
    "email_pattern",
    "tel_pattern_1",
    "tel_pattern_2",
    "tel_pattern_3",
]

pattern_data = list(zip(pattern_names, patterns))
unique_entities = set()

for model in models:
    doc = model(text_without_linebreaks)
    for ent in doc.ents:
        key = (ent.label_, ent.text)
        unique_entities.add(key)

entities_list = [{"text": re.sub(r'[\[\]]', '', ent.text.replace(
    '\n', '')), "label": ent.label_} for ent in doc.ents]
parsed_entities = []

for entity in entities_list:
    # Remove trailing whitespaces and replace multiple whitespaces with a single one
    text = re.sub(r'\s+', ' ', entity["text"].rstrip())

    for pattern_names, pattern in pattern_data:
        if entity["label"] == "TEL" and re.search(pattern, text) and len(text) < 20:
            text = re.sub(r'[a-zA-Z]', '', text)
            text = re.sub(r'\.', '', text)
            entity_key = (entity["label"], text, pattern_names)
            if entity_key not in unique_entities:
                parsed_entities.append(
                    {"label": entity["label"], "text": text.rstrip(), "pattern": pattern_names})
                unique_entities.add(entity_key)
                break

        elif entity["label"] == "ADDRESS" and len(text) < 50:
            text = re.sub('Kontakt', '', text)
            text = re.sub('Tel.', '', text)
            text = re.sub('Tel', '', text)
            text = re.sub(':', '', text)
            entity_key = (entity["label"], text, "")
            if entity_key not in unique_entities:
                parsed_entities.append(
                    {"label": entity["label"], "text": text.rstrip(), "pattern": None})
                unique_entities.add(entity_key)
                break

        elif entity["label"] == "EMAIL" and re.search(pattern, text):
            entity_key = (entity["label"], text, pattern_names)
            if entity_key not in unique_entities:
                parsed_entities.append(
                    {"label": entity["label"], "text": text.rstrip(), "pattern": pattern_names})
                unique_entities.add(entity_key)
                break


with open(output_file_path_json, "w", encoding="utf-8") as output_file_json:
    json.dump(parsed_entities, output_file_json, ensure_ascii=False, indent=4)

with open(output_file_path_json, "r", encoding="utf-8") as json_file:
    json_content = json_file.read()

print("Content of JSON file:")
print(json_content)

with open(output_file_path_txt, "w", encoding="utf-8") as output_file_txt:
    for ent in doc.ents:
        output_file_txt.write("{}\n".format(
            re.sub(r'\.', '', re.sub(r'[\[\]]', '', re.sub(r',', ',', ent.text.replace('\n', ''))))))

for ent in doc.ents:
    print(re.sub(r'\.', '', re.sub(r'[\[\]]', '', re.sub(
        r',', ', ', ent.text.replace('\n', '')))), ent.label_, "UNFILTERED")
