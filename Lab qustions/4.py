import math

lower_val = int(input('Enter the lower bound value: '))
upper_val = int(input('Enter the upper bound value: '))


def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True 


for i in range(lower_val, upper_val):
    val = is_prime(i)
    if is_prime(i):
        print(i)
    

