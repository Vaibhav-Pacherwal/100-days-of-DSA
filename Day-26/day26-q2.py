## Count subsequence with sum K
def subSeqCount(arr,ans,i,k):
    if i == len(arr):
        sum = 0
        for val in ans:
            sum += val
        if sum == k:
            return 1
        
        return 0
    
    ans.append(arr[i])
    inc = subSeqCount(arr,ans,i+1,k)

    ans.pop()
    exc = subSeqCount(arr,ans,i+1,k)

    return inc+exc

arr = [4, 9, 2, 5, 1]
count = subSeqCount(arr,[],0,10)
print(count)