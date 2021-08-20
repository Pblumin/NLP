# Philip Blumin
# NLP Project 1 Spring 2020

import nltk 
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import math

def getUserInput():
    trainFile = input("Enter file containing list of labeled training documents: ")
    testFile = input("Enter file containing list of unlabeled test documents: ")
    outputFile = input("Enter name of output file: ")
    return trainFile, testFile, outputFile

def Count(dict, i):
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

########## TRAINING STAGE ##########
def train(trainFile):
    #open train file
    fTrain = open(trainFile, "r")

    #split the file into lines so I can get the info
    fTrainLines = fTrain.read().splitlines()

    #DICTIONARIES FOR TRAINING
    fileDict = dict() #file dictionary
    wordDict = dict() #word dictionary
    catDict = dict() #category dictionary

    for i in fTrainLines:
        #get the name and category 
        split = i.split()
        name = split[0]
        category = split[1]

        trainCurrent = open(name, "r")
        
        #use word tokenize
        tokenizedTrain = word_tokenize(trainCurrent.read())

        Count(fileDict, category)

        #need to get the total number of files
        fileNum = sum(fileDict.values())

        for word in tokenizedTrain:
            
            Count(catDict, category)
            
            Count(wordDict, (word,category))

        categories = catDict.keys()

    return fileDict, catDict, wordDict, fileNum, categories

########## TEST STAGE ##########
def test(testFile, fileDict, catDict, wordDict, fileNum, categories):
    #open test file
    fTest = open(testFile, "r")
    #split the file into lines so I can get the info
    fTestLines = fTest.read().splitlines()

    preds = []

    for i in fTestLines:
        testCurrent = open(i, "r")
        tokenizedTest = word_tokenize(testCurrent.read())

        testDict = dict() #testdoc
        probSum = dict() #sum[c]

        for j in tokenizedTest:

            Count(testDict, j)

        #READ THROUGH CHAPTER 4
        for c in categories:

            #Ndoc = fileNum
            #Nc = fileDict[c]
            logPrior = math.log(fileDict[c]/fileNum)
            totalLoglikelihood = 0
            #totalVocab = len(testDict) + catDict[c] #vocabulary of D
            #V = testDict.items()
            bottomSum = len(testDict) + catDict[c]
            
            for w,count in testDict.items():
                
                if(w, c) in wordDict:
                    wordCount = wordDict[(w, c)] + 0.1
                else:
                    wordCount = 0.1

                # print('count: ', count)
                # print('\n')
                # print('wordCount: ', wordCount)
                # print('\n')

                loglikelihood = count*math.log(wordCount/bottomSum)
                totalLoglikelihood += loglikelihood

            probSum[c] = logPrior + totalLoglikelihood

        #choose the max
        bestGuess = max(probSum, key = probSum.get)

        #what ever you get from the max make that into string
        predString = i + ' ' + bestGuess + '\n'

        #append each string to the predictions
        preds.append(predString)
    
    return preds

########## OUTPUT STAGE ##########
def output(outputFile, preds):
    #open output file
    fOutput = open(outputFile, "w")

    #write to output file
    #something like fOutput.write()
    for p in preds:
        fOutput.write(p)

    #close output file
    fOutput.close()

########## MAIN STAGE ##########
trainFile, testFile, outputFile = getUserInput()

fileDict, catDict, wordDict, fileNum, categories = train(trainFile)

predictions = test(testFile, fileDict, catDict, wordDict, fileNum, categories)

output(outputFile, predictions)
