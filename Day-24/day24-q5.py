## Check if array is sorted
def isSorted(arr,n):
    if n == 1:
        return True
    
    if arr[n-1] < arr[n-2]:
        return False
    
    return isSorted(arr,n-1)

arr = [1,2,8,4,5]
if isSorted(arr,len(arr)):
    print("true")
else:
    print("false")
