# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 23:01:03 2016

@author: nshah
"""

friends = ['john', 'pat', 'gary', 'michael']
for i,name in enumerate(friends):
    print('name ',i,' is ',name)


# How many friends contain the letter 'a' ?
count_a = 0
for name in friends:
    if 'a' in name:
        count_a+=1
        
print( ( count_a / len(friends)), " percent of the names contain an 'a'") 

# Say hi to all friends
def print_hi(name, greeting='hello '):
     return greeting + name
nameslist = map(print_hi, friends)

# Print sorted names out
friends.sort()
print("Sorted Names: ", friends)



#
#   Calculate the factorial N! = N * (N-1) * (N-2) * ...
#

def factorial(x):
    """
    Calculate factorial of number
    :param N: Number to use
    :return: x!
    """
    if x==1: 
        return 1
    else:
        return x*factorial(x-1)
 
print ("The value of 5! is", factorial(5))
