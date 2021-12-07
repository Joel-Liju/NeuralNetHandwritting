import random
def activation(value):
    return 0
"""
this is the node class
"""
class Node:
    def __init__(self):
        pass
    def output(self,input):
        self.output = input
    def addinput(self, input):
        self.input = self.input + input
    """
    This function is used to pass the value forward
    """
    def passforward(self):
        pass
    def output(self):
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
this is the NeuralNet
"""
class NeuralNet:
    def __init__(self, layersizes):
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
