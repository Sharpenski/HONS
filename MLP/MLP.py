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
        self.layers = []
        
    def addLayer(self):
        self.layers.append(Neuron_Layer())
        print "A new layer was added to the MLP."
        
    def readParam(self, file_name):
        print file_name
        
    def getInfo(self):
        print ("The MLP consists of " + str(len(self.layers)) + " layers"), self.layers
        
#===============================================================================
# Neuron_Layer: represents a layer within an MLP
#===============================================================================
class Neuron_Layer:
    
    def __init__(self):
        self.neurons = [] # stores each Neuron within the layer (also used to find width)
        
    def addNeuron(self, toAdd):
        self.neurons.append(toAdd)
        print "Added a new Neuron to the layer"
        
    def printLayer(self):
        print self.neurons, len(self.neurons) 
        
    def __str__(self):
        return "Neuron_Layer"
    
    def __repr__(self):
        return "Neuron_Layer"
        
#===============================================================================
# Neuron: Represents an individual Neuron
#===============================================================================
class Neuron:
    
    def __init__(self):
        self.weights = [] # stores the weight value of each incoming connection
        
    def init_weights(self):
        print
        
    def assignActivation(self, func_name):
        self.function = activation.getFunc(func_name)
        
    def printNeuron(self):
        print "The activation function of the Neuron is:", self.function.__name__
        
    def __str__(self):
        return "Neuron string rep"
    
    def __repr__(self):
        return "Neuron string rep"
    
#===============================================================================
# back_propagate: train the network using back propagation
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
    
    nl1 = Neuron_Layer()
    print nl1
    
    nl1.addNeuron(n1)
    
if __name__ == "__main__":
    main()
        
        