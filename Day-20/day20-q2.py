## Median of Row Wise Sorted Matrix
nums = [[1,4,7],[2,5,8],[3,6,9]]

flattenMat = []
for i in range(len(nums)):
    for j in range(len(nums[0])):
        flattenMat.append(nums[i][j])

flattenMat.sort()
print(flattenMat)
mid = int(len(flattenMat)/2)
if mid % 2 != 0:
    print(flattenMat[mid])
else:
    median = int((flattenMat[mid]+flattenMat[mid-1])/2 + 1)
    print(median)