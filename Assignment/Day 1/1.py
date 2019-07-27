'''1.	Write a program to accept a number and determine whether it is a prime number or not.'''

import math

def is_prime(num):
    '''Returns True if number is prime otherwise returns False'''
    if num < 2:
        return False 
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")