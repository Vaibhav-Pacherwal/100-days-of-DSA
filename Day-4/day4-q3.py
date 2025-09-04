## Longest Subarray with given Sum K
nums = [2,3,5,1,9]

max_len = 0
max_sum = 0
target = int(input("enter target:"))
for i in range(len(nums)):
    for j in range(i, len(nums)):
        sum = 0
        count = 0
        for k in range(i, j+1):
            count += 1
            sum += nums[k]
        if sum == target:
            if count > max_len:
                max_len = count
        
print(max_len)