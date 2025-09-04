## rotate matrix by 90 degree
matrix = [[1,2,3], [4,5,6], [7,8,9]]

print(matrix)
rows = len(matrix)
for i in range(rows):
    for j in range(i, rows):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp

for i in range(0, rows):
    matrix[i].reverse()
    
print(matrix)