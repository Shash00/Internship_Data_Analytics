from functools import reduce

def get_input(N):
    input_list = list()
    for i in range(0, N):
        input_list.append(int(input()))
    return input_list

N = int(input("How many elements: "))
numbers = get_input(N)
res = reduce(lambda x, y : x + y, numbers )
print(f"Sum : {res}")