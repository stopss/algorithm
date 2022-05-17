# 스택을 이용한 문자 제거
import collections

class Solution:
    def removeDuplicteLetters(self, s: str) -> str:
        # seen - 중복 항목을 찾고 다른 중복 목록을 만들기 위한 집합 함수
        # collections.counter를 이용하여 문자열 내의 각 글자마다 등장 횟수를 파악한다.
        counter, seen, stack = collections.Counter(s), set(), []

        # 문자열의 앞부터 탐색해 글자 하나씩 스택에 push한다.
        for char in s:
            # 탐색한 글자의 counter는 하나씩 감소한다.(해당 글자는 스택에 push 하기 때문에)
            counter[char] -= 1
            # 이미 문자열이 집합함수에 추가되었다면 스택에 push할 필요가 없어서 다음 글자로 넘어간다.
            if char in seen:
                continue

            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            # 1. while stack -> stack이 비어있고(처음 시점이고)
            # 2. char < stack[-1] -> 후행 글자(char = b)가 선행 글자(stack[-1] = c)보다 작다면
            # 3. 선행 글자(stack[-1] = c)의 counter가 1이상일 때
            # 위의 세 가지 조건 일 때 pop을 한다.
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        # 모든 글자를 탐색했다면 stack 에 남아있는 글자를 문자열로 변경해 리턴한다.
        return ''.join(stack)



# class Solution:
#     def removeDuplicteLetters(self, s: str) -> str:
#         # seen - 중복 항목을 찾고 다른 중복 목록을 만들기 위한 집합 함수
#         counter, seen, stack = collections.Counter(s), set(), []
#
#         for char in s:
#             counter[char] -= 1
#             print("char: ", char, counter[char])
#             if char in seen:
#                 print("seen1", seen)
#                 print("========패스========")
#                 continue
#
#             # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
#             while stack and char < stack[-1] and counter[stack[-1]] > 0:
#                 seen.remove(stack.pop())
#                 print("pop")
#
#             stack.append(char)
#             seen.add(char)
#             print("stack: ", stack)
#             print("seen2: ", seen)
#             print("========================")
#
#         return ''.join(stack)

if __name__ == '__main__':
    s1 = "bcabc"
    s2 = "acdb"
    e1 = "abc"
    e2 = "acbd"
    a = Solution()

    print(e1, "-", a.removeDuplicteLetters(s1))
    print(e2, "-", a.removeDuplicteLetters(s2))