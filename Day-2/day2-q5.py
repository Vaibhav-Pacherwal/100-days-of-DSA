## Pair Sum.
nums = [2,7,4,6,2,6,0,0,12]

target = int(input("enter target:"))

ele_pos = {}
for i in range(0, len(nums)):
    ele = target-nums[i]
    if ele in ele_pos:
        print(f"{ele_pos[ele],i}")
    else:
        ele_pos[nums[i]] = i

