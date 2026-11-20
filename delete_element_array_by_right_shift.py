arr = [5,10,15,25,30,35]
pos = 2
for i in range(0,pos):
    arr[i] = arr[i+1]
for i in range(0,pos):
    arr[i] = 0
print(arr)
