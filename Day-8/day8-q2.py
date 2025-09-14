## Lower Bound
nums = [1,3,5,6]

start = 0
end = len(nums)-1

last_mid = -1
x = int(input("enter x:"))
while start <= end:
    mid = int(start + (end-start)/2)

    if nums[mid] >= x:
        start = mid+1
        last_mid = mid

    else:
        end = mid-1

print(last_mid+1)

