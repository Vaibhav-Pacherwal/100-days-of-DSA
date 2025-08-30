## Check if array is sorted or not.
nums = [1, 2, 3, 4, 5, 0, 6, 1]

count = 0
n = len(nums)
for i in range(0, len(nums)):
    if nums[i] > nums[(i+1) % n]:
        count += 1

if count <= 1:
    print("sorted!")
else:
    print("not sorted!")
