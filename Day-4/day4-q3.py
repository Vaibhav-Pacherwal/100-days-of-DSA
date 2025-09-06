## Longest Subarray with given Sum K
nums = [2,3,5,1,9]


target = int(input("enter target:"))
# for i in range(len(nums)):
#     for j in range(i, len(nums)):
#         sum = 0
#         count = 0
#         for k in range(i, j+1):
#             count += 1
#             sum += nums[k]
#         if sum == target:
#             if count > max_len:
#                 max_len = count
        
# print(max_len)

## Better Approach
sum = 0
max_len = 0
prefix_sum = {}
for i in range(len(nums)):
    sum += nums[i]
    if sum == target:
        max_len = max(max_len, i+1)
    if prefix_sum.get(target-sum, 0) == 0:
        prefix_sum[sum] = i
    else:
        max_len = max(i-prefix_sum.get(target-sum, 0), max_len)

print(max_len)    

    