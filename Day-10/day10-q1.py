## Find Minimum in Rotated Sorted Array
nums = [4,5,6,7,0,1,2]

def findMin(nums):
    start,end = 0,len(nums)-1
    target = float("inf")
    while start <= end:
        mid = int(start + (end-start)/2)

        if nums[mid] < target:
            target = nums[mid]

        if nums[mid] <= nums[end]:
            end = mid-1
        elif nums[mid] >= nums[start]:
            start = mid+1

    return target

tar = findMin(nums)
print(tar)