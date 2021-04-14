
# Factorial with lambda and math.factorial
import os 

if __name__ == "__main__": 
    if False:
       for (root,dirs,files) in os.walk('.', topdown=1): 
          print (root) 
          print (dirs) 
          print (files) 
          print ('--------------------------------')
    # get the current directory
    thisdir = os.getcwd()
    print(thisdir)
    arr = next(os.walk('.'))[2]   # os.walk(): list files of a tree
    print(arr)
    #arr = os.listdir()            # os.listdir(): list in the current directory
    #print(arr)

import math

y = lambda a : math.factorial(a)
a = 5 #input("Enter a number: ")
print('{} != {}'.format(a, y(a)))

# Factorial
def factorial(x):
    if x == 1:
        return x
    else:
        return x*factorial(x-1)
    
n = 6 #input("Enter a number: ")
print( factorial( int(n) ) )
print('{} != {}'.format(n, factorial(int(n))))

