## Move Zeros to end
nums = [0,1,0,3,12]

k = 0
for i in range(0, len(nums)):
    if nums[i] != 0:
        temp = nums[i]
        nums[i] = nums[k]
        nums[k] = temp
        k += 1

print(nums)