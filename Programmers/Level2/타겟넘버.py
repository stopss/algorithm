from collections import deque

count = 0

def dfs(idx, value, numbers, target):
    # 전역변수 count 사용 선언
    global count
    len_num = len(numbers)
    if idx == len_num:
        if value == target:
            count += 1
        return

    dfs(idx + 1, value + numbers[idx], numbers, target)
    dfs(idx + 1, value + numbers[idx], numbers, target)


def solution(numbers, target):
   global count
   dfs(0, 0, numbers, target)

   return count


numbers = [4,1,2,1]
target = 4
print(solution(numbers, target))