## Factorial using Recursion
def fact(n):
    if n == 1:
        return 1
    
    return n * fact(n-1)

n = int(input("enter n:"))
factorial = fact(n)
print(f"factorial of {n}:{factorial}")