## Fibonacci Series
def fibo(n):
    if n == 0 or n == 1:
        return n

    return fibo(n-1) + fibo(n-2)

n = int(input("enter n:"))
print(f"{n}th fibonacci term:{fibo(n)}")