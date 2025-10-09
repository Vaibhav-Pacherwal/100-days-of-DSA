## Subset-II
def subsetsWithDup(arr,subSets,ans,i):
    if i == len(arr):
        subSets.append(ans[:])
        return
    
    ans.append(arr[i])
    subsetsWithDup(arr,subSets,ans,i+1)

    ans.pop()
    subsetsWithDup(arr,subSets,ans,i+1)

arr,subSets,ans = [0],[],[]
subsetsWithDup(arr,subSets,ans,0)
subSetCollection = set()
for subset in subSets:
    subSetCollection.add(tuple(subset))

subSetList = list(subSetCollection)
for i in range(len(subSetList)):
    subSetList[i] = list(subSetList[i])

print(subSetList)