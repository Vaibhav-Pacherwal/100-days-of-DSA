## Book Allocation 
def isValid(arr,n,m,mid):
    st,pages = 1,0
    for i in range(n):
        if arr[i] > mid:
            return False
        
        if arr[i] + pages > mid:
            st += 1
            pages = 0
        pages += arr[i]
    
    if st > m:
        return False
    
    return True

def bookAllocation(arr,n,m):
    if m > n:
        return -1

    ans = -1
    start,end = 0,sum(arr)
    while start <= end:
        mid = int(start + (end-start)/2)

        if isValid(arr,n,m,mid):
            ans = mid
            end = mid-1
        else:
            start = mid+1

    return ans

arr = [15,17,20]
n,m = 3,2
ans = bookAllocation(arr,n,m)
print(ans)