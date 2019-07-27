def pascals_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascals_triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

no_of_rows = int(input("Enter rows: "))
res = pascals_triangle(no_of_rows)
c_row = 0
for rows in res:
    for i in range(0, no_of_rows - c_row):
        print(end=" ")

    for ele in rows:
        print(ele, end=" ")
    print()
    c_row += 1