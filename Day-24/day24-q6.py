## Binary Search Using Recursion
def binarySearch(arr,start,end,target):
    if start > end:
        return -1
    
    mid = int(start + (end-start)/2)

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binarySearch(arr,mid+1,end,target)
    else:
        return binarySearch(arr,start,mid-1,target)
    
arr = [1,2,3,4,5]
ans = binarySearch(arr,0,len(arr)-1,58)
print(ans)
