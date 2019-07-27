num = input('Enter a number: ')

li = [int(i) for i in num]

li2 = [0 if i == 9 else i + 1 for i in li]

for i in li2:
    print(i, end= '')
