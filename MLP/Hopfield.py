'''
Created on 19 Jan 2016

@author: tobydobbs
'''

import numpy as np
import activation

#===============================================================================
# Hopfield (Recurrent Neural Network):
# no self connections
# can be modeled as a matrix 
#===============================================================================
class Hopfield:
    
    def __init__(self, patterns):
        self.patterns = patterns # list of patterns to be learned
        self.noNodes = len(self.patterns[0])
        self.node_matrix = np.zeros(shape=(self.noNodes,self.noNodes), dtype=int) # matrix represents each connection within the network
        print self.node_matrix
        self.train_hopfield()
        
    def train_hopfield(self):
        for pattern in self.patterns:
            self.const_contrib_matrix(pattern)
            print self.node_matrix
    
    # convert a binary number to bipolar
    def binary_to_bipolar(self, value):
        return (2 * int(value)) - 1
        
    # patterns converted from binary to boolean
    def const_contrib_matrix(self, pattern):
        rows = len(self.node_matrix)
        columns = rows # matrix is always as long as it is wide
        for row in range(rows):
            for column in range(row+1, columns): # matrix is symmetric so start from self-connection (i.e. matrix[i][i])
                self.node_matrix[row][column] += self.binary_to_bipolar(pattern[row]) * self.binary_to_bipolar(pattern[column])
                self.node_matrix[column][row] += self.node_matrix[row][column]
        
    def pattern_recall(self, pattern):
        activations = [] # store activation (signum output) for each pattern
        for row in range(self.noNodes):
            act = 0
            for column in range(self.noNodes):
                act += self.binary_to_bipolar(pattern[column]) * self.node_matrix[row][column]
            activations.append(activation.signum(act))
        return activations

def main():        
    patterns = ["0010","0001", "0001"]
    hop = Hopfield(patterns)
    print hop.pattern_recall(patterns[0])
    print hop.pattern_recall("1110")
    
if __name__ == "__main__":
    main()


    
        
        