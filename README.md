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

The script loads annotated training data from a JSON file named "training_data.json." The training data should be structured as a list of dictionaries, where each dictionary contains two keys: "text" for the input text and "entities" for the annotated entity spans.
The script then formats the training data to be compatible with spaCy's training format. For each data point, it creates an Example object that includes the text and the associated entity spans.

### test.py

Contains a script to test the model, the script loads the trained NER model. The model should be saved in the "output" directory, as indicated by "output/model-best" in spacy.load().
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
Negative training data is added so that the AI knows what NOT to look for.

## Getting started using PyCharm

### Step 1

In PyCharm, create a new project.

### Step 2

In the top toolbar click VCS > Get from version control > Paste the URL and clone

### Step 3

Click OK on the popup to create a virtual environment. After that please install Spacy

### Done

Now you should be able to run the scripts. Try running the test.py script.
If not, refer to [this](https://www.youtube.com/watch?v=cAnWazo5pFU) video for help.

## VS-code

### Step 1

Clone the project to your local machine.

### Step 2

Open the folder in VS-code, CD to the "ner" directory.
Make sure Python is installed and that the [virtual environment](https://code.visualstudio.com/docs/python/environments) works.

### Done

Now you should be able to run the scripts. Try running the test.py script.

### Dependencies

Git
Spacy

### Executing program

In PyCharm you can simply run the file you want from the toolbar.
So run the test.py script to test the model.

### Limitations

Rarely extracts perfect data. Only trained towards swedsih data.
Trouble extracting data that comes in a unconventional format.

## Version History

### v0.1.0-beta

Initial Release

### v0.2.0-beta

Added more training data. And changed to the official Spacy training method

### v0.3.0-beta

Better at finding emails, people and company names. Added more labels.
