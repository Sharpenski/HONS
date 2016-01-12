'''
Created on 12 Dec 2015

@author: tobydobbs
'''

print "In the MLP module"

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
        
    def readParam(self, file_name):
        print file_name
        
    def getInfo(self):
        print ("The MLP consists of " + self.noLayers + "layers")
        
#===============================================================================
# Neuron_Layer: represents a layer within an MLP
#===============================================================================
class Neuron_Layer:
    
    def __init__(self, width):
        self.neurons = [] * width
        
#===============================================================================
# Neuron: Represents an individual Neuron
#===============================================================================
class Neuron:
    
    print "Neuron"   
        
#===============================================================================
# main: program called from here
#===============================================================================
def main():
    print "In the main method of MLP:"
    mlp1 = MLP("test_file.txt") 
    mlp1.getInfo()
    
if __name__ == "__main__":
    main()
        
        