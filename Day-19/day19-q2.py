## Selection Sort
def selectionSort(nums):
    for i in range(len(nums)):
        smallest = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j

        if smallest != i:
            temp = nums[i]
            nums[i] = nums[smallest]
            nums[smallest] = temp
        
nums = [4,1,5,2,3,0,2]
selectionSort(nums)
print(nums)