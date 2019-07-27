from functools import reduce
print("\nEnter the numbers, type 'done' to stop entering")
numbers = list()
while(True):
    input_data = input(">> ")
    if(input_data == "done"):
        break
    numbers.append(int(input_data))

even = filter(lambda x : x % 2 == 0, numbers)
sqaures = map(lambda x : x ** 2, even)
res = reduce(lambda x, y : x + y, sqaures)
print(res)