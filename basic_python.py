
# Factorial with lambda and math.factorial
import os 

if __name__ == "__main__": 
    for (root,dirs,files) in os.walk('.', topdown=1): 
        print (root) 
        print (dirs) 
        print (files) 
        print ('--------------------------------')

import math

y = lambda a : math.factorial(a)
a = 5 #input("Enter a number: ")
prinit(a, '! = ', y(a))

# Factorial
def factorial(x):
    if x == 1:
        return x
    else:
        return x*factorial(x-1)
    
n = 6 #input("Enter a number: ")
print( n, '!= ', factorial( int(n) ) )

