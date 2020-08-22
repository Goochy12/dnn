import numpy as np
import csv
import os

np.random.seed(0)

# inputs layer

# hidden layers

# output layer


def dot(x, y):
    if not x:
        return 0
    return x[0] * y[0] + dot(x[1:], y[1:])


class layer:
    def __init__(self, inputs, neurons):
        self.weights = np.random.randn(inputs, neurons)
        self.biases = np.zeros((1, neurons))

    def foward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

    def backward(self):
        pass


class dnn:
    def __init__(self, inputs):
        self.inputs = inputs
        return


def getInputs(filename):
    f = open(filename, 'r+')
    reader = csv.reader(f)
    inputs = []
    results = []
    for eachLine in reader:
        inputs.append(eachLine[:len(eachLine)-1])
        results.append(eachLine[len(eachLine)-1])
    return inputs[1:], results


X = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 1]])

if __name__ == "__main__":
    inputs, results = getInputs(os.path.join(
        os.path.dirname(__file__), "iris_flowers.csv"))
