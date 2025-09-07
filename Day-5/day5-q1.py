## Pascal's Triangle
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

row = int(input("enter row:"))

for i in range(1, row+1):
    for j in range(1, i+1):
        pascalEle = fact(i-1)/(fact(j-1)*fact(i-j)) 
        print(int(pascalEle), end=' ')
    print()