arr = [5,10,15,25,30,35]
pos = 2
for i in range(pos,0,-1):
    arr[i] = arr[i-1]
arr[0] = 0
print(arr)
