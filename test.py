import spacy

# Load the trained model
nlp = spacy.load("ner_model")

file_path = "test_text.txt"

output_file_path = "output_entities.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Process the text with the model
doc = nlp(text)

# Create a file to save the output


# Open the output file in write mode
with open(output_file_path, "w", encoding="utf-8") as output_file:
    # Iterate over the entities predicted by the model
    for ent in doc.ents:
        # Write the entity text and label to the output file
        output_file.write(f"{ent.text}\n")
        print(ent.text, ent.label_)

print("Entities saved to:", output_file_path)