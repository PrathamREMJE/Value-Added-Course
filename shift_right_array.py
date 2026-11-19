arr = [5,10,15,25,30,35]
for i in range(len(arr)-1,0,-1):
    arr[i] = arr[i-3]
for i in range(0,3):
    arr[i] = 0
print(arr)