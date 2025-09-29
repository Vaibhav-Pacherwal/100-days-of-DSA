## Insertion Sort
def insertionSort(nums):
    for i in range(1,len(nums)):
        prev = i-1
        for j in range(i,len(nums)):
            curr = nums[j]
            if nums[prev] > nums[j]:
                nums[j] = nums[prev]
                nums[prev] = curr

nums = [4,1,5,2,3,0,2]
insertionSort(nums)
print(nums)
