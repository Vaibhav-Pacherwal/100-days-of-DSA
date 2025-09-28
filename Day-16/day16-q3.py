def findMedianSortedArrays(nums1, nums2):
    mergedArr = [0]*(len(nums1)+len(nums2))
    i,j,k = 0,0,0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            mergedArr[k] = nums1[i]
            i += 1
            j += 1
            k += 1
        elif nums1[i] < nums2[j]:
            mergedArr[k] = nums1[i]
            i += 1
            k += 1
        else:
            mergedArr[k] = nums2[j]
            j += 1
            k += 1
    
    if i < len(nums1):
        while i < len(nums1):
            mergedArr[k] = nums1[i]
            i += 1
            k += 1
    
    if j < len(nums2):
        while j < len(nums2):
            mergedArr[k] = nums2[j]
            j += 1
            k += 1

    print(mergedArr)
    if len(mergedArr)%2 != 0:
        mid = len(mergedArr)//2
        return mergedArr[mid]
    else:
        mid = len(mergedArr)//2
        median = (mergedArr[mid]+mergedArr[mid-1])/2
        return median
    
nums1 = [1,2]
nums2 = [3,4]
ans = findMedianSortedArrays(nums1,nums2)
print(ans)
