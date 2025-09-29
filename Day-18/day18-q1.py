## Find the row with maximum number of 1's
def countOcc(row,searchLeft):
    row.sort()
    count = 0
    start,end = 0,len(row)-1
    while start <= end:
        mid = int(start + (end-start)/2)
        
        if row[mid] < 1:
            start = mid+1
        
        elif row[mid] > 1:
            end = mid-1

        else:
            count += 1
            if searchLeft:
                end = mid-1
            else:
                start = mid+1
    
    return count

nums = [
    [1, 0, 1, 1]
]
row,count = -1,0
for i in range(len(nums)):
    currCount = countOcc(nums[i],True) + countOcc(nums[i],False) - 1
    print(currCount)
    if currCount > count:
        row = i
        count = currCount

if row == -1:
    print("No row is having '1'")
else:
    print(f"row {row} have {count} 1's")
