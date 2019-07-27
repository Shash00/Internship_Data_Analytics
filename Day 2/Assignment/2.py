R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:")) 

matrix = []
minRow = []
maxRow = []
minCol = []
maxCol = []

print("Enter the entries row wise:")

for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

for i in matrix:
    minRow.append(min(i))
    maxRow.append(max(i))
    min1 = min(minRow)
    max1 = max(maxRow)

trans = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for i in trans:
    minCol.append(min(i))
    maxCol.append(max(i))

print(matrix)
print(f"Minimum:{min1}, Maximum:{max1}, Min Row:{minRow}, Max Row:{maxRow}, Min Col:{minCol}, Max Col:{maxCol}")



