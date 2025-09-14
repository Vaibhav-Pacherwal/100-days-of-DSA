## Binary Search
nums = [-1,0,3,4,5,8,12]

target = int(input("enter target:"))
start, end, default = 0, len(nums)-1, -1
while start <= end:
    mid = int(start + (end-start)/2)

    if target < nums[mid]:
        end = mid-1

    elif target > nums[mid]:
        start = mid+1

    else:
        default = mid
        print(f"{target} is at index {mid}.")
        break

if default == -1:
    print(f"{target} does not exists in nums.")
        
## Using Recurrsion
nums = [-1,0,3,4,5,8,12]

def binarySearch(nums, target, start, end):
    if start > end:
        return -1

    mid = int(start + (end-start)/2)

    if target < nums[mid]:
        return binarySearch(nums, target, start, mid-1)

    elif target > nums[mid]:
        return binarySearch(nums, target, mid+1, end)

    else:
        return mid

target = int(input("enter target:"))
idx = binarySearch(nums, target, 0, len(nums)-1)
print(f"{target} is at index {idx}.")