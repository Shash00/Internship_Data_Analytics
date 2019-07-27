matrix = list()
m = int(input("Enter no. of rows: "))
n = int(input("Enter no. of columns: "))
for i in range(m):
    temp = list()
    for j in range(n):
        temp.append(int(input(f"Enter Row {i} Column {j}: ")))
    matrix.append(temp)

matrix_max = matrix[0][0]
matrix_min = matrix[0][0]
row_max = list()
row_min = list()
col_min = list()
col_max = list()

for rows in matrix:
    row_max.append(max(rows))
    row_min.append(min(rows))
    for ele in rows:
        if ele > matrix_max:
            matrix_max = ele
        if ele < matrix_min:
            matrix_min = ele
for i in range(n):
    for j in range(m):
        print(matrix[i][j])

print(f"Matrix minimum : {matrix_min}")
print(f"Matrix maximum : {matrix_max}")
print(f"Row maximum : {row_max}")
print(f"Row minimum : {row_min}")
# print(f"Column maximum : {column_max}")