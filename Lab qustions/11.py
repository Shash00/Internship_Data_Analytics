num1, num2, num3 = [int(i) for i in input('Enter 3 numbers: ').split(' ')]

def biggest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3
    
res = biggest(num1,num2,num3)

print(f"The biggest of {num1} {num2} {num3} is {res}")