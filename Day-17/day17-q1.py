## Painter's Partition Problem
def isVaild(arr,m,mid):
    painter,time = 1,0
    for board in arr:
        if board > mid:
            return False
        
        if time + board > mid:
            painter += 1
            time = 0
        time += board

    if painter > m:
        return False
    else:
        return True

def paintersPartition(arr,m):
    ans = 0
    start,end = 0,sum(arr)
    while start <= end:
        mid = int(start + (end-start)/2)
        
        if isVaild(arr,m,mid):
            ans = mid
            end = mid-1
        
        else:
            start = mid+1

    return ans

arr,m = [40,30,10,20],2
ans = paintersPartition(arr,m)
print(ans)