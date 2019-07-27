import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True 

num = input('Enter a number: ')

li = [int(i) for i in num]
count = 0
for i in li:
    if is_prime(i):
        count += 1

print(f"No of prime numbers:{count} ")

