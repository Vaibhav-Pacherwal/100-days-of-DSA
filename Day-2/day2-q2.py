## Find the number that appears once, and the other numbers twice.
nums = [4,1,2,1,2]

min_occ = 0
for i in range(0, len(nums)):
    min_occ = min_occ ^ nums[i]

print(f"{min_occ} occurs only once!")