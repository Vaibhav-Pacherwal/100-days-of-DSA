## Kadane's Algorithm : Maximum Subarray Sum in an Array
nums = [-2,1,-3,4,-1,2,1,-5,4]

currSum = 0
maxSum = float("-inf")
for i in range(0, len(nums)):
    currSum += nums[i]
    maxSum = max(currSum, maxSum)
    if currSum < 0:
        currSum = 0

print(f"maximum subarray sum:{maxSum}")     