## Count the number of subarrays with given xor K

nums = [5, 6, 7, 8, 9]

count = 0
for i in range(len(nums)):
    xor = 0
    for j in range(i, len(nums)):
        xor ^= nums[j]
        if xor == 5:
            count += 1

print(count)