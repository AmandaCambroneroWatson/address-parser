import spacy
import json
import re
import html

def clean_text(input_text):
    # Remove HTML tags and convert HTML entities to their corresponding characters
    cleaned_text = html.unescape(re.sub(r'<.*?>', '', input_text))
    # Remove multiple consecutive whitespaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

# Load the trained models
nlp1 = spacy.load("./output/model-best")  # load the best model
nlp2 = spacy.load("sv_core_news_sm")

# Process the text with the models
models = [nlp1, nlp2]

file_path = "../test_text.txt"
output_file_path_json = "output_entities.json"
output_file_path_txt = "output_entities.txt"

# Define the address pattern
address_pattern = r'\b\d{1,5}\s[A-Za-z0-9åäöÅÄÖ]+\s(?:\d{1,5}\s)?\d{1,5}(?:\s-\s\d{1,5}\s\d{1,5})?(?:\s[A-Za-z0-9åäöÅÄÖ]+\s?\d{1,5})?\b'

# Define the telephone number pattern
tel_pattern = r'^(?:\+?(?:\d{1,3})?\s?(?:0[1-9]|[1-9]))(?:[\s.-]?\d{2,3}(?:(?:[\s.-]?\d{2,3}){1,2})?|\d{5,15})$'


# Define the email pattern
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

# Validate TEL entities using phonenumbers
validated_entities = []

for entity in entities:
    text = entity["text"]
    if re.search(tel_pattern, text):
        # If the text matches the TEL pattern, consider it as a TEL entity
        validated_entities.append({"label": "TEL", "text": text})
    elif re.search(email_pattern, text):
        validated_entities.append({"label": "EMAIL", "text": text})
    elif re.search(address_pattern, text):
        validated_entities.append({"label": "ADDRESS", "text": text})

# Save entities to JSON
with open(output_file_path_json, "w", encoding="utf-8") as output_file_json:
    json.dump(validated_entities, output_file_json, ensure_ascii=False, indent=4)

# Save entities to text file
with open(output_file_path_txt, "a", encoding="utf-8") as output_file_txt:
    for ent in validated_entities:
        output_file_txt.write("{}\n".format(ent["text"].replace('\n', ' ')))

# Print entities to console
for ent in validated_entities:
    if ent["label"] == "ADDRESS" or ent["label"] == "EMAIL" or ent["label"] == "TEL":
        print("{} {}".format(ent["label"], ent["text"].replace('\n', ' ')))
