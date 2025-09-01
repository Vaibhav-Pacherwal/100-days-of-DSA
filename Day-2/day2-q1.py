## Count Maximum Consecutive One's in the array
nums = [1,1,0,1,1,1]

count = 0
max_count = 0
for i in range(0, len(nums)):
    if nums[i] == 1:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0

if count != 0:
    max_count = max(max_count, count)


print(f"Maximum consecutive 1's are {max_count}")