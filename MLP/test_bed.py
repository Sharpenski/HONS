'''
Created on 16 Jan 2016

@author: tobydobbs
'''

import time

print "hello"

def fibo_print():
    array = [0, 1]
    for x in range(2, 10):
        array.append(array[x-1] + array[x-2])
        time.sleep(0.3)
        print array[x]
        
#fibo_print()

def swap(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
    
"""friends = ["Arthur", "Brain", "Buster", "Francine"]
hier = [0] * 4
relation = str(raw_input())
while relation:
    best = friends.index(relation.split()[0])
    worst = friends.index(relation.split()[1])
    hier[worst] = hier[best] + 1
    if best > worst:
        swap(friends, best, worst)
        swap(hier, best, worst)
    print friends
    print hier
    relation = str(raw_input())

lowest = 0    
for i in range(1, len(hier)):
    if hier[i] > hier[lowest]:
        lowest = i
    
print friends[lowest]"""

print "\n\n\n"

a = []
a.append(9)
print a[0], a
a[0] = a[0] * 2
print a[0], a
    
    


