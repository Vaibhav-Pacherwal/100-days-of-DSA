## Bubble Sort
def bubbleSort(nums):
    l = 0
    isSwap = False
    while l < len(nums):
        i,j = 0,1
        while j < len(nums):
            if nums[i] > nums[j]:
                isSwap = True
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            
            i += 1
            j += 1
        
        if not isSwap:
            return
        
        l += 1


nums = [4,1,5,2,3,0,2]
bubbleSort(nums)
print(nums)
