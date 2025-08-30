## remove duplicate from list
nums = [0,0,1,1,1,2,2,3,3,4]

j = 0
for i in range(0, len(nums)):
    if nums[i] != nums[j]:
        nums[j+1] = nums[i]
        j += 1

print(nums, j+1)