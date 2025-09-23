## 
def shipWithinDays(weights,days):
    ans = 0
    start,end = max(weights),sum(weights)
    while start <= end:
        mid = int(start + (end-start)/2)

        dayCount,currWeigh = 0,0
        for weight in weights:
            if currWeigh + weight > mid:
                dayCount += 1
                currWeigh = 0
            currWeigh += weight
            
        if dayCount <= days:
            ans = mid
            end = mid-1
        else:
            start = mid+1
        
    return ans

weights,days = [3,2,2,4,1,4],3
ans = shipWithinDays(weights,days)
print(ans)




