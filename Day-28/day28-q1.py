## Combination Sum - I
def combinationSum(nums,target,ans):
    track,currSum,subSeq,trackVal = {},0,[],0
    for num in nums:
        if num == target:
            ans.append([num])
            continue

        if target % num == 0:
            occ = target // num
            ans.append([num]*occ)
            continue
        else:
            occ = target // num
            subSeq.append([num]*occ)
            currSum += occ
            if currSum + num < target:
                subSeq.append(num)
                currSum += num
                valTBS = target - currSum
                found = track.get(valTBS,-1)
                if found != -1:
                    currSum += valTBS
                    subSeq.append(valTBS)
                if currSum == target:
                    ans.append(subSeq[:])
                    currSum = 0
                    subSeq = []

            track[num] = trackVal
            trackVal += 1

arr,ans = [2,3,5],[]
target = int(input("enter target:"))
combinationSum(arr,target,ans)
print(ans)