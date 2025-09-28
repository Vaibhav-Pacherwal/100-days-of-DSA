## Search a 2D Matrix
def binarySearch(nums,target):
    start,end = 0,len(nums)-1
    while start <= end:
        mid = int(start + (end-start)/2)

        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            start = mid+1
        
        else:
            end = mid-1

    return -1
    

def searchMatrix(matrix,target):
    for row in matrix:
        if binarySearch(row,target) != -1:
            return True
        
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = int(input("enter target:"))
print(searchMatrix(matrix,target))