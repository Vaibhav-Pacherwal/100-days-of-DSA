## Next Permutation
def nextPermutation(nums):
    pivot,i = -1,len(nums)-1
    while i > 0:
        if nums[i-1] < nums[i]:
            pivot = i-1
            break
        i -= 1

    if pivot == -1:
        nums.reverse()
        return nums

    j = len(nums)-1
    while j > 0:
        if nums[j] > nums[pivot]:
            temp = nums[j]
            nums[j] = nums[pivot]
            nums[pivot] = temp
            break
        j -= 1

    start,end = pivot+1,len(nums)-1
    while start <= end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1

    return nums

nums = [1,1,5]
ans = nextPermutation(nums)
print(ans)
