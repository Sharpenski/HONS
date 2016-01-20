'''
Created on 16 Jan 2016

@author: tobydobbs
'''

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
print y.name
