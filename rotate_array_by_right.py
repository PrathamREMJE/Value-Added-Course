n = len(arr)
r = r % n
if r == 0:
    print(arr)
temp_arr = arr[n-r:]
rem_arr = arr[:n-r]
print(temp_arr + rem_arr)