def sum1(num):
    sum2 = 0
    while num != 0:
        sum2 = sum2 + num % 10
        num = num // 10
    return sum2 == 12


def split(num):
    temp = num
    temp, a1 = temp % 1000, temp // 1000
    temp, b1 = temp % 100, temp // 100
    temp, c1 = temp % 10, temp // 10
    temp, d1 = temp % 1, temp // 1

    return a1, b1, c1, d1


for i in range(1000, 10000):
    if sum1(i):
        a, b, c, d = split(i)
        if a - b == c and a + c == d:
            print(i)


