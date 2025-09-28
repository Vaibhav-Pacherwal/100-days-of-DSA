## Split Array Largest Sum
def isValid(nums,k,mid):
    subArray,currSum = 1,0
    for num in nums:
        if num + currSum > mid:
            subArray += 1
            currSum = 0
        currSum += num
    
    if subArray <= k:
        return True
    
    return False


def splitArray(nums,k):
    ans = -1
    start,end = 0,sum(nums)
    while start <= end:
        mid = int(start + (end-start)/2)

        if isValid(nums,k,mid):
            ans = mid
            end = mid-1
        else:
            start = mid+1

    return ans

nums,k = [7,2,5,10,8],2
ans = splitArray(nums,k)
print(ans)
