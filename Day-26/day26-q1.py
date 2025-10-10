## Print subsequence with sum K
def subSeqSumK(arr,ans,i,k):
    if i == len(arr):
        sum = 0
        for val in ans:
            sum += val
        if sum == k:
            print(ans,end=" ")
        return 
    
    ans.append(arr[i])
    subSeqSumK(arr,ans,i+1,k)

    ans.pop()
    subSeqSumK(arr,ans,i+1,k)


arr = [1,2,3]
subSeqSumK(arr,[],0,3)
print()