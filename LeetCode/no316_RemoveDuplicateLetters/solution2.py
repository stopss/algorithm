# 재귀 함수를 이용 방법

class Solution:
    def removeDuplicteLetters(self, s: str) -> str:
		# 알파벳 순으로 정렬을 한다.
        for char in sorted(set(s)):
        	# char부터 접미사(suffix)를 분리한다.
            suffix = s[s.index(char):]

			# 분리 가능 여부를 판단하기 위해
            # 전체 집합(set(s))과 접미사 집합(set(suffix))가 일치하는 지 확인한다.
            if set(s) == set(suffix):
            	# 일치한다면, 현재 문자는 리턴하고 현재 문자의 이후 문자들(중복 문자들)은 빈 문자로 대체(replace)한다.
                return char + self.removeDuplicteLetters(suffix.replace(char, ''))

        return ''



# class Solution:
#     def removeDuplicteLetters(self, s: str) -> str:
#
#         for char in sorted(set(s)):
#             print(char)
#             print("s: ", s)
#
#             print("전체집합: ", set(s))
#             suffix = s[s.index(char):]
#             print(suffix)
#             print("접미사집합: ", set(suffix))
#
#             if set(s) == set(suffix):
#                 print("전체집합과 접미사 집합이 같다.")
#
#                 print("확인",suffix.replace(char,''))
#                 print("==========")
#                 return char + self.removeDuplicteLetters(suffix.replace(char, ''))
#
#         return ''

if __name__ == '__main__':
    s1 = "bcabc"
    s2 = "cbacdcbc"
    e1 = "abc"
    e2 = "acbd"
    a = Solution()

    print(e1, "-", a.removeDuplicteLetters(s1))
    print(e2, "-", a.removeDuplicteLetters(s2))