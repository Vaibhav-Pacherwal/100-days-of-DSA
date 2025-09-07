## Majority Elements(>n/3)
nums = [1,2]

freq = {}
for i in range(len(nums)):
    freq[nums[i]] = freq.get(nums[i], 0) + 1

ans = []
elements = set(nums)
edge = len(nums)/3
for element in elements:
    if freq[element] > edge:
        ans.append(element)

print(ans)