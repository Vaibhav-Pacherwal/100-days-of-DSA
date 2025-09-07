## Subarray sum equals K

# Brute Force
nums = [9,4,20,3,10,5]

count = 0
target = int(input("enter target:"))
for i in range(0, len(nums)):
    sum = 0
    for j in range(i, len(nums)):
            sum += nums[j]
            if sum == target:
                count += 1

print(count)

# Optimal - using dictionary
nums = [1,2,3]

sum = 0
prefixSum = []
for i in range(len(nums)):
    sum += nums[i]
    prefixSum.append(sum)

n_count = 0
pre_count = {}
for i in range(len(nums)):
    if prefixSum[i] == target:
        n_count += 1
        
    curr_ele = prefixSum[i] - target
    if curr_ele in pre_count:
        n_count += pre_count.get(curr_ele)
    
    pre_count[prefixSum[i]] = pre_count.get(prefixSum[i], 0) + 1

print(n_count)


