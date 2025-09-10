## Merge Overlapping Sub-intervals
nums = [[1,4],[0,2],[3,5]]
nums.sort()

ans = []
if len(nums) == 1:
    ans.append(nums[0])
    print(ans)
else:
    interval1 = nums[0]
    for i in range(1, len(nums)):
        interval2 = nums[i]
        if interval1[1] >= interval2[0]:
            subans = [interval1[0],interval2[1]]
            interval1 = subans
            ans.append(subans)
        else:
            ans.append(interval2)
            interval1 = interval2

    print(ans)