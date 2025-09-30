## Largest Odd Number in String
def largestOddNumber(nums):
    i = len(nums)-1
    while i >= 0:
        if int(nums[i])%2 != 0:
            return nums[:i+1]
        i -= 1
    
    return ""

num = "35427"
ans = largestOddNumber(num)
print(ans)