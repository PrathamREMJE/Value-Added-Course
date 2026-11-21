arr = [10,20,10,30,10,40,10,10]
X = 10
j = 0
for i in range(0,len(arr)):
    if arr[i] != X:
        arr[j] = arr[i]
        j += 1
for i in range(j,len(arr)):
    arr[i] = 0
print(arr)