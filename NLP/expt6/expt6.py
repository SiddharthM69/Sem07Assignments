import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Input and output file paths
input_file_path = "rec.autos.txt"  # Replace with the path to your input file
output_file_path = "output_6.txt"  # Replace with the desired output file path

# Initialize the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to map NLTK POS tags to WordNet POS tags
def get_wordnet_pos(tag):
    tag = tag[0].upper()
    tag_dict = {"J": "a", "N": "n", "V": "v", "R": "r"}
    return tag_dict.get(tag, "n")  # Default to noun if not found

# Open the input and output files with ANSI encoding
with open(input_file_path, "r", encoding="cp1252") as input_file, open(output_file_path, "w") as output_file:
    # Process each line in the input file
    for line in input_file:
        line = line.strip()  # Remove leading/trailing whitespace
        if not line:
            continue  # Skip empty lines

        # Tokenize the line into words
        words = word_tokenize(line)

        # Perform part-of-speech tagging
        tagged_words = pos_tag(words)

        # Lemmatize and write the analysis results to the output file
        for word, tag in tagged_words:
            lemma = lemmatizer.lemmatize(word, get_wordnet_pos(tag))
            output_file.write(f"Token: {word}\n")
            output_file.write(f"Lemma: {lemma}\n")
            output_file.write(f"POS Tag: {tag}\n")
            output_file.write("\n")  # Separate tokens with a blank line

print("Morphological analysis complete. Results written to", output_file_path)
