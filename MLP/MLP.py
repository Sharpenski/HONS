'''
Created on 12 Dec 2015

@author: tobydobbs
'''

import activation
import random, math

#===============================================================================
# MLP: Class representing a new MLP
# user-defined number of layers
# predefined input-output mapping (supervised learning)
#===============================================================================
class MLP:
    
    def __init__(self, no_inputs, config):
        
        self.no_inputs = no_inputs 
        self.layers = []  
        self.insert_layers(config)
        
        print self

    # addLayer: insert layers, the new layer becomes the last element in the list
    def insert_layers(self, layer_sizes):
        
        self.layers.append(Neuron_Layer(0, layer_sizes[0], self.no_inputs)) # input layer
        
        for i in range(1, len(layer_sizes)-1):
            noLayers = len(self.layers)
            self.layers.append(Neuron_Layer(noLayers, layer_sizes[i], self.layers[noLayers-1].noNeurons))
            
        self.layers.append(Output_Layer(len(self.layers), layer_sizes[-1], self.layers[-1].noNeurons)) # output layer
           
    # feed_forward_online: online learning (example-by-example training)
    def feed_forward(self, input_example, bias):
        
        # print "Feeding input", input_example, "forward:"
           
        self.layers[0].feed_forward(input_example, bias) # first layer receives direct input (input layer)
        
        for layer_index in range(1, len(self.layers)): # iterate through remaining layers (hidden + output)
            next_input_ex = [] 
            for node in self.layers[layer_index - 1].neurons: # reference the node output
                next_input_ex.append(node.node_out)
            self.layers[layer_index].feed_forward(next_input_ex, bias)  
            
        return self.layers[-1].act_out     
        
    def calc_error(self, expected_output):
        
        # print "Calculating errors for entire network:"
        
        net_error = self.layers[-1].calc_error(expected_output) # calculate the initial error at the output layer
        
        for i in range(len(self.layers)-2, -1, -1): # iterate from the pen-ultimate layer backwards
            self.layers[i].calc_error(self.layers[i+1])
            
        return net_error    
            
    def update_synapses(self, learn_rate, mom_fact, input_example):
        
        # print "Updating synapses of network:", input_example
        
        self.layers[0].upd_weights_first(learn_rate, mom_fact, input_example)
        
        for i in range(1, len(self.layers)): # iterate from second hidden layer onwards
            self.layers[i].upd_weights(learn_rate, mom_fact, self.layers[i-1])
            
    def __repr__(self):
        
        mlp_info = ("\nThe MLP consists of:\n" + 
                str(self.no_inputs) + " inputs\n" +
                str(len(self.layers) + 1) + " layers (including the input layer)\n")
        
        layer_info = ""
        
        for i in range(len(self.layers)-1):
            layer_info += "Layer " + str(i) + " is comprised of " + str(len(self.layers[i].neurons)) + " nodes.\n" 
            
        layer_info += "The Output layer is comprised of " + str(len(self.layers[-1].neurons)) + " nodes.\n"
            
        return mlp_info + layer_info 
        
