## Increasing Triplet Subsequence

## my intutive approach - passed 77/86 test cases.
def inctriplet(nums):
    for i in range(0, len(nums)):
        j = i+1
        k = len(nums)-1
        while j <= k:
            if nums[i] < nums[j] < nums[k]:
                return True
            
            if nums[k] < nums[j] and nums[k] > nums[i]:
                j += 1
            else:
                k -= 1

    return False

nums = [1,5,0,4,1,3]
print(inctriplet(nums))

## Optimal Approach
def incTriplet(nums):
    first = float("inf")
    second = float("inf")
    
    for x in nums:
        if x <= first:
            first = x
        elif x <= second:
            second = x
        else:
            return True
        
    return False

nums = [1,5,0,4,1,3]
print(incTriplet(nums))
