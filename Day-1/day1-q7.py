## Find the missing number in an array
nums = [1,2,4,5,0]

def missingVal(nums):
    for i in range(0, len(nums)):
        if nums[i] != i+1:
            return i+1
        
    return -1

missingIdx = missingVal(nums)
print(f"{missingIdx} is missing!")