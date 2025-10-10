## Check if subsequence exists with sum K
def isExists(arr,ans,i,k):
    if i == len(arr):
        sum = 0
        for val in ans:
            sum += val
        if sum == k:
            return 1
        
        return 0

    ans.append(arr[i])
    flag1 = isExists(arr,ans,i+1,k)

    ans.pop()
    flag2 = isExists(arr,ans,i+1,k)

    return flag2+flag1
    
arr = [4, 9, 2, 5, 1]
count = isExists(arr,[],0,10)
if count > 0:
    print(f"there exists {count} subsequence whose sum is equal to K")
else:
    print("there exists no subsequence whose sum is equal to K")

