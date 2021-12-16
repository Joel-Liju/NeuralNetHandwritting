import random
import math
def activation(value):
    return 1/(1+math.pow(math.e,-value))
def derActivation(value):
    return activation(value)*(1-activation(value))
"""
this is the node class
"""
class Node:
    def __init__(self):
        self.input = 0
        self.output = 0
        self.DO = 0
        self.DI = 0
        pass
    def addinput(self, input):
        self.input = self.input + input
    """
    this function calculates the error for each node
    """
    def calculateError(self,expectedVal):
        self.DO = self.output - expectedVal
        self.DI = self.DO * derActivation(self.input)
    """
    This function is used to pass the value forward
    """
    def passforward(self):
        pass
    def setOutput(self,output):
        self.output = output
    def Output(self):
        try:
            self.output  = activation(self.input)
        except:
            pass
    def reset(self):
        self.input = 0
        self.output = 0

"""
this is the layer class
"""
class Layer:
    def __init__(self,layersize):
        self.nodes = []
        for i in range(layersize):
            self.nodes.append(Node())
    """
    calculates the error for each node in the layer
    """
    def calculateError(self):
        pass
    """
    takes the activation function and sets the output 
    """
    def calculateOuput(self):
        for node in self.nodes:
            node.output = activation(node.input)
    def setOutput(self,output):
        for i in range(len(self.nodes)):
            self.nodes[i].output = output[i]

    def setInput(self, Input):
        for i in range(len(self.nodes)):
            self.nodes[i].input = Input[i]

"""
this is the NeuralNet
"""
class NeuralNet:
    def __init__(self, layersizes):
        random.seed(100)
        self.layers = []
        self.weights = []
        for i in range(len(layersizes)):#per layers
            self.layers.append(Layer(layersizes[i]))
            layerweight = []
            if i+1 < len(layersizes):
                for t in range(layersizes[i]):
                    eachLayer = []
                    for j in range(layersizes[i+1]):
                        t = random.random()
                        #print(t)
                        eachLayer.append(t)
                    layerweight.append(eachLayer)
                self.weights.append(layerweight)
    """
    this function takes the input given, and forward passes the information.
    """
    def forwardpass(self,values):
            self.layers[0].setInput(values)# first layer
            self.layers[0].setOutput(values)  # first layer
            for i in range(len(self.layers)):#each layer
                try:
                    for node in range(len(self.layers[i+1].nodes)):#for each node in next layer
                        for n in range(len(self.layers[i].nodes)):#for each node in current layer
                            self.layers[i+1].nodes[node].addinput(self.layers[i].nodes[n].output*self.weights[i][n][node])
                    self.layers[i+1].calculateOuput()
                except:
                    #output layer
                    pass
    """
    this function calculates the error for the neural network
    """
    def calculateError(self,output):
        meanSqauareError = 0
        for i in range(len(output)):#for each output
            meanSqauareError = meanSqauareError + (pow(output-self.layers[len(self.layers)-1],2))/2.0#gets the mean squared error
        pass
    """
    this does the backward pass.
    """
    def backwardPass(self):

        pass
            #self.layers[len(self.layers)-1].setOutput(output)#setting the outputs for training.