#===============================================================================
# Neuron_Layer: represents a layer within an MLP
#===============================================================================
class Neuron_Layer:
    
    def __init__(self, index, width, connections_per_node):
        
        self.noNeurons = 0
        self.index = index # the input layer will have index 1, the output layer will have index (length - 1)
        self.neurons = self.addNeurons(width, connections_per_node) # stores each Neuron within the layer (also used to find width)
        
    def addNeurons(self, width, connections_per_node):
        
        neuron_array = []
        
        while self.noNeurons < width:
            neuron_array.append(Neuron(connections_per_node))
            self.noNeurons += 1
            # print "A new node was added to layer " + str(self.index)
            
        return neuron_array
            
    def feed_forward(self, node_inputs, bias):
        
        # print "Feeding forward at layer", str(self.index)
        
        for node in self.neurons: # same inputs processed by each node in the layer
            # print "\tFeeding through node", node_inputs
            node.get_out_from_in(node_inputs, bias)
        
    # calc_error: error at hidden/input layers
    # weighted_sum: the weighted sum of node errors that receive a connection from the current node
    def calc_error(self, next_layer):
        
        # print "Calculating the error at layer", self.index 
        
        connected_nodes = next_layer.neurons # nodes of next layer
        weighted_sum = 0
        
        for i in range(len(self.neurons)): # index of each node in the current layer
            current_node = self.neurons[i] # references the current node of the current layer
            for node in connected_nodes: # nodes of next layer (reference the weight value of each connection)
                weighted_sum += node.weights[i] * node.out_error # weights[i] references the 'i'th node of the connecting layer
            current_node.out_error = (weighted_sum  * current_node.node_out) * current_node.node_out * (1 - current_node.node_out)
            
    # update weights: update the weight values in accordance with back propagation rules (training)
    def upd_weights(self, learn_rate, mom_fact, prev_layer):
        
        # print "Updating weights at layer:", self.index
        
        connecting_layer = prev_layer.neurons # the connecting layer
        
        for neuron in self.neurons: # 'i' references the receiving node
            for i in range(len(connecting_layer)): # 'j' references the connecting node
                neuron.deltas[i] = ((learn_rate * neuron.out_error * connecting_layer[i].node_out) + (mom_fact * neuron.deltas[i])) # calculate the delta
                neuron.weights[i] += neuron.deltas[i]
                
    def upd_weights_first(self, learn_rate, mom_fact, input_example):
        
        # print "Updating weights at layer: 0"
        # print "Inputs:", input_example
        
        for neuron in self.neurons: # iterate through neurons of the first hidden layer
            for i in range(len(input_example)): # iterate over all inputs from the input layer
                neuron.deltas[i] = ((learn_rate * neuron.out_error * input_example[i]) + (mom_fact * neuron.deltas[i])) # calculate the delta
                neuron.weights[i] += neuron.deltas[i]          
                
    def __repr__(self):
        
        return "Neuron_Layer " + str(self.index) + " has " + str(self.noNeurons) + " nodes."
    
#===============================================================================
# Output_Layer: all networks have exactly one output layer, error calculation treated independently of the other layers
#===============================================================================
class Output_Layer(Neuron_Layer):
    
    def __init__(self, index, width, connections_per_node):
        
        Neuron_Layer.__init__(self, index, width, connections_per_node)
        
        
    def feed_forward(self, layer_inputs, bias):
        
        # print "Feeding forward at the Output layer"
            
        for node_index in range(len(self.neurons)):
            # print "\tFeeding through node", layer_inputs
            self.neurons[node_index].get_out_from_in(layer_inputs, bias)  
            self.act_out = self.neurons[node_index].node_out 
             
    # @override    
    # calc_error: error at the output layer (treated independently)
    # note that the layer index is consistently, length_of_list - 1
    def calc_error(self, expected_output):
        
        # print "Calculating error at the Output layer"
        
        current_act = self.act_out
        current_exp = expected_output
        
        #print self.act_out, expected_output
        
        network_error = 0
        
        for i in range(len(self.neurons)):
            self.neurons[i].out_error = (current_exp - current_act) * current_act * (1 - current_act)
            network_error += self.neurons[i].out_error / len(self.neurons)
            #print "error", self.neurons[i].out_error
            
        return network_error
            
    def print_outputs(self):
        print "Network output: ", self.act_out
        
