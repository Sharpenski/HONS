'''
Created on 12 Dec 2015

@author: tobydobbs
'''

import activation
import random

#===============================================================================
# MLP: Class representing a new MLP
# user-defined number of layers
# predefined input-output mapping (supervised learning)
#===============================================================================
class MLP:
    
    def __init__(self, ins, outs):
        self.ins = ins 
        self.outs = outs
        self.layers = []  
        self.noLayers = 0

    # addLayer: insert a new layer to the MLP, the new layer becomes the last element in the list
    def addLayer(self, width):
        self.layers.append(Neuron_Layer(self.noLayers, width))
        self.noLayers += 1
        print "A new layer was added to the MLP."
    
    # returns the layer associated with an index    
    def getLayer(self, index):
        if len(self.layers) > index:
            return self.layers[index]
        else:
            raise Exception("The layer index is not valid")
           
    # feed_forward_online: online learning (example-by-example training)
    def feed_forward(self, input_ex):
        self.layers[0].feed_forward(input_ex) # first layer receives direct input (input layer)
        for layer_index in range(1, len(self.layers)): # iterate through remaining layers (hidden + output)
            next_input_ex = [] 
            for node in self.layers[layer_index - 1].neurons: # reference the node output
                next_input_ex.append(node.node_out)
            self.layers[layer_index].feed_forward(next_input_ex)       
        
    def calc_errors(self, learning_rate, momentum_factor):
        self.layers[-1].calc_error() # calculate the initial error at the output layer
        for i in range(len(self.layers)-2, 0, -1): # iterate from the pen-ultimate layer backwards
            self.layers[i].calc_error(self.getLayer(i+1))
            
    def update_synapses(self, learn_rate, mom_fact):
        for i in range(1, len(self.layers)):
            self.layers[i].upd_weights(learn_rate, mom_fact, self.layers[i-1])
            
    def train_network_online(self, learn_rate, mom_fact):
        if self.layers[0].noNeurons != len(self.ins):
            raise Exception("The number of inputs and nodes (in the input layer) must be equal")
        else:
            for net_in in self.ins:
                self.feed_forward(net_in) # feed input through the network
                self.calc_errors(learn_rate, mom_fact) # calculate the error, start at output layer and back-propagate
                self.update_synapses(learn_rate, mom_fact) # update the weight values of each synapse according to the calculate error            
        
#===============================================================================
# Neuron_Layer: represents a layer within an MLP
#===============================================================================
class Neuron_Layer:
    
    def __init__(self, index, width):
        self.noNeurons = 0
        self.index = index # the input layer will have index 1, the output layer will have index (length - 1)
        self.neurons = self.addNeurons(width) # stores each Neuron within the layer (also used to find width)
        
    def addNeurons(self, width):
        neuron_array = []
        while self.noNeurons < width:
            neuron_array.append(Neuron(self.noNeurons))
            self.noNeurons += 1
        return neuron_array
        
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
    def upd_weights(self, learn_rate, mom_fact, prev_layer):
        connecting_layer = prev_layer.neurons # the connecting layer
        for neuron in self.neurons: # 'i' references the receiving node
            for i in range(len(connecting_layer)): # 'j' references the connecting node
                neuron.deltas[i] = ((learn_rate * neuron.out_error * connecting_layer[i].node_out) + (mom_fact * neuron.deltas[i])) # calculate the delta
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
    
    def __init__(self, no_connections):
        self.weights = [] * no_connections # stores the weight value of each incoming connection
        self.deltas = [0] * no_connections
        self.init_weights(-1, 1)
        self.function = self.assignActivation("sigmoid") # null function by default
        
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
    
    ins = [0.1,0.2,0.3,0.4,0.5]
    outs = [0.1,0.2,0.3,0.4,0.5] 
    mlp1 = MLP(ins, outs) 
    mlp1.addLayer(3) # hidden 1
    mlp1.addLayer(3) # hidden 2
    mlp1.addLayer(1) # output 
    mlp1.train_network_online(0.01, 0.5)
    
if __name__ == "__main__":
    main()
        
        