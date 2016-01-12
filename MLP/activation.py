'''
Created on 12 Jan 2016

@author: tobydobbs
'''

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def hyperbolic_tang(x):
    return math.tanh(x)

def nullFunc(x):
    return 0

def signum(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else: 
        return 1
    
def threshold(x):
    print
