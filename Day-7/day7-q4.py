## Count Inversion
nums = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        temp = nums[i][j]
        nums[i][j] = nums[j][i]
        nums[j][i] = temp

for row in nums:
    row = row.reverse()

print(nums)