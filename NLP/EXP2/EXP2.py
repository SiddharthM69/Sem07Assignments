import os
import re
import nltk
import contractions
from word2number import w2n
datasetFolderPath = "../dataset"
nltk.download('punkt')
# contains filenames
datasetFolder = os.listdir(datasetFolderPath)
os.mkdir("FilesAfterPreProcess")
os.mkdir("FilesAfterTokenization")
for file in datasetFolder:
    with open(datasetFolderPath + '/' + file, 'r') as datasetFile:
        linesInFile=datasetFile.readlines()
        # lowercase
        for i in range(0, len(linesInFile)):
            linesInFile[i]=linesInFile[i].lower()

        # # remove whitespaces
        for i in range(0,len(linesInFile)):
            linesInFile[i] = " ".join(linesInFile[i].split())

        # # removal of special characters
        for i in range(0, len(linesInFile)):
            linesInFile[i] = re.sub(r"[^a-zA-Z0-9]+", ' ', linesInFile[i]).lower() + "\n"
        with open("FilesAfterPreProcess/"+file, "a") as newFile:
            newFile.writelines([el for el in linesInFile if len(el)>3])

        # tokenization
        tokens=[]
        for i in range(0,len(linesInFile)):
            nltk_tokens = nltk.word_tokenize(linesInFile[i])
            for el in nltk_tokens:
                tokens.append(el+" ")
            tokens.append("\n")
        with open("FilesAfterTokenization/" + file, "a") as newFile:
            newFile.writelines(tokens)





