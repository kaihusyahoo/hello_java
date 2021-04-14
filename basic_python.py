
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

print('Using math.factorial function:')
y = lambda a : math.factorial(a)
a = 5 #input("Enter a number: ")
print('{} != {}'.format(a, y(a)))

# Factorial
def factorial(x):
    if x == 1:
        return x
    else:
        return x*factorial(x-1)

# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
def fibonacci (x):
    if x <= 1:
        return x
    else:
        return fibonacci(x-1) + fibonacci(x-2)

print('Factorial of n:')
n = int(6) #input("Enter a number: ")
print( factorial(n) )
print('{} != {}'.format(n, factorial(n)))

print('A Fibonacci sequence:')
x = int(5)  #(input("How many terms? "))
print("Fibonacci sequence:")
for i in range(x):
     print(fibonacci(i))
