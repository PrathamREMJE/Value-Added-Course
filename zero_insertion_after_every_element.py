arr = [10,20,30,40,50,60]
ans_list = []
j = 0
for i in range(0,len(arr)):
    if i % 2 != 0:
        ans_list.append(0)
    else:
        ans_list.append(arr[j])
        j += 1
print(ans_list)