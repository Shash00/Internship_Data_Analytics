num = int(input('Enter num:'))

while num > 9:
    num = (num % 10 + num // 10)

print(num)