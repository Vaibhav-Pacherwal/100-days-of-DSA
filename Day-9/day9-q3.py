## Count Occurrences in Sorted Array
nums = [1, 1, 2, 2, 2, 2, 2, 3]

x = int(input("enter x:"))

def countOcc(ste):
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
            if ste:
                end = mid-1
            else:
                start = mid+1

    return idx

first = countOcc(True)
last = countOcc(False)

print(f"{x} occurs {last-first+1} times!")
