## Find the union
nums1 = [1, 2, 3, 4, 5]
nums2 = [3, 4, 5, 6, 7]

nums_set1 = set(nums1)
nums_set2 = set(nums2)
new_set = nums_set1.union(nums_set2)
new_nums_lst = list(new_set)
print(new_nums_lst)