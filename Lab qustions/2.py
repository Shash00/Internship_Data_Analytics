'''Finding factorial of a number'''

input_num = int(input('Enter a number to find the factorial:'))

def fact(num):
    if num == 0:
        return 1
    else:
        fact_val = num * fact(num-1)
        return fact_val
    

fact_val = fact(input_num)
print(f"Factorial of {input_num} is : {fact_val}")