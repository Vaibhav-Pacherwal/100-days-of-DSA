## majority element using moore's voting algo
nums = [1, 1, 1, 3, 3]

ele = 0
freq = 1
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        ele = nums[i-1]
        freq += 1
    else:
        freq -= 1
        if freq == 0:
            ele = nums[i]

print(f"majority element:{ele}")