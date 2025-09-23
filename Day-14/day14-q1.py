## Minimum Number of Days to Make m Bouquets
def minDays(bloomDay,m,k):
    ans = float("inf")
    start,end = min(bloomDay),max(bloomDay)
    while start <= end:
        dCount,bCount = 0,0
        for day in bloomDay:
            if day <= start:
                dCount += 1
                if dCount == k:
                    bCount += 1
                    if bCount == m:
                        ans = min(start,ans)
            else:
                dCount = 0
        
        start += 1
    
    return ans


bloomDay,m,k = [7,7,7,7,12,7,7],2,3
ans = minDays(bloomDay,m,k)
print(ans)

