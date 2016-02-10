'''
Created on 19 Jan 2016

@author: tobydobbs
'''

import numpy as np
import activation

#===============================================================================
# Hop-field (Recurrent Neural Network):
# no self connections
# can be modeled as a matrix 
#===============================================================================
class Hopfield:
    
    def __init__(self, patterns):
        
        self.patterns = patterns # list of patterns to be learned
        self.noNodes = len(self.patterns[0])
        self.node_matrix = np.zeros(shape=(self.noNodes,self.noNodes), dtype=int) # matrix represents each connection within the network
        self.previous = 0
    
    # convert a binary number to bipolar
    def binary_to_bipolar(self, value):
        
        return (2 * int(value)) - 1
        
    # patterns converted from binary to boolean
    def const_contrib_matrix(self, pattern):
        
        rows = len(self.node_matrix)
        columns = rows # matrix is always as long as it is wide
        
        for row in range(rows):
            for column in range(columns): # matrix is symmetric so start from self-connection (i.e. matrix[i][i])
                self.node_matrix[row][column] += (self.binary_to_bipolar(pattern[row]) * self.binary_to_bipolar(pattern[column])) + self.previous
                
        self.set_diag_to_zero()
        
        print self.node_matrix, "\n"
    
    # set the diagonals of a matrix to be 0    
    def set_diag_to_zero(self):
        
        for i in range(len(self.node_matrix)):
            self.node_matrix[i][i] = 0
     
    # recall a pattern from the matrix    
    def pattern_recall(self, pattern):
        
        activations = [] # store activation (signum output) for each pattern
        
        for row in range(self.noNodes):
            act = 0
            for column in range(self.noNodes):
                act += int(pattern[column]) * self.node_matrix[row][column]    
            activations.append(activation.signum(act))
            
        return activations

# train the network on given set of patterns    
def train_hopfield(hnn):
          
    for pattern in hnn.patterns: 
        hnn.const_contrib_matrix(pattern)
        
    print hnn.node_matrix, "\n"

def main():     
          
    patterns = ["1010010101010101110111", "0000000000000000000001"]
    hop = Hopfield(patterns)
    train_hopfield(hop)
     
    for pattern in patterns:
        print hop.pattern_recall(pattern)  
    
if __name__ == "__main__":
    main()


    
        
        