#===============================================================================
# Neuron: Represents an individual Neuron
#===============================================================================
class Neuron:
    
    def __init__(self, no_connections):
        
        self.weights = [0] * no_connections # stores the weight value of each incoming connection
        self.deltas = [0] * no_connections
        self.init_weights(-1, 1)
        self.function = self.assignActivation("sigmoid") # null function by default
        self.node_out = None
        
    # init_weights: initialize weights between two reasonable boundaries (i.e. between -5 and 5 at most)
    def init_weights(self, lower_bound, upper_bound):
        
        if lower_bound >= -5 and upper_bound <= 5:
            for i in range(len(self.weights)):
                self.weights[i] = random.uniform(lower_bound, upper_bound)
        else:
            raise Exception("The boundaries are constrained between -5 and 5")
    
    # assignActivation: each node can be assigned an activation function at the user's discretion
    def assignActivation(self, func_name):
        
        return activation.getFunc(func_name)
        
    # get_out_from_in: process the weighted sum of each input via the activation function
    def get_out_from_in(self, node_inputs, bias):
        
        # print "\tInput to node", node_inputs
        
        weighted_sum = 0
        
        for i in range(len(node_inputs)): # weights and inputs must have matching order (first input corresponds to first weight/synapse)
            # print "\t\t weighted_sum/weight/input -->", weighted_sum, self.weights[i], node_inputs[i]
            weighted_sum += self.weights[i] * node_inputs[i]
        
        #print "\tWeighted sum (Function input)", weighted_sum + bias
            
        self.node_out = self.function(weighted_sum + bias) # output is the activation function applied to the weighted sum
        
        #print "\tOutput (Function output)", self.node_out
    
    def __repr__(self):
        
        return "Neuron: " + str(self.weights) + " Output: " + str(self.node_out) + " Function:" + str(self.function)
    
#===========================================================================
# train_network_online: main method of the class regarding online learning (example-by-example network updating)
#===========================================================================
def train_network_online(mlp, learn_rate, mom_fact, no_epochs, in_out_map, bias):
    
    print "Training network in online mode:"
    
    no_examples = len(in_out_map)
    
    net_errors = [0] * len(in_out_map) # record error for ech input example
    net_outputs = [0] * len(in_out_map)
    avg_error = 0
    epoch = 0
    
    while epoch < no_epochs:
        
        avg_error = 0 
        print epoch, avg_error
        
        for i in range(no_examples):
            net_outputs[i] = mlp.feed_forward(in_out_map[i][0], bias)
            net_errors[i] = mlp.calc_error(in_out_map[i][1])
            mlp.update_synapses(learn_rate, mom_fact, in_out_map[i][0])
            
        for error in net_errors:
            avg_error += (abs(error) / len(net_errors))
            
        if avg_error < math.pow(1,-3) :
            break
        
        epoch += 1
        
    print "MLP has completed training"
    print "Average error: " + str(avg_error) 
    print net_outputs
    
    return mlp # return the newly trained MLP

#===============================================================================
# build_in_out_map
# construct an input-output mapping from the file provided as a parameter
#===============================================================================
def build_in_out_map(filename):
    
    file_to_read = open(filename, "r")
    io_map = []
    
    io_line = file_to_read.readline()
    
    while io_line:
        input_list = []
        value = io_line.split()
        for i in range(len(value)-1):
            input_list.append(float(value[i]))
        new_entry = (input_list, float(value[-1]))
        io_map.append(new_entry)
        io_line = file_to_read.readline()  
        
    return io_map
        
def main():
    
    filename = raw_input("Please specify the filename:\n")
    training_set = build_in_out_map("test_cases/" + filename)
    no_inputs = int(raw_input("Please specify the number of inputs for the network: "))
    no_layers = int(raw_input("Number of layers for Network:"))
    layers = []
    
    for i in range(no_layers):
        layers.append(int(raw_input("Width of layer " + str(i) + ": ")))
    
    mlp1 = MLP(no_inputs, layers) # construct a new MLP which takes 1 input  
    mlp1 = train_network_online(mlp1, 0.2, 0.5, 100000, training_set, 0.0) # MLP instance, learning rate, momentum factor, no.epochs
    
if __name__ == "__main__":
    main()
        
        