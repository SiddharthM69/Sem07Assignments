import nltk
import os
from sklearn.feature_extraction.text import TfidfVectorizer

listOfFiles = os.listdir('../EXP2/FilesAfterTokenization')

listOfSentences = []
for fileName in listOfFiles:
    with open('../EXP2/FilesAfterTokenization/' + fileName) as file:
        for el in file.readlines():
            listOfSentences.append(el)

sentences = [el for el in listOfSentences]
for i in range(0, len(listOfSentences)):
    listOfSentences[i] = ['<s>'] + listOfSentences[i].split(' ') + ['</s>']

bigramList = list(nltk.ngrams(listOfSentences, 2))
trigramList=list(nltk.ngrams(listOfSentences, 3))

print('\n Ngrams list is: ')
print(bigramList)
print(trigramList)

tfidf = TfidfVectorizer()
result = tfidf.fit(sentences)

print('\nWord indexes:')
print(tfidf.vocabulary_)

# display tf-idf values
print('\ntf-idf values:')
print(result)
