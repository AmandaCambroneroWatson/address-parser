import spacy
import random
import json
from spacy.training.example import Example

# Load the blank Swedish language model
nlp = spacy.blank("sv")

# Define the entity label for addresses
label = "ADDRESS"

# Add the NER component to the pipeline
nlp.add_pipe("ner", name=label)

# Load and convert the annotated training data
with open("training_data.json", "r", encoding="utf-8") as file:
    training_data = json.load(file)

# Format the training data for spaCy
formatted_data = []
for data in training_data:
    text = data["text"]
    entities = data["entities"]
    entity_dict = {"entities": entities}
    formatted_data.append(Example.from_dict(nlp.make_doc(text), entity_dict))

# Start training the model
nlp.begin_training()

# Set the number of training iterations and batch size
epochs = 40
batch_size = 8

for _ in range(epochs):
    random.shuffle(formatted_data)
    batches = spacy.util.minibatch(formatted_data, size=batch_size)
    losses = {}

    for batch in batches:
        nlp.update(batch, losses=losses)

    print("Loss:", losses)

# Save the trained model
nlp.to_disk("ner_model")