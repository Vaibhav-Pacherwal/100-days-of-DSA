## Aggressive Cows Problem
def isPossible(arr,C,mid):
    arr.sort()
    cows,lastStallPos = 1,arr[0]
    for stall in arr:
        if stall-lastStallPos >= mid:
            cows += 1
            lastStallPos = stall
        if cows == C:
            return True
    
    return False

def aggCows(arr,C):
    start,end = min(arr),max(arr)-min(arr)
    ans = 0
    while start <= end:
        mid = int(start + (end-start)/2)

        if isPossible(arr,C,mid):
            ans = mid
            start = mid+1
        else:
            end = mid-1
    
    return ans

arr, C = [1,2,8,4,9], 3
ans = aggCows(arr,C)
print(ans)