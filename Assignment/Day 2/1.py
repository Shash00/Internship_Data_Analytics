def split_number(num):
    digits = list()
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits


for num in range(1000, 10000):
    digits = split_number(num)
    if sum(digits) == 12 and digits[2] == digits[0] - digits[1] and digits[3] == digits[0] + digits[2]:
        print(num)

map()