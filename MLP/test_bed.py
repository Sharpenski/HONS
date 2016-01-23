'''
Created on 16 Jan 2016

@author: tobydobbs
'''

import time

weights = [0,2,3,4,1,5,4,3]

print weights

for i in range(len(weights)):
    weights[i] = 0
    
print weights

class Test:
    
    x = False
    g = 0
    
    def __init__(self):
        self.x = True
        Test.g += 1
        
    def sayHello(self):
        self.name = "Toby"
        print Test.g
        print "hello"
    
y = Test()
print y.x
print Test.g
Test().sayHello()
y.sayHello()
y.h = 100000
print y.name, y.h

def fibo_print():
    array = [1, 1]
    for x in range(2, 10):
        array.append(array[x-1] + array[x-2])
        time.sleep(0.3)
        print array[x]
        
fibo_print()
        

employee = str(raw_input("HI?\n"))
while employee:
    print "Hello", employee
    employee = str(raw_input())
