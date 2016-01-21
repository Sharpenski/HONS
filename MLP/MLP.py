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
    
    def __init__(self, file_name):
        # self.readParam(file_name)
        self.layers = []  

    # addLayer: insert a new layer to the MLP, the new layer becomes the last element in the list
    def addLayer(self):
        self.layers.append(Neuron_Layer(len(self.layers)))
        print "A new layer was added to the MLP."
        
    def readParam(self, file_name):
        print file_name
    
    # returns the layer associated with an index    
    def getLayer(self, index):
        if len(self.layers) > index:
            return self.layers[index]
        else:
            raise Exception("The layer index is not valid")
           
    # feed_forward_online: online learning (example-by-example training)
    def feed_forward_online(self, input_ex):
        if self.layers[0] != len(input_ex):
            raise Exception("The number of inputs and nodes (in the input layer) must be equal")
        else:
            self.layers[0].feed_forward(input_ex) # first layer receives direct input (input layer)
            for layer_index in range(1, len(self.layers)): # iterate through remaining layers (hidden + output)
                next_input_ex = [] 
                for node in self.layers[layer_index - 1].neurons: # reference the node output
                    next_input_ex.append(node.node_out)
                self.layers[layer_index].feed_forward(next_input_ex)       
        
    def calc_errors(self, learning_rate, momentum_factor):
        self.layers[-1].calc_error()
        for i in range(len(self.layers)-2, 0, -1): # iterate from the penultimate layer backwards
            self.layers[i].calc_error(self.getLayer(i+1))
        
#===============================================================================
# Neuron_Layer: represents a layer within an MLP
#===============================================================================
class Neuron_Layer:
    
    def __init__(self, index):
        self.index = index # the input layer will have index 1, the output layer will have index (length - 1)
        self.neurons = [] # stores each Neuron within the layer (also used to find width)
        self.noNeurons = 0
        
    def addNeuron(self):
        self.neurons.append(Neuron(self.noNeurons))
        self.noNeurons += 1
        
    # applyBias: the bias is weighted by 1, universally across the layer
    def applyBias(self, bias):
        for node in self.neurons:
            node.weights.append(1)
            
    def feed_forward(self, node_inputs):
        for node in self.neurons: # same inputs processed by each node in the layer
            node.get_out_from_in(node_inputs)
        
    # calc_error: error at hidden/input layers
    # weighted_sum: the weighted sum of node errors that receive a connection from the current node
    def calc_error(self, next_layer):
        connected_nodes = next_layer.neurons # nodes of next layer
        weighted_sum = 0
        for i in range(len(self.neurons)): # index of each node in the current layer
            current_node = self.neurons[i] # references the current node of the current layer
            for node in connected_nodes: # nodes of next layer (reference the weight value of each connection)
                weighted_sum += node.weights[i] * node.out_error # weights[i] references the 'i'th node of the connecting layer
            current_node.out_error = weighted_sum  * current_node.node_out * (current_node.node_out - 1) 
            
    # update weights: update the weight values in accordance with back propagation rules (training)
    def upd_weights(self, learning_rate, momentum_fact, prev_layer):
        connecting_layer = prev_layer.neurons # the connecting layer
        for neuron in self.neurons: # 'i' references the receiving node
            for i in range(len(connecting_layer)): # 'j' references the connecting node
                neuron.deltas[i] = ((learning_rate * neuron.out_error * connecting_layer[i].node_out) + (momentum_fact * neuron.deltas[i])) # calculate the delta
                neuron.weights[i] += neuron.deltas[i]
                
    def __repr__(self):
        return "Neuron_Layer " + str(self.index) + " has " + str(self.noNeurons) + " neurons."
    
#===============================================================================
# Output_Layer: all networks have exactly one output layer, error calculation treated independently of the other layers
#===============================================================================
class Output_Layer(Neuron_Layer):
    
    def __init__(self, exp_out):
        Neuron_Layer.__init__(self, "Output")
        self.exp_out = exp_out # store expected outputs
        self.act_out = [] # record actual outputs
     
    # @override    
    # calc_error: error at the output layer (treated independently)
    # note that the layer index is consistently, length_of_list - 1
    def calc_error(self):
        for i in range(len(self.neurons)):
            current_act = self.act_out[i]
            current_exp = self.exp_out[i]
            self.act_out.append((current_exp - current_act) * current_act * (1 - current_act))
        
#===============================================================================
# Neuron: Represents an individual Neuron
#===============================================================================
class Neuron:
    
    def __init__(self, name, function, no_connections):
        self.weights = [] * no_connections # stores the weight value of each incoming connection
        self.init_weights(-1, 1)
        self.deltas = [0] * no_connections
        self.function = self.assignActivation(function) # null function by default
        
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
        
    # get_out_from_in: process the weighted sum of each input via the activation function
    def get_out_from_in(self, node_inputs):
        weighted_sum = 0
        for i in range(len(node_inputs)): # weights and inputs must have matching order
            weighted_sum += self.weights[i] * node_inputs[i]
        self.node_out = self.function(weighted_sum) # output is the activation function applied to the weighted sum
    
    def __repr__(self):
        return "Neuron string representation"
        
def main():
    print "In the main method of MLP:"
    
    mlp1 = MLP("test_file.txt")    
    mlp1.addLayer()
    mlp1.addLayer() 
    mlp1.addLayer()
    print mlp1.layers
    
if __name__ == "__main__":
    main()
        
        