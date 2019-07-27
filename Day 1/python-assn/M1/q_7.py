def split_number(num):
    digits = list()
    while num > 0:    
        digits.append(num % 10)
        num = num//10
    return digits

def digit_sum(num):
    while num >= 10:
        digits = split_number(num)
        num = sum(digits)
    return num


N = int(input("enter a number: "))
digits = split_number(N)
res = digit_sum(sum(digits))

print(res)