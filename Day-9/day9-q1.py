## Find First and Last Position of Element in Sorted Array
nums = [1]

x = int(input("enter x:"))

def findBound(isFirst):
    start, end = 0, len(nums)-1
    idx = -1

    while start <= end:
        mid = int(start + (end-start)/2)

        if nums[mid] < x:
            start = mid+1
        
        elif nums[mid] > x:
            end = mid-1

        else:
            idx = mid
            if isFirst:
                end = mid-1
            else:
                start = mid+1

    return idx

first = findBound(True)
last = findBound(False)

print(first, last)