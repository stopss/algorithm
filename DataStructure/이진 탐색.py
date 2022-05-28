import bisect


def binary_search1(target, data):
    data.sort()
    left = 0
    right = len(data) - 1

    while left <= right :
        mid = (left + right) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

# 재귀적 구현
def binary_search2(target, data, start, end):
    data.sort()
    if start > end:
        return None

    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

    return binary_search2(target, data, start, end)


# 내장 라이브러리 사용
def binary_search3(target, data):
    data.sort()
    idx = bisect.bisect_left(data, target)
    if idx < len(data) and data[idx] == target:
        return idx
    else:
        return None


target = 25
data = [31, 25, 7, 81, 70, 11, 43, 56, 19, 63, 21, 98]
end = len(data) - 1
# print(data.sort())
print(binary_search1(target, data))
print(binary_search2(target, data, 0, end))
print(binary_search3(target, data))

