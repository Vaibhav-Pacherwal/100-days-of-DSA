## Print all subsets
def printSubsets(arr,i,ans,subSets):
    if i == len(arr):
        subSets.append(ans[:])
        return
    
    ans.append(arr[i])
    printSubsets(arr,i+1,ans,subSets)

    ans.pop()
    printSubsets(arr,i+1,ans,subSets)

arr,ans,subSet = [1,2,3],[],[]
printSubsets(arr,0,ans,subSet)
print(subSet)