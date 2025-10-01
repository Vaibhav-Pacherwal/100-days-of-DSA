## Find Triangular Sum of an Array
def triangularSum(nums):
    if len(nums) == 1:
        return nums[0]

    i = 0
    while i < len(nums)-1:
        sum = nums[i]+nums[i+1]
        if sum >= 10:
            sum %= 10
        nums[i] = sum
        i += 1

    nums = nums[:i]
    print(nums)
    return triangularSum(nums)

nums = [1,2,3,4,5]
ans = triangularSum(nums)
print(ans)