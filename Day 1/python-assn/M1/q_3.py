'''
3.	Write a program to accept 2 different numbers from the user and print all the prime numbers between these 2 numbers.
'''

import math

def is_prime(num):
    '''Returns True if number is prime otherwise returns False'''
    if num < 2:
        return False 
    else:
        for i in range(2, int(math.sqrt(num)) + 1 ):
            if num % i == 0:
                return False
    return True

lb = int(input("Enter lower bound: "))
ub = int(input("Enter upper bound: "))

for i in range(lb, ub+1):
    if is_prime(i):
        print(f"{i}",end=" ")
print()
