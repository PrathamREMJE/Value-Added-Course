nums = [10,20,30,40,50,60]
r = 2
# for i in range(0,r):
#     temp = nums[0]
#     for j in range(0,len(nums)-1):
#         nums[j] = nums[j+1]
#     nums[-1] = temp
# print(nums)
j = 0
temp_arr = []
for i in range(r):
    temp_arr.append(nums[i])
for i in range(0,len(nums)-r,1):
    nums[i] = nums[i+r]
for i in range(len(nums)-r,len(nums),1):
    nums[i] = temp_arr[j]
    j += 1
print(nums)
