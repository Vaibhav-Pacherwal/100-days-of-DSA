## Peak index in mountain array
nums = [1,2]

if len(nums) == 0:
    print(0)
elif len(nums) == 1:
    if nums[0] >= nums[1]:
        print(0)
    else:
        print(1)
else:
    start,end = 0,len(nums)-1
    while start <= end:
        mid = int(start + (end-start)/2)

        if (mid == 0 or nums[mid] > nums[mid-1]) \
            and (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
            print(mid)
            break

        elif nums[mid-1] > nums[mid]:
            end = mid-1

        else:
            start = mid+1




