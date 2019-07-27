def get_input(N):
    input_list = list()
    for i in range(0, N):
        input_list.append(int(input()))
    return input_list

N = int(input("How many elements: "))
print("Enter elements to list 1: ")
list_1 = get_input(N)
print("Enter elements to list 2: ")
list_2 = get_input(N)

list_res = list(map(lambda x, y : x + y, list_1, list_2))
print(list_res)