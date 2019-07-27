''' Program to check whether number is prime or not '''
import math

def prime(num):
    for i in range(2,(num//2)+1):
        if(num%i==0):
            return False
    return True


inp=int(input("Enter Number To Check whether Number is Prime Or Not :"))
if(prime(inp)):
    print(f"{inp} is a Prime Number")
else:
    print(f"{inp} is not a Prime Number")