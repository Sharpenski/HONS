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
    else: 
        return 1
    
def threshold(x):
    print
    
# getFunc: returns the function associated with the func_name provided
def getFunc(func_name):
    functions = [sigmoid, hyperbolic_tang, nullFunc, signum, threshold]
    for func in functions:
        if func.__name__ == func_name:
            return func
    raise Exception("The requested function is not available.")
