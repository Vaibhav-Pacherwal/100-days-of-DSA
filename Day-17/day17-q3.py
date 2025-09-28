## Minimum Number of Days to Make m Bouquets
bloomDay,m,k = [7,7,7,7,12,7,7],2,3

def isPossible(bloomDay,m,k,mid):
    currDay,flowerCount = 0,0
    for day in bloomDay:
        if day <= mid:
            flowerCount += 1
        else:
            flowerCount = 0

        if flowerCount >= k:
            currDay += 1
            if flowerCount == k:
                flowerCount = 0
            flowerCount = 1
         
        if currDay == m:
            return True
        
    return False


def minDays(bloomDay,m,k):
    if len(bloomDay) < m*k:
        return -1
    
    start,end = min(bloomDay),max(bloomDay)
    ans = -1
    while start <= end:
        mid = int(start + (end-start)/2)

        if isPossible(bloomDay,m,k,mid):
            ans = mid
            end = mid-1
        else:
            start = mid+1

    return ans

ans = minDays(bloomDay,m,k)
print(ans)