## majority element using moore's voting algo
nums = [1, 1, 1, 3, 3]

ele = nums[0]
count = 1
for i in range(1, len(nums)):
    if nums[i] == ele:
        count += 1
    else:
        count -= 1
        if count < 0:
            count = 0
            ele = nums[i]
    
print(f"majority element:{ele}")