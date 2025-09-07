## Maximum Product Subarray
nums = [-3,1,0,-2]

pre_prod = 1
prefixProd = []
for i in range(len(nums)):
    pre_prod *= nums[i]
    prefixProd.append(pre_prod)
    if nums[i] == 0:
        pre_prod = 1

suff_prod = 1
suffixProd = [0]*len(nums)
for i in range(len(nums)-1, -1, -1):
    suff_prod *= nums[i]
    suffixProd[i] = suff_prod
    if nums[i] == 0:
        suff_prod = 1

ans1 = max(prefixProd)
ans2 = max(suffixProd)
print(max(ans1, ans2))