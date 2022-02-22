# -*- coding: utf-8 -*-
"""Task1_2_TrainOnActualTask.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lBiPpJYmRkCZ7kHxSKWdWhKecYaZZjkJ
"""

pip install tensorflow==2.4

import tensorflow as tf
import numpy as np
import torch
import torchvision as tv
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

trainingSet = datasets.MNIST('', train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))
testingSet = datasets.MNIST('', train=False, download=True, transform=transforms.Compose([transforms.ToTensor()]))
train = torch.utils.data.DataLoader(trainingSet, batch_size=50, shuffle=True)
test = torch.utils.data.DataLoader(testingSet, batch_size=50, shuffle=True)

class ShallowTrainNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 34)
        self.fc2 = nn.Linear(34, 10)

    def forward(self, val):
        val = F.relu(self.fc1(val))
        val = self.fc2(val)
        return val


class MiddleTrainNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 28)
        self.fc2 = nn.Linear(28, 64)
        self.fc3 = nn.Linear(64, 42)
        self.fc4 = nn.Linear(42, 10)

    def forward(self, val):
        val = F.relu(self.fc1(val))
        val = F.relu(self.fc2(val))
        val = F.relu(self.fc3(val))
        val = self.fc4(val)
        return val
    

class DeepTrainNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 24)
        self.fc2 = nn.Linear(24, 40)
        self.fc3 = nn.Linear(40, 60)
        self.fc4 = nn.Linear(60, 48)        
        self.fc5 = nn.Linear(48, 30)
        self.fc6 = nn.Linear(30, 10)        
        
    def forward(self, val):
        val = F.relu(self.fc1(val))
        val = F.relu(self.fc2(val))
        val = F.relu(self.fc3(val))
        val = F.relu(self.fc4(val))
        val = F.relu(self.fc5(val))
        val = self.fc6(val)
        return val

shallownn = ShallowTrainNN()
middlenn = MiddleTrainNN()
deepnn = DeepTrainNN()
costFunc = nn.CrossEntropyLoss()
shallowOpt = optim.Adam(shallownn.parameters(), lr=0.001)
middleOpt = optim.Adam(middlenn.parameters(), lr=0.001)
deepOpt = optim.Adam(deepnn.parameters(), lr=0.001)

EPOCHS = 100
counter = 0
counterList = []
shallowCostList = []
shallowTestAccuracyList = []
shallowTrainAccuracyList = []
for index in range(EPOCHS):
    counterList.append(counter)
    counter += 1
    
    for batch in train:
        inputImages, groundTruth = batch
        shallownn.zero_grad()
        output = shallownn(inputImages.view(-1,784))
        cost = costFunc(output, groundTruth)
        cost.backward()
        shallowOpt.step()
    shallowCostList.append(cost.detach().numpy())
    
    
    correct = 0
    total = 0
    with torch.no_grad():
        for batch in train:
            inputImages, groundTruth = batch
            output = shallownn(inputImages.view(-1,784))
            for i, outputTensor in enumerate(output):
                if torch.argmax(outputTensor) == groundTruth[i]:
                    correct += 1
                total += 1
    shallowTrainAccuracyList.append(round(correct/total, 3))

    
    correct = 0
    total = 0
    with torch.no_grad():
        for batch in test:
            inputImages, groundTruth = batch
            output = shallownn(inputImages.view(-1,784))
            for i, outputTensor in enumerate(output):
                if torch.argmax(outputTensor) == groundTruth[i]:
                    correct += 1
                total += 1
    shallowTestAccuracyList.append(round(correct/total, 3))

middleCostList = []
middleTrainAccuracyList = []
middleTestAccuracyList = []
for index in range(EPOCHS):
   
    for batch in train:
        inputImages, groundTruth = batch
        middlenn.zero_grad()
        output = middlenn(inputImages.view(-1,784))
        cost = costFunc(output, groundTruth)
        cost.backward()
        middleOpt.step()
    middleCostList.append(cost.detach().numpy())
    
   
    correct = 0
    total = 0
    with torch.no_grad():
        for batch in train:
            inputImages, groundTruth = batch
            output = middlenn(inputImages.view(-1,784))
            for i, outputTensor in enumerate(output):
                if torch.argmax(outputTensor) == groundTruth[i]:
                    correct += 1
                total += 1
    middleTrainAccuracyList.append(round(correct/total, 3))

    
    correct = 0
    total = 0
    with torch.no_grad():
        for batch in test:
            inputImages, groundTruth = batch
            output = middlenn(inputImages.view(-1,784))
            for i, outputTensor in enumerate(output):
                if torch.argmax(outputTensor) == groundTruth[i]:
                    correct += 1
                total += 1
    middleTestAccuracyList.append(round(correct/total, 3))

deepCostList = []
deepTrainAccuracyList = []
deepTestAccuracyList = []
for index in range(EPOCHS):
    
    for batch in train:
        inputImages, groundTruth = batch
        deepnn.zero_grad()
        output = deepnn(inputImages.view(-1,784))
        cost = costFunc(output, groundTruth)
        cost.backward()
        deepOpt.step()
    deepCostList.append(cost.detach().numpy())
    
    
    correct = 0
    total = 0
    with torch.no_grad():
        for batch in train:
            inputImages, groundTruth = batch
            output = deepnn(inputImages.view(-1,784))
            for i, outputTensor in enumerate(output):
                if torch.argmax(outputTensor) == groundTruth[i]:
                    correct += 1
                total += 1
    deepTrainAccuracyList.append(round(correct/total, 3))

   
    correct = 0
    total = 0
    with torch.no_grad():
        for batch in test:
            inputImages, groundTruth = batch
            output = deepnn(inputImages.view(-1,784))
            for i, outputTensor in enumerate(output):
                if torch.argmax(outputTensor) == groundTruth[i]:
                    correct += 1
                total += 1
    deepTestAccuracyList.append(round(correct/total, 3))

plt.plot(counterList, shallowCostList, 'r', label='Shallow-1')
plt.plot(counterList, middleCostList, 'g', label='Middle-3')
plt.plot(counterList, deepCostList, 'b', label='Deep-5')
plt.title("Learning Progression for MNIST")
plt.xlabel("EPOCHS")
plt.ylabel("Cross Entropy Loss")
plt.legend(loc="upper right")
plt.show()

plt.plot(counterList, shallowTrainAccuracyList, 'r--', label='Shallow Train')
plt.plot(counterList, shallowTestAccuracyList, 'r', label='Shallow Test')
plt.plot(counterList, middleTrainAccuracyList, 'g--', label='Middle Train')
plt.plot(counterList, middleTestAccuracyList, 'g', label='Middle Test')
plt.plot(counterList, deepTrainAccuracyList, 'b--', label='Deep Train')
plt.plot(counterList, deepTestAccuracyList, 'b', label='Deep Test')
plt.title("Accuracy of NNs")
plt.xlabel("EPOCHS")
plt.ylabel("Accuracy")
plt.legend(loc="lower right")
plt.show()