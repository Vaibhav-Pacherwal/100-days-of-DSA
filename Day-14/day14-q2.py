## Find the Smallest Divisor Given a Threshold
nums, threshold = [21212,10101,12121], 1000000

ans = 0
start,end = 1,max(nums)
while start <= end:
    mid = int(start + (end-start)/2)

    sum = 0
    for num in nums:
        if num % mid == 0:
            sum += num // mid
        else:
            sum += (num // mid) + 1
    
    if sum <= threshold:
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)