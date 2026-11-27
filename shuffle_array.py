def shuffleArray(arr: List[int], n: int) -> List[int]:
    temp_arr = []
    for i in range(n):
        temp_arr.append(arr[i])
        temp_arr.append(arr[i+n])
    for i in range(2*n):
        arr[i] = temp_arr[i]
    return arr