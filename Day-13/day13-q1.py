## square root of a number using binary search.
def sqrt(n):
    start,end = 1,n
    imperfectSqrt = 0
    while start <= end:
        mid = int(start + (end-start)/2)

        if mid*mid == n:
            return mid

        if mid < n:
            if mid*mid < n:
                imperfectSqrt = max(mid, imperfectSqrt)
                start = mid+1
            else:
                end = mid-1

        else:
            end = mid-1

    return imperfectSqrt

n = int(input("enter n:"))
root = sqrt(n)
print(f"sqrt of n:{root}")



