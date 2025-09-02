## Rearrange the array in alternating positive and negative items
nums = [1,2,-4,-5]

pos = 0
neg = 1
new_nums = [0]*len(nums)
for i in range(0, len(nums)):
    if nums[i] < 0:
        new_nums[neg] = nums[i]
        neg += 2
    else:
        new_nums[pos] = nums[i]
        pos += 2

print(nums)
print(new_nums)
