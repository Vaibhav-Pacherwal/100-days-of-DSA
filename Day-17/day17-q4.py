## Median of Two Sorted Arrays
def median(nums):
    mid = int(len(nums)/2)
    if len(nums) % 2 != 0:
        return nums[mid]
    else:
        median = (nums[mid]+nums[mid-1])/2
        return median
    
def mergeArrays(nums1,nums2):
    mergedArr = [0]*(len(nums1)+len(nums2))

    i,j,k = 0,0,0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            mergedArr[k] = nums1[i]
            i += 1
            k += 1
            print(mergedArr,i)
        elif nums1[i] > nums2[j]:
            mergedArr[k] = nums2[j]
            k += 1
            j += 1
        else:
            mergedArr[k] = nums1[i]
            k += 1
            i += 1
            j += 1

    if i < len(nums1):
        while i < len(nums1):
            mergedArr[k] = nums1[i]
            k += 1
            i += 1
    
    if j < len(nums2):
        while j < len(nums2):
            mergedArr[k] = nums2[j]
            k += 1
            j += 1
    
    print(mergedArr)
    ans = median(mergedArr)
    return ans

nums1,nums2 = [1,2],[3,4]
ans = mergeArrays(nums1,nums2)
print(ans)
