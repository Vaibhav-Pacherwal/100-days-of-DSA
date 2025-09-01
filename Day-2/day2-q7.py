## stock buy and sell.
nums = [7,1,5,3,6,4]

maxProfit = 0
bestBuy = nums[0]
for i in range(1, len(nums)):
    if nums[i] > bestBuy:
        maxProfit = max(maxProfit, nums[i]-bestBuy)
    bestBuy = min(bestBuy, nums[i])

print(f"maximum profit:{maxProfit}")