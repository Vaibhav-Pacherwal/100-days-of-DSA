## Merge Sorted Array
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]

# m = 3
# n = len(nums2)
# merged_arr = []
# i = 0
# j = 0
# while i < m and j < n:
#     if nums1[i] == nums2[j]:
#         merged_arr.append(nums1[i])
#         i += 1
#         merged_arr.append(nums2[j])
#         j += 1
#     elif nums1[i] < nums2[j]:
#         merged_arr.append(nums1[i])
#         i += 1
#     else:
#         merged_arr.append(nums2[j])
#         j += 1

# if i < m:
#     while i < m:
#         merged_arr.append(nums1[i])
#         i += 1

# if j < n:
#     while j < n:
#         merged_arr.append(nums2[j])
#         j += 1

# print(merged_arr)

## Optimal Approach
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3

p = m-1
q = n-1
r = m+n-1
while p >= 0 and q >= 0 and r != -1:
    if nums2[q] == nums1[p]:
        temp = nums1[r]
        nums1[r] = nums1[p]
        nums1[p] = temp
        p -= 1
        r -= 1
        temp = nums1[r]
        nums1[r] = nums2[q]
        nums2[q] = temp
        q -= 1
        r -= 1
    elif nums2[q] > nums1[p]:
        temp = nums1[r]
        nums1[r] = nums2[q]
        nums2[q] = temp
        q -= 1
        r -= 1
    else:
        temp = nums1[r]
        nums1[r] = nums1[p]
        nums1[p] = temp
        p -= 1
        r -= 1

if r != -1 and q >= 0:
    while r != -1 and q >= 0:
        temp = nums1[r]
        nums1[r] = nums2[q]
        nums2[q] = temp
        q -= 1
        r -= 1
    
        
print(nums1)

