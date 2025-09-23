## Kth Missing Positive Number
arr,k = [1,2,3,4],2

def main(arr,k):
    i,j = 1,0
    count,ans = 0,0
    while j < len(arr):
        if i == arr[j]:
            j += 1
            i += 1
        else:
            count += 1
            if count == k:
                return i
            i += 1

    while count != k:
        count += 1
        ans = i
        i += 1
    
    return ans

ans = main(arr,k)
print(ans)        

