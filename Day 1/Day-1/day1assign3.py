''' Program to print prime  in a given range'''
import math

def prime(num):
    for i in range(2,(num//2)+1):
        if(num%i==0):
            return False
    return True


inp=int(input("Enter Start Range :"))
inp2=int(input("Enter End Range :"))
for i in range(inp,inp2+1):
    if(prime(i)):
        print(f"{i}",end=" ")