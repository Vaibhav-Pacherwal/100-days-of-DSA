## Reverse Pair

## Brute Force
# nums = [-2, -1, 0, 1, 2]

# count = 0
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] > 2*nums[j]:
#             print(f"({nums[i]},{nums[j]})")
#             count += 1

# print(count)

## Better Approach
nums = [1, 3, 2, 3, 1]

count = 0
freq = {}
for i in range(len(nums)):
    check_val = 2*nums[i]
    existence = sum(1 for val in freq.values() if val > check_val)
    count += existence
    freq[i] = nums[i]

print(count)
    
