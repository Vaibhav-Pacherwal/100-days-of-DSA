## Floor and Ceil in Sorted Array
nums = [3, 4, 4, 7, 8, 10]

target = int(input("enter target:"))

def floorAndCeil(nums, target):
    start, end = 0, len(nums)-1
    idx = -1
    while start <= end:
        mid = int(start + (end-start)/2)
        idx = mid

        if nums[mid] < target:
            start = mid+1

        elif nums[mid] > target:
            end = mid-1

        else:
            return [target,target]
        
    return idx

ceil = nums[floorAndCeil(nums, target)]
floor = nums[floorAndCeil(nums, target)-1]
print([floor,ceil])