## Insertion in sorted array
nums = [1, 2, 4, 6, 7]

x = int(input("enter x:"))

if len(nums) == 0:
    print(f"{x} can be inserted at index {0}")

else:
    start = 0
    default = -1
    end = len(nums)-1
    while start <= end:
        mid = int(start + (end-start)/2)

        if x > nums[mid]:
            default = mid
            start = mid+1

        elif x < nums[mid]:
            default = mid
            end = mid-1

        else:
            default = mid
            if nums[default-1] == x:
                end = mid-1
            else:
                break

    if default == 0:
        if nums[default] < x:
            print(f"{x} can be inserted at index {default+1}")
        else:
            print(f"{x} can be inserted at index {default}")

    elif default == len(nums)-1:
        if nums[default] < x:
            print(f"{x} can be inserted at index {default+1}")
        else:
            print(f"{x} can be inserted at index {default}")

    else:
        if nums[default] < x:
            print(f"{x} can be inserted at index {default+1}")
        else:
            print(f"{x} can be inserted at index {default}")