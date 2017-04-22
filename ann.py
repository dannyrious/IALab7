import fileinput
import random

trainSet = []
testSet = []
outputTrain = []
dimensionality = 0
trainSize = 0
testSize = 0


def stringToNumber (itemList):
  dataList = []
  for items in itemList:
    if isinstance(items, list):
      temp  = []
      for x in items:
        x = float(x)
        temp.append(x)
      dataList.append(temp)
    else:
      items = float(items)
      dataList.append(items)
  return dataList

def trainFormat(trainList):
  formated = []
  for items in trainList:
    del(items[-1])
    formated.append(items)
  return formated


def getOutputTrain(trainSet):
  for element in trainSet:
    outputTrain.append(element[len(element)-1])
  return outputTrain

def readInput(trainSet, testSet, dimensionality, trainSize, outputTrain, testSize):
  file = fileinput.input()
  lineInput = 0
  trainCount = 0
  testCount = 0
  verifier = 0
  for line in file:
    if lineInput == 0:
      dimensionality = float(line.strip("\n"))
      verifier = 0
      
    if lineInput ==  1:
      trainSize = float(line.strip("\n"))
      # print("train " + trainSize)
      verifier = 1
      
    if lineInput == 2:
      testSize = float(line.strip("\n"))
      verifier = 2
      
    if lineInput == 3:
      # print(trainCount)
      line = line.strip("\n")
      line = line.split(",")
      temp = [1]
      temp.extend(line)
      trainSet.append(temp)
      trainCount += 1
      if trainCount == trainSize:
        outputTrain = getOutputTrain(trainSet)
        trainSet = trainFormat(trainSet)
        verifier = 3
      
    if lineInput == 4:
      line = line.strip("\n").strip()
      line = line.split(",")
      temp = [1]
      temp.extend(line)
      testSet.append(temp)
      
      
    if lineInput == verifier:
      lineInput += 1
  
  trainSet = stringToNumber(trainSet)
  outputTrain = stringToNumber(outputTrain)
  testSet = stringToNumber(testSet)
  return dimensionality, trainSize, testSize, trainSet, outputTrain, testSet
      
def initWeights(trainSet):
  weights = []
  for items in range(0,len(trainSet[1])):
    weights.append(random.random())
  return weights

def updateWeight(weights, predictions, trainSet, outputTrain):
  error = 0
  for i in range(0,len(predictions)):
    if (outputTrain[i] - predictions[i] != 0):
      error += 1
      for j in range(0,len(trainSet[i])):
        weights[j] = weights[j] + (outputTrain[i] - predictions[i])*trainSet[i][j]
    else:
      error += 0
  return weights, error;

def predict(weights, trainSet):
  out = 0
  predictions = []
  for i in range(0,len(trainSet)):
    out = 0
    for j in range(0, len(trainSet[i])):
      out = out + trainSet[i][j]*weights[j]
    if (out >= 0):
      predictions.append(1)
    else:
      predictions.append(0)
  return predictions




def train(trainSet, outputTrain, weights):
  for i in range(0, 999):
    predictions = predict(weights, trainSet)
    weights, error = updateWeight(weights, predictions, trainSet, outputTrain)
    if error == 0:
      print(i)
      return weights
  return 0


dimensionality, trainSize, testSize, trainSet, outputTrain, testSet = readInput(trainSet, testSet, dimensionality, trainSize, outputTrain, testSize)
weights = initWeights(trainSet)

answer = train(trainSet, outputTrain, weights)
prediction = predict(answer, testSet)
if answer == 0:
  print("no solution found")
else:
  for i in prediction:
    print(prediction[i])
  