## Search in Rotated Sorted Array - II
nums = [1,0,1,1,1]
target = 0

start,end = 0,len(nums)-1
flag = False
while start <= end:
    mid = int(start + (end-start)/2)

    if nums[mid] == target:
        flag = True
        break

    if nums[start] == nums[mid] == nums[end]:
        start += 1
        end -= 1

    if nums[start] <= nums[mid]:
        if nums[start] <= target <= nums[mid]:
            end = mid-1
        else:
            start = mid+1

    if nums[mid] <= nums[end]:
        if nums[mid] <= target <= nums[end]:
            start = mid+1
        else:
            end = mid-1

print(flag)