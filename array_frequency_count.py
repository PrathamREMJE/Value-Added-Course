arr = [100,101,100,100,102,101,100]
freq = [0] * 4

for i in arr:
    freq[i-100] += 1
    
print(freq)

for i in range(0,len(freq)):
    print([i+100], "occurs", freq[i], "times")


indices_arr = [-4,-2,-1,0,-2,1,3,-4]

freq = [0] * 5

for i in indices_arr:
    pass

# freq = {}
# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# print(freq)