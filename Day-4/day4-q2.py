## Print the matrix in spiral manner
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

ub, lb, rb, ltb = 0, len(matrix)-1, len(matrix[0])-1, 0
while ub <= lb and ltb <= rb:
    for i in range(ltb, rb+1):
        print(matrix[ub][i], end=" ")
    ub += 1

    for i in range(ub, lb+1):
        print(matrix[i][rb], end=" ")
    rb -= 1
    
    for i in range(rb, ltb-1, -1):
        print(matrix[lb][i], end=" ")
    lb -= 1
    
    for i in range(lb, ub-1, -1):
        print(matrix[i][ltb], end=" ")
    ltb += 1

print()



