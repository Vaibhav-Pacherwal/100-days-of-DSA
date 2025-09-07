## 3 Sum

## Brute Force
nums = [-2,0,1,1,2]

ans = set()
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i]+nums[j]+nums[k] == 0:
                subans = []
                subans.append(nums[i])
                subans.append(nums[j])
                subans.append(nums[k])
                subans.sort()
                ans.add(str(subans))

ans_list = list(ans)
print(ans_list)
for i in range(len(ans_list)):
    ans_list[i] = eval(ans_list[i])

print(ans_list)

## Better Approach
nums = [0,0,0]

ans = set()
track = {}
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        third_ele = -1 * (nums[i]+nums[j])
        if third_ele in track:
            subans = []
            subans.append(nums[i])
            subans.append(nums[j])
            subans.append(third_ele)
            subans.sort()
            ans.add(str(subans))

    track[nums[i]] = track.get(nums[i], 0) + 1

ans_list = list(ans)
for i in range(len(ans_list)):
    ans_list[i] = eval(ans_list[i])

print(ans_list)

## Optimal Approach - Two Pointers
nums = [-1,0,1,2,-1,-4]

ans = []
nums.sort()
for i in range(len(nums)):
    j = i+1
    k = len(nums)-1

    if i > 0 and nums[i] == nums[i-1]:
        continue

    while j < k:
        sum = nums[i]+nums[j]+nums[k]
        if sum == 0:
            subans = [nums[i], nums[j], nums[k]]
            ans.append(subans)
            j += 1
            k -= 1
            while j < k and nums[j] == nums[j-1]:
                j += 1
            while j < k and nums[k] == nums[k + 1]:
                k -= 1
        else:
            if sum > 0:
                k -= 1
            else:
                j += 1

print(ans)