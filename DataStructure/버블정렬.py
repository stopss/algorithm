# 버블 정렬
# 인접한 원소들 간에 대소 비교를 통한 정렬

# 버블 정렬 - 오름 차순
def bubbleSort_ASC(arr):
    # 배열의 크기만큼 반복
    for i in range(len(arr)-1, 0, -1):
        swapped = False
        # 배열의 크기에서 i의 값과
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# 버블 정렬 - 내림 차순
def bubbleSort_DESC(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr



arr = [1, 6, 5, 2, 4, 3]
result_asc = [1, 2, 3, 4, 5, 6]
result_desc = [6, 5, 4, 3, 2, 1]
assert bubbleSort_ASC(arr) == result_asc
assert bubbleSort_DESC(arr) == result_desc