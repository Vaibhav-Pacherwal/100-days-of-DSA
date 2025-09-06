## Count Subarray sum Equals K
nums = [1,2,3]

count = 0
target = int(input("enter target:"))
for i in range(len(nums)):
    sum = 0
    for j in range(i, len(nums)):
        sum += j

    if sum == target:
        count += 1

print(count)

