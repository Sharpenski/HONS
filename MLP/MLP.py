'''
Created on 12 Dec 2015

@author: tobydobbs
'''

import activation
import random

#===============================================================================
# MLP: Class representing a new MLP
# user-defined number of layers
# read required parameters in via a text file
#===============================================================================
class MLP:
    
    noLayers = 0
    
    def __init__(self, file_name):
        self.readParam(file_name)
        self.layers = []
        
    def addLayer(self):
        self.layers.append(Neuron_Layer())
        # print "A new layer was added to the MLP."
        
    def readParam(self, file_name):
        print file_name
        
    def getInfo(self):
        print ("The MLP consists of " + str(len(self.layers)) + " layers"), self.layers
        
#===============================================================================
# Neuron_Layer: represents a layer within an MLP
#===============================================================================
class Neuron_Layer:
    
    noNeurons = 0
    
    def __init__(self):
        self.neurons = [] # stores each Neuron within the layer (also used to find width)
        
    def addNeuron(self, toAdd):
        self.neurons.append(toAdd)
        self.noNeurons += 1
        # print "Added a new Neuron to the layer"
        
    def applyBias(self, bias):
        for node in self.neurons:
            node.weights.insert(0, bias)
        
    def printLayer(self):
        print self.neurons, len(self.neurons) 
    
    def __repr__(self):
        return "Neuron_Layer"
        
#===============================================================================
# Neuron: Represents an individual Neuron
#===============================================================================
class Neuron:
    
    def __init__(self):
        self.weights = [] # stores the weight value of each incoming connection
        
    #===========================================================================
    # init_weights: initialize weights between two reasonable boundaries (i.e. between -5 and 5 at most)
    #===========================================================================
    def init_weights(self, lower_bound, upper_bound):
        for weight in self.weights:
            weight = random.randint(lower_bound, upper_bound)
        
    def assignActivation(self, func_name):
        self.function = activation.getFunc(func_name)
        
    def printNeuron(self):
        print "The activation function of the Neuron is:", self.function.__name__
    
    def __repr__(self):
        return "Neuron string representation"
    
#===============================================================================
# back_propagate: train the network using back propagation
# note:
# the input to each node is: 
#     the summation of, the output of the previous layer * weight
#     the output is ordered from the first node to the last of the previous layer
#     the weights are ordered in the same way
#     note that the bias is the first input
#     the activation function is attached uniquely to each node
#===============================================================================
def back_propagate(learning_rate, momentum_factor):
    
    print learning_rate, momentum_factor
    
    #===========================================================================
    # calc_error: calculate the error at a particular node
    #===========================================================================
    def calc_error(node_name):
        return       
        
#===============================================================================
# main: program called from here
#===============================================================================
def main():
    print "In the main method of MLP:"
    
    mlp1 = MLP("test_file.txt") 
    mlp1.getInfo()
    mlp1.addLayer()
    print str(mlp1.layers[0])
    mlp1.addLayer()
    mlp1.addLayer()
    mlp1.getInfo()
    
    n1 = Neuron()
    print n1
    n1.assignActivation("sigmoid")
    n1.printNeuron()
    
    n2 = Neuron()
    n2.assignActivation("nullFunc")
    n2.printNeuron()
    
    nl1 = Neuron_Layer()
    print nl1
    
    nl1.addNeuron(n1)
    
if __name__ == "__main__":
    main()
        
        