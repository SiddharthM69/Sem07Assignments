import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Specify the file path with cp1252 encoding for input
input_file_path = 'rec.autos.txt'

# Read the text file with cp1252 encoding
with open(input_file_path, 'r', encoding='cp1252') as file:
    blogs = file.read()

    # Initialize stopwords, stemmer, and lemmatizer
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

sentences = nltk.sent_tokenize(blogs)
tokenized_blogs = [nltk.word_tokenize(sentence) for sentence in sentences]

# Perform stopword removal and save to a separate output file
output_stopword_removal_path = 'output_stopword_removal.txt'
cleaned_blogs_stopword_removal = []

for tokens in tokenized_blogs:
    cleaned_tokens = []
    for token in tokens:
        if token.lower() not in stop_words and token.isalpha():
            cleaned_tokens.append(token)
    cleaned_blog = ' '.join(cleaned_tokens)
    cleaned_blogs_stopword_removal.append(cleaned_blog)

with open(output_stopword_removal_path, 'w', encoding='ansi') as output_file:
    for cleaned_blog in cleaned_blogs_stopword_removal:
        output_file.write(cleaned_blog + '\n')

print(f"Cleaned blogs after stopword removal saved to {output_stopword_removal_path}")


# Create output files for lemmatization, stemming, and stopwords removal
output_lemmatization_path = 'output_lemmatization.txt'
output_stemming_path = 'output_stemming.txt'
output_stopwords_removal_path = 'output_stopwords_removal.txt'

# Perform lemmatization and stemming word by word with corresponding lemmas and stems
lemmatized_words = []
stemmed_words = []

# Tokenize paragraphs
paragraphs = sent_tokenize(blogs)

for paragraph in paragraphs:
    # Tokenize words in the paragraph
    words = word_tokenize(paragraph)
    
    lemmatized_tokens = []
    stemmed_tokens = []

    for word in words:
        if word.isalpha():
            # Lemmatize the word with the appropriate POS tag (default is noun)
            lemmatized_word = lemmatizer.lemmatize(word, pos='v')  # 'v' indicates verb
            stemmed_word = stemmer.stem(word)
            lemmatized_tokens.append((word, lemmatized_word))
            stemmed_tokens.append((word, stemmed_word))
    
    lemmatized_words.extend(lemmatized_tokens)
    stemmed_words.extend(stemmed_tokens)

# Save lemmatized words to the output file
with open(output_lemmatization_path, 'w', encoding='cp1252') as lemmatization_output_file:
    for word, lemma in lemmatized_words:
        lemmatization_output_file.write(f"{word} -> {lemma}\n")

print(f"Lemmatized words saved to {output_lemmatization_path}")

# Save stemmed words to the output file
with open(output_stemming_path, 'w', encoding='cp1252') as stemming_output_file:
    for word, stem in stemmed_words:
        stemming_output_file.write(f"{word} -> {stem}\n")

print(f"Stemmed words saved to {output_stemming_path}")
