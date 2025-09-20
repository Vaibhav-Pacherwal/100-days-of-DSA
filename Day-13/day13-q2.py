## Nth Root of a Number using Binary Search
def nthRoot(m,n):
    start,end = 1,n
    while start <= end:
        mid = int(start + (end-start)/2)

        root = 1
        for i in range(1,m+1):
            root *= mid
        
        if root == n:
            return mid
        
        if root < n:
            start += 1
        else:
            end = mid-1

    return -1

n = int(input("enter n:"))
m = int(input("enter m:"))
root = nthRoot(n,m)
print(f"nth root of m:{root}")

