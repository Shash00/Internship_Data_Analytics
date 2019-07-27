'''
2.	Write a program to accept a number “n” from the user; then display the sum of the following series:
1+ 1/2 + 1/3 + …….+ 1/n
'''

def solve(num):
    '''
    returns the sum of the series 1+ 1/2 + 1/3 + …….+ 1/num
    '''
    res = 0
    for i in range(1, num + 1):
        res = res +  (1 / i)
    return res

num = int(input("Enter a number: "))
res = solve(num)

print(res)