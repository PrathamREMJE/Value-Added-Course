arr = [5,10,15,25,30,35]
pos = 2
for i in range(len(arr)-pos):
    arr[i] = arr[i+pos]
for i in range(len(arr)-1,len(arr)-pos-1,-1):
    arr[i] = 0
print(arr)
