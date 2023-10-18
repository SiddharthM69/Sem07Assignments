import spacy

# Load the spaCy NER model
nlp = spacy.load('en_core_web_sm')
nlp.max_length = 2665900

# Input and output file paths
input_file_path = 'rec.autos.txt'
output_file_path = 'output_8.txt'

# Open the input file for reading
with open(input_file_path, 'r', encoding='cp1252') as input_file:
    input_text = input_file.read()

# Process the input text with spaCy
doc = nlp(input_text)

# Open the output file for writing
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Iterate through the named entities and write them to the output file
    for ent in doc.ents:
        output_file.write(f"Entity: {ent.text}, Label: {ent.label_}\n")
print("Named entities extracted and saved to output.txt.")