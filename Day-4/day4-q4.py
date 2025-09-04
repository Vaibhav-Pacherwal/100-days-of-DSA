## Subarray Sum Equals K
nums = [1,2,3]

count = 0
sb_ct = 0
target = int(input("enter nums:"))
for i in range(len(nums)):
    count = 0
    for j in range(i, len(nums)):
        count += nums[j]
        if count == target:
            sb_ct += 1

print(sb_ct)