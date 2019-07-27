def sum_list(list1):
    sum = 0
    for i in list1:
        sum += int(i)

    return sum

inp = [int(i) for i in input('Enter list: ').split(' ')]
print(sum_list(inp))
