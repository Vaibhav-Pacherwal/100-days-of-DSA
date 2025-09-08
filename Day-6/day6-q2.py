## 4 Sum
## Brute Force
# nums = [4,3,3,4,4,2,1,2,1,1]

# ans = set()
# target = int(input("enter target:"))
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         for k in range(j+1, len(nums)):
#             sum = 0
#             for l in range(k+1, len(nums)):
#                 sum = nums[i]+nums[j]+nums[k]+nums[l]
#                 if sum == target:
#                     subans = [nums[i], nums[j], nums[k], nums[l]]
#                     subans.sort()
#                     ans.add(str(subans))

# ans_list = list(ans)
# for i in range(len(ans_list)):
#     ans_list[i] = eval(ans_list[i])

# print(ans_list)

## Better Approach - using dictionary
# nums = [4,3,3,4,4,2,1,2,1,1]

# ans = set()
# nums_ele = {}
# target = int(input("enter target:"))
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         for k in range(j+1, len(nums)):
#             fourth_ele = target - (nums[i]+nums[j]+nums[k])
#             if fourth_ele in nums_ele:
#                 subans = [nums[i], nums[j], nums[k], fourth_ele]
#                 subans.sort()
#                 ans.add(str(subans))
            
#     nums_ele[nums[i]] = i

# ans_list = list(ans)
# for i in range(len(ans_list)):
#     ans_list[i] = eval(ans_list[i])

# print(ans_list)

## Optimal Approach
nums = [2,2,2,2,2]
nums.sort()

ans = []
target = int(input("enter target:"))
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
            continue
    
    for j in range(i+1, len(nums)):
        if j > i+1 and nums[j] == nums[j-1]:
            continue

        p = j+1
        q = len(nums)-1

        while p < q:
            sum = nums[i]+nums[j]+nums[p]+nums[q]
            if target == sum:
                subans = [nums[i], nums[j], nums[p], nums[q]]
                ans.append(subans)
                p += 1
                q -= 1
                while p < q and nums[p] == nums[p-1]:
                    p += 1
                while p < q and nums[q] == nums[q+1]:
                    q -= 1
            else:
                if sum < target:
                    p += 1
                else:
                    q -= 1

print(ans)

