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
    
    noMLPs = 0
    
    def __init__(self, file_name):
        # self.readParam(file_name)
        self.noLayers = 0
        self.layers = []
        MLP.noMLPs += 1
        

    # addLayer: insert a new layer to the MLP, the new layer becomes the last element in the list
    def addLayer(self):
        self.layers.append(Neuron_Layer(self.noLayers))
        self.noLayers += 1
        print "A new layer was added to the MLP."
        
    def readParam(self, file_name):
        print file_name
        
    def getInfo(self):
        print ("The MLP consists of " + str(len(self.layers)) + " layers"), self.layers
           
    # feed_forward_online: online learning (example-by-example training)
    def feed_forward_online(self, input_ex):
        if self.layers[0] != len(input_ex):
            raise Exception("The number of inputs and nodes (in the input layer) must be equal")
        else:
            print
        
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
    def back_propagate(self, learning_rate, momentum_factor):
        for layer_index in range(len(self.layers), 0, -1): # iterate from the outer-layer backwards
            print layer_index
            
    # calc_error_at_outputs: error at the output layer (treated independently)
    # note that the layer index is consistently, length_of_list - 1
    def calc_error_at_outputs(self, target_output, actual_output):
        return (target_output - actual_output) * actual_output * (1 - actual_output)
           
    # calc_error: error at hidden/input layers
    # weighted_sum: the weighted sum of node errors that receive a connection from the current node
    def calc_error(self, layer_index, activation_output):
        from_node_connections = self.layers[layer_index + 1].neurons # connected to all nodes of next layer (feed-forward)
        
        weighted_sum = 0
        for node in from_node_connections:
            print weighted_sum
        
#===============================================================================
# Neuron_Layer: represents a layer within an MLP
#===============================================================================
class Neuron_Layer:
    
    def __init__(self, name):
        self.name = name
        self.neurons = [] # stores each Neuron within the layer (also used to find width)
        self.noNeurons = 0
        
    def addNeuron(self):
        self.neurons.append(Neuron(self.noNeurons))
        self.noNeurons += 1
        # print "Added a new Neuron to the layer"
        
    # applyBias: the bias is weighted by 1, universally across the layer
    def applyBias(self, bias):
        for node in self.neurons:
            node.weights.insert(0, 1)
        
    def printLayer(self):
        print self.neurons, len(self.neurons) 
    
    def __repr__(self):
        return "Neuron_Layer string representation"
        
#===============================================================================
# Neuron: Represents an individual Neuron
#===============================================================================
class Neuron:
    
    def __init__(self, name):
        self.weights = [] # stores the weight value of each incoming connection
        self.function = activation.nullFunc() # null function by default
        self.node_output = 0 # store the output for use in training
        
    # init_weights: initialize weights between two reasonable boundaries (i.e. between -5 and 5 at most)
    def init_weights(self, lower_bound, upper_bound):
        if lower_bound >= -5 and upper_bound <= 5:
            for i in range(len(self.weights)):
                self.weights[i] = random.uniform(lower_bound, upper_bound)
        else:
            raise Exception("The boundaries are constrained between -5 and 5")
        
    # assignActivation: each node can be assigned an activation function at the user's discretion
    def assignActivation(self, func_name):
        self.function = activation.getFunc(func_name)
        
    def printNeuron(self):
        print ("The activation function of the", self.name, "is:", self.function.__name__ +
               "The weights of each input connection are:", self.weights)
        
    # get_out_from_in: process the weighted sum of each input via the activation function
    def get_out_from_in(self, node_inputs):
        weighted_sum = 0
        for i in range(len(node_inputs)): # weights and inputs must have matching order
            weighted_sum += self.weights[i] * node_inputs[i]
        self.node_output = self.function(weighted_sum) # output is the activation function applied to the weighted sum
    
    def __repr__(self):
        return "Neuron string representation"
        
def main():
    print "In the main method of MLP:"
    
    mlp1 = MLP("test_file.txt")    
    mlp1.addLayer()
    mlp1.addLayer() 
    mlp1.addLayer()
    mlp1.back_propagate(0.05, 0.01)
    
if __name__ == "__main__":
    main()
        
        