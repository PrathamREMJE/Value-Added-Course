arr = [1,0,2,3,0,4,5,0]
for i in range(0,len(arr)):
    if arr[i] == 0:
        arr.insert(i,0)
        arr.pop()
print(arr)

arr = [1,0,2,3,0,4,5,0]
i = 0
while i < len(arr)-1:
    if arr[i] == 0:
        for j in range(len(arr)-1,i+1,-1):
            arr[j] = arr[j-1]
            if i + 1 < len(arr):
                arr[i+1] = 0
            i += 1      
        i += 1


print(arr)