## Sort an array of 0s, 1s and 2s.
nums = [2,0,2,1,1,0]

i = 0
for j in range(i, len(nums)):
    if nums[j] == 0:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1

for k in range(i, len(nums)):
    if nums[k] == 1:
        temp = nums[i]
        nums[i] = nums[k]
        nums[k] = temp
        i += 1

print(nums)