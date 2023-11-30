import spacy
import json
import re
import html
# Load the trained models
nlp1 = spacy.load("./output/model-best")  # load the best model

def clean_text(input_text):
    # Remove HTML tags and convert HTML entities to their corresponding characters
    cleaned_text = html.unescape(re.sub(r'<.*?>', '', input_text))
    # Remove multiple consecutive whitespaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

# Process the text with the models
models = [nlp1]

file_path = "../test_text.txt"
output_file_path_json = "output_entities.json"
output_file_path_txt = "output_entities.txt"

tel_pattern = r'([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?\s[0-9]+([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?\s[0-9]+'
tel_pattern2 = r'[0-9]+([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?\s[0-9]+\s[0-9]+'
tel_pattern3 = r'(([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?( ([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?)+)'
address_pattern = r'[A-Za-z]+ä([A-Za-z0-9]+( [A-Za-z0-9]+)+), ([A-Za-z0-9]+( [A-Za-z0-9]+)+)'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|net|org|edu|gov|mil|int|eu|aero|coop|museum|arpa|[a-z]{2,})\b'

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Extract unique entities
unique_entities = set()

for model in models:
    doc = model(text)
    for ent in doc.ents:
        unique_entities.add(ent.text)

entities = [{"label": "UNKNOWN", "text": text} for text in unique_entities]

# Filter and Save TEL entities to JSON and text file
parsed_entities = []

for entity in entities:
    text = entity["text"]
    if entity["label"] == "TEL" and re.search(tel_pattern, text):
        parsed_entities.append({"label": "TEL", "text": text})

    elif entity["label"] == "TEL" and re.search(tel_pattern2, text):
        parsed_entities.append({"label": "TEL", "text": text})

    elif entity["label"] == "TEL" and re.search(tel_pattern3, text):
        parsed_entities.append({"label": "TEL", "text": text})

    elif entity["label"] == "TEL" and re.search(tel_pattern3, text):
        parsed_entities.append({"label": "TEL", "text": text})

    elif entity["label"] == "ADDRESS":
        parsed_entities.append({"label": "ADDRESS", "text": text})

    elif entity["label"] == "EMAIL" and re.search(email_pattern, text):
        parsed_entities.append({"label": "EMAIL", "text": text})


# Save TEL entities to JSON
with open(output_file_path_json, "w", encoding="utf-8") as output_file_json:
    json.dump(parsed_entities, output_file_json, ensure_ascii=False, indent=4)

# Save TEL entities to text file
with open(output_file_path_txt, "w", encoding="utf-8") as output_file_txt:
    for tel_entity in parsed_entities:
        output_file_txt.write("{}\n".format(
            tel_entity["text"].replace('\n', ' ')))

# Print TEL entities to console
for tel_entity in parsed_entities:
    print("{} {}".format(tel_entity["label"],
          tel_entity["text"].replace('\n', ' ')))