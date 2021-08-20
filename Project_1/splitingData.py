from sklearn.model_selection import train_test_split
import random

inputFile = input("Enter the corpus file you want to split: ")
outputTrainFile = input("Enter name of output train file: ")
outputTestFile = input("Enter name of output test file: ")
outputTestLabels = input("Enter name of output test labels file: ")

with open(inputFile, "r") as f:
    data = f.read().splitlines()

    x_train ,x_test = train_test_split(data,test_size=0.2)

#x_train ,x_test = train_test_split(fin,test_size=0.2)
trainLines = x_train
testLines = x_test

train = []
for j in trainLines:
    train.append(j)

testList = []
testLabels = []
for i in testLines:
    
    testLabels.append(i)
    #get the name and category 
    split = i.split()
    name = split[0]
    
    testList.append(name)

trainOutput = open(outputTrainFile, "w")

for i in train:
    trainOutput.write(i)
    trainOutput.write('\n')

trainOutput.close()

testOutput = open(outputTestFile, "w")

for i in testList:
    testOutput.write(i)
    testOutput.write('\n')

testOutput.close()

testLabelsOut = open(outputTestLabels, "w")

for i in testLabels:
    testLabelsOut.write(i)
    testLabelsOut.write('\n')

testLabelsOut.close()