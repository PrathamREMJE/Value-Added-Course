nums = [2,3,3,2]
val = 3
k = 0
for i in range(0,len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1
print(k)

