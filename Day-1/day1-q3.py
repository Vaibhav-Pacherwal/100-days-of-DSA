## Left Rotate an array by one place
def reverse(lst, start, end):
    while start < end:
        temp = lst[start]
        lst[start] = lst[end]
        lst[end] = temp
        start += 1
        end -= 1

nums = [3]
reverse(nums, 0, len(nums)-1)
reverse(nums, 0, len(nums)-2)
print(nums)
