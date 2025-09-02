## 2 Sum
nums = [2,6,5,8,11]

target = int(input("enter target:"))
nums_track = {}
for i in range(0, len(nums)):
    sec_ele = target - nums[i]
    if sec_ele in nums_track:
        print(f"{nums_track.get(sec_ele),i}")
        break
    else:
        nums_track[nums[i]] = i


