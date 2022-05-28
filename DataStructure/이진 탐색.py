# import bisect
#
#
# def binary_search1(target, data):
#     data.sort()
#     left = 0
#     right = len(data) - 1
#
#     while left <= right :
#         mid = (left + right) // 2
#
#         if data[mid] == target:
#             return mid
#         elif data[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return None
#
# # 재귀적 구현
# def binary_search2(target, data, left, right):
#     data.sort()
#     if left > right:
#         return None
#
#     mid = (left + right) // 2
#     if data[mid] == target:
#         return mid
#     elif data[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
#
#     return binary_search2(target, data, left, right)
#
#
# # 내장 라이브러리 사용
# def binary_search3(target, data):
#     data.sort()
#     idx = bisect.bisect_left(data, target)
#     if idx < len(data) and data[idx] == target:
#         return idx
#     else:
#         return None
#
#
# target = 25
# data = [31, 25, 7, 81, 70, 11, 43, 56, 19, 63, 21, 98]
# right = len(data) - 1
# print(binary_search1(target, data))
# print(binary_search2(target, data, 0, right))
# print(binary_search3(target, data))



# 부품 찾기
n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

def binary_search(n_arr, target):
    n_arr.sort()

    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if n_arr[mid] == target:
            return mid
        elif n_arr[mid] < target:
            left = mid + 1
        elif:
            right = mid - 1
    return None

for e in m_arr:
    result = binary_search(n_arr, e)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

