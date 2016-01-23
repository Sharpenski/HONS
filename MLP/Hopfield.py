'''
Created on 19 Jan 2016

@author: tobydobbs
'''

import numpy as np

#===============================================================================
# Hopfield:
# no self connections
# can be modeled as a matrix 
#===============================================================================
class Hopfield:
    
    def __init__(self, patterns):
        self.patterns = patterns # list of patterns to be learned
        self.noNodes = len(self.patterns)
        self.node_matrix = np.zeros(shape=(self.noNodes,self.noNodes), dtype=int) # matrix represents each connection within the network
        
    def train_hopfield(self):
        for pattern in self.patterns:
            self.const_contrib_matrix(pattern)
        
    def const_contrib_matrix(self, pattern):
        rows = len(self.node_matrix)
        columns = rows # matrix is always as long as it is wide
        for row in range(rows):
            for column in range(columns):
                print row, column
                print self.node_matrix[row][column]
        
    def add_matrices(self):
        print
        
    def pattern_recall(self):
        for pattern in self.patterns:
            print pattern
        
patterns = ["1110", "0101", "1001", "0110", "1110"]
hop = Hopfield(patterns)
hop.train_hopfield()
    
        
        