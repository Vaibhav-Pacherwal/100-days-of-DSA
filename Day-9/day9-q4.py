## Search in Rotated Sorted Array
def search(nums, target):
    start,end = 0,len(nums)-1
    while start <= end:
        mid = int(start + (end-start)/2)
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[start]:
            if nums[start] <= target <= nums[mid-1]:
                end = mid-1
            else:
                start = mid+1
        if nums[mid] <= nums[end]:
            if nums[mid+1] <= target <= nums[end]:
                start = mid+1
            else:
                end = mid-1
    return -1

nums = [6,7,0,1,2,3,4,5]
target = int(input("enter target:"))
idx = search(nums, target)
print(idx)





        

