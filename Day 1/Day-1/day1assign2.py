''' Write a program to accept a number “n” from the user; then display the sum of the following series:
1+ 1/2 + 1/3 + …….+ 1/n '''

sum = 0

inp = int(input('Num:'))

for i in range (1,inp+1):
    sum+=1/i
print(sum)