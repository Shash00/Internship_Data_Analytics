input_num = int(input('Enter a number to find the sum of digits: '))

def sum_of_digits(num):
    rem = 0
    sum = 0
    while num > 0:
        rem = num % 10
        sum += rem
        num = num // 10
    
    if sum >= 10:
        sum_of_digits(sum)
    else:
        print(sum)

sum_of_digits(input_num)
