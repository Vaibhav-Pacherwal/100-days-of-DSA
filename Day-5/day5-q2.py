## longest consecutive subsequence
nums = [0,3,7,2,5,8,4,6,0,1]

backup = set(nums)
longest_seq = 0
for num in backup:
    if num - 1 is not backup:
        length = 1
        while num + length in backup:
            length += 1
        longest_seq = max(longest_seq, length)

print(longest_seq)