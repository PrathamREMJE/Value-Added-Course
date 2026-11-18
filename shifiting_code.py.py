arr = [5,10,15,25,30,35]
# for i in range(len(arr)-1,0,-1):
#     arr[i] = arr[i-3]
# for i in range(0,3):
#     arr[i] = 0
# print(arr)

# pos = 2
# for i in range(len(arr)-pos):
#     arr[i] = arr[i+pos]
# for i in range(len(arr)-1,len(arr)-pos-1,-1):
#     arr[i] = 0
# print(arr)

# pos = 3
# for i in range(len(arr)-1,len(arr)-pos-1,-1):
#     arr[i] = 0
# print(arr)

pos = 2
arr1 = [5,10,20,25]
temp = arr[pos]
arr1[pos] = 15  
for i in range(pos+1,len(arr1)):  
    arr1[i] = temp
    temp = arr1[i+1]
print(arr1)
