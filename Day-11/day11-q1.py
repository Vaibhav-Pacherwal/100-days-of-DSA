## Single Element in a Sorted Array
def findSingle(nums):
    n = len(nums)
    start,end = 0,n-1
    while start <= end:
        mid = int(start + (end-start)/2)

        if (mid == 0 or nums[mid-1] != nums[mid])\
        and (mid == n-1 or nums[mid] != nums[mid+1]):
            return nums[mid]
        
        if mid%2 == 0:
            if nums[mid-1] == nums[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if nums[mid-1] == nums[mid]:
                start = mid+1
            else:
                end = mid-1

nums = [1,1,2,3,3,4,4,8,8]
singleElement = findSingle(nums)

print(singleElement)

