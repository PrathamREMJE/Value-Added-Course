nums = [10,20,30,40,50,60]
r = 2
for i in range(0,r):
    temp = nums[0]
    for j in range(0,len(nums)-1):
        nums[j] = nums[j+1]
    nums[-1] = temp
print(nums)
