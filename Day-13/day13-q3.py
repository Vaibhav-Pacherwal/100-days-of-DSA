## koko eating bananas

# Brute Force
def koko(nums,h):
    for i in range(1, max(nums)+1):
        time = 0
        for pile in nums:
            if pile % i == 0:
                time += pile // i
            else:
                time += (pile // i) + 1

        if time <= h:
            return i



nums,h = [3,6,7,11],8
sol = koko(nums,h)
print(sol)

# using binary search
def koko(nums,h):
    start,end = 1,max(nums)
    ans = float("inf")
    while start <= end:
        mid = int(start + (end-start)/2)

        time = 0
        for pile in nums:
            if pile % mid == 0:
                time += pile // mid
            else:
                time += (pile // mid)+1
        
        if time == h:
            ans = mid
            end = mid-1

        else:
            start = mid+1
    
    return ans

nums,h = [3,6,7,11],8
sol = koko(nums,h)
print(sol)