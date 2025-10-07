## Recursion
def printNum(n):
    if n == 0:
        return

    print(n, end=" ")
    printNum(n-1)

printNum(5)