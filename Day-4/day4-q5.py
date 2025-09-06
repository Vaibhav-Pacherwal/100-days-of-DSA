## product of array except self
nums = [1,2,3,4]

i = 0
product = []
while i < len(nums):
    ans = 1
    j = i-1
    while j >= 0:
        ans *= nums[j]
        j -= 1

    k = i+1
    while k < len(nums):
        ans *= nums[k]
        k += 1
    
    product.append(ans)
    i += 1

print(nums)
print(product)

## optimal approach
prefix = []
pre_prod = 1
for i in range(0, len(nums)):
    prefix.append(pre_prod)
    pre_prod *= nums[i]

suffix = [0]*len(nums)
suff_prod = 1
for i in range(len(nums)-1, -1, -1):
    suffix[i] = suff_prod
    suff_prod *= nums[i]

ans = []
for i in range(0, len(nums)):
    ans.append(suffix[i]*prefix[i])

print(ans)

