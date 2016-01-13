'''
Created on 12 Dec 2015

@author: tobydobbs
'''

import activation

#===============================================================================
# MLP: Class representing a new MLP
# user-defined number of layers
# read required parameters in via a text file
#===============================================================================
class MLP:
    
    noLayers = 0
    
    def __init__(self, file_name):
        self.readParam(file_name)
        self.neurons = []
        
    def addLayer(self):
        self.noLayers += 1
        
    def readParam(self, file_name):
        print file_name
        
    def getInfo(self):
        print ("The MLP consists of " + str(self.noLayers) + " layers")
        
#===============================================================================
# Neuron_Layer: represents a layer within an MLP
#===============================================================================
class Neuron_Layer:
    
    def __init__(self):
        self.neurons = [] # stores each Neuron within the layer
        
    def addNeuron(self, toAdd):
        self.neurons.append(toAdd)
        print "Added a new Neuron to the layer"
        
    def printLayer(self):
        print self.neurons, len(self.neurons)
        
#===============================================================================
# Neuron: Represents an individual Neuron
#===============================================================================
class Neuron:
    
    def __init__(self):
        self.weights = [] # stores the weight value of each incoming connection
        
    def assignActivation(self, func_name):
        self.function = activation.getFunc(func_name)
        
    def printNeuron(self):
        print "The activation function of the Neuron is:", self.function.__name__
        
#===============================================================================
# back_propagate: train the network using back propagation
#===============================================================================
def back_propagate(learning_rate, momentum_factor):
    
    print learning_rate, momentum_factor
          
        
#===============================================================================
# main: program called from here
#===============================================================================
def main():
    print "In the main method of MLP:"
    
    mlp1 = MLP("test_file.txt") 
    mlp1.getInfo()
    
    nl1 = Neuron_Layer(8)
    nl1.printLayer()
    
    n1 = Neuron()
    n1.assignActivation("sigmoid")
    n1.printNeuron()
    
    nl1.addNeuron(n1)
    
if __name__ == "__main__":
    main()
        
        