m = int(input("Enter m : "))
n  = int(input("Enter n : "))
res = 1
if n > 0:
    for i in range(0, n):
        res *= m
print(res)