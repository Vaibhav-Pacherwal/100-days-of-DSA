## Search in a row and column wise sorted matrix
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

target = int(input("enter target:"))
row,col = 0,len(matrix[0])-1
while row < len(matrix) or col >= 0:
    if matrix[row][col] == target:
        print([row,col])
        break

    if matrix[row][col] < target:
        row += 1
    
    if matrix[row][col] > target:
        col -= 1

print([-1,-1])