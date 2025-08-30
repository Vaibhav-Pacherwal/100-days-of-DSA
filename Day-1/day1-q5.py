## Linear Search
def linearSearch(nums, target):
    for i in range(0, len(nums)):
        if nums[i] == target:
            return i
    
    return -1

nums = [1, 2, 3, 5, 6, 7]
target = int(input("enter target:"))
idx = linearSearch(nums, target)
if idx != -1:
    print(f"{target} is present at index {idx}")
else:
    print(f"{target} is not in this list")