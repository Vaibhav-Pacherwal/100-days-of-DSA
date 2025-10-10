## Permutations using recursion
def getPerms(arr,totalPerms,i):
    if i > totalPerms:
        return

    for val in arr:
        print(val, end=" ")
    print()

    pivot = -1
    for j in range(len(arr)-1,0,-1):
        if arr[j-1] < arr[j]:
            pivot = j-1
            break

    if pivot == -1:
        return
    
    for k in range(len(arr)-1,-1,-1):
        if arr[k] > arr[pivot]:
            temp = arr[k]
            arr[k] = arr[pivot]
            arr[pivot] = temp
            break

    start,end = pivot+1,len(arr)-1
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

    getPerms(arr,totalPerms,i+1)

arr = [1,2,3]
totalPerms = 1
for i in range(1,len(arr)+1):
    totalPerms *= i

getPerms(arr,totalPerms,1)
