'''
Created on 12 Jan 2016

@author: tobydobbs
'''

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def disgmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))

def tanh(x):
    return math.tanh(x)

def dtanh(x):
    return 1 - x**2

def nullFunc(x):
    return 0

def signum(x):
    if x < 0:
        return 0
    else: 
        return 1
    
def sine(x):
    return math.sin(x)
    
def threshold(x):
    print
    
# getFunc: returns the function associated with the func_name provided
def getFunc(func_name):
    functions = [sigmoid, tanh, nullFunc, signum, threshold, sine]
    for func in functions:
        if func.__name__ == func_name:
            return func
    raise Exception("The requested function is not available.")

def main():
    print tanh(-1)

if __name__ =="__main__":
    main()
