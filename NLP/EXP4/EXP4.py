import nltk
from nltk import pos_tag
from nltk import RegexpParser
import os
nltk.download('averaged_perceptron_tagger')

listOfFiles=os.listdir('../EXP2/FilesAfterTokenization')


listOfSentences=[]
for fileName in listOfFiles:
    with open('../EXP2/FilesAfterTokenization/'+fileName) as file:
        for el in file.readlines():
            listOfSentences.append(el)
sentences=[el for el in listOfSentences]
for i in range(0, len(listOfSentences)):
    listOfSentences[i]=listOfSentences[i].split(' ')

posTagged=[]
for el in listOfSentences:
    posTagged.append(pos_tag(el))

patterns= """mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"""
chunker = RegexpParser(patterns)
print("After Regex parsing:",chunker)

output = chunker.parse(posTagged)
print("After Chunking",output)



chunker = RegexpParser("""
                       NP: {<DT>?<JJ>*<NN>}
                       P: {<IN>}               
                       V: {<V.*>}              
                       PP: {<p> <NP>}          
                       VP: {<V> <NP|PP>*}      
                       """)

# Print all parts of speech in above sentence
output = chunker.parse(pos_tag(nltk.word_tokenize(listOfSentences[0])))
print("After Extracting\n", output)