'''	Write a program to accept a number “n” from the user; then display the sum of the following series:
1/23+1/33+1/43 + ……+1/n3 '''


sum = 0

inp = int(input('Num:'))

for i in range (1,inp+1):
    sum+=1/i**3

print(sum)

