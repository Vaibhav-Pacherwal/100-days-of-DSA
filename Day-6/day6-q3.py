## Longest subarray with sum 0
nums = [15, -2, 2, -8, 1, 7, 10, 23]

sum = 0
prefixSum = []
for i in range(len(nums)):
    sum += nums[i]
    prefixSum.append(sum)

max_len = 0
track = {}
for i in range(len(prefixSum)):
    if prefixSum[i] == 0:
        i += 1

    if prefixSum[i] in track:
        max_len = max(i-track.get(prefixSum[i]), max_len)

    if prefixSum[i] not in track:
        track[prefixSum[i]] = i

print(max_len)