## N sum using recursion
def nSum(n):
    if n == 1:
        return 1

    return n + nSum(n-1)

n = int(input("enter num:"))
print(f"sum of first {n} natural numbers:{nSum(n)}")