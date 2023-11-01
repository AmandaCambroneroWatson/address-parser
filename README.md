# SkyIntelligence

This repository contains a Python script for training a custom NER model using spaCy. The model is designed to identify addresses in Swedish text.

## Description

### Main.py
The script begins by importing the necessary Python libraries, which include:
spacy: The core library for natural language processing and NER.
random: Used for shuffling data during training.
json: Required for reading training data from a JSON file.
spacy.training.example.Example: Used to format training data for spaCy.

The script loads a blank Swedish language model in spaCy. This blank model serves as the foundation for training the custom NER model.
We can also of course load a trained model and train it. But it's a work in progress to perfect the training.

An entity label for addresses is defined as "ADDRESS." This label will be used to mark and identify addresses in text during training.
The NER (Named Entity Recognition) component is added to the spaCy pipeline, with the entity label set to "ADDRESS." This component will be responsible for identifying addresses in the text.
The script loads annotated training data from a JSON file named "training_data.json." The training data should be structured as a list of dictionaries, where each dictionary contains two keys: "text" for the input text and "entities" for the annotated entity spans.
The script then formats the training data to be compatible with spaCy's training format. For each data point, it creates an Example object that includes the text and the associated entity spans.
The script initiates the training process by calling nlp.begin_training(). It specifies the number of training iterations (epochs) and the batch size.
For each epoch, the script shuffles the training data to ensure a diverse training experience. It then divides the data into batches and updates the NER model with each batch. The training loss is recorded after each batch.
You can customize the script by adjusting the number of training epochs and the batch size to suit your specific dataset and training requirements.

### test.py
Contains a script to test the model, the script loads the trained NER model. The model should be saved in the "ner_model" directory, as indicated by "ner_model" in spacy.load().
Define the file paths for the input text file (file_path) and the output file to store the extracted entities (output_file_path).
The script opens and reads the contents of the input text file specified by file_path and assigns it to the text variable.
The loaded NER model (nlp) is used to process the input text, creating a spaCy Doc object.
The script prepares to create and write the extracted entities to the output file specified by output_file_path. The file will be opened in write mode, overwriting any existing content.
The script iterates over the entities detected in the processed text using the .ents attribute of the doc object. For each entity, it writes the entity's text and label to the output file.
Additionally, the script prints each entity's text and label to the console.

### training_data.json
The json file contains the data used by the model.
```
{
    "text": "Östergatan 3B, 223 56 Lund, Sverige är en vacker gata.",
    "entities": [
      [0, 26, "ADDRESS"]
    ]
  },
```
The address is marked by the enteties. In the example above, the address is the enteties 0-26.
Negative training data is added so that the AI knows what NOT to look for, basically everything that is not an address is negative data.

## Getting Started/Installing
Clone the repo. Using git.
```
git clone https://github.com/AmandaCambroneroWatson/address-parser.git
```
I recommend using PyCharm to run and work on the script.

### Dependencies
Git
Spacy

### Executing program
In PyCharm you can simply run the file you want from the toolbar.
So run the test script to test the AI.

## Version History
 0.1
   Initial Release
