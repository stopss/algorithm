class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = start = 0
        temp = {}
        for i, c in enumerate(s):
            # print('i: ', i, ", c: ", c, "start: ", start, "temp: ", temp)
            if c in temp and start <= temp[c]:
                start = temp[c] + 1
                # print("start: ", start)
            else:
                max_len = max(max_len, i - start + 1)
                # print("max: ", max_len)

            temp[c] = i
            # print("=============")

        return max_len


if __name__ == '__main__':
    a1 = Solution()
    s1 = "abcabcbb"
    print(3, s1, a1.lengthOfLongestSubstring(s1))

    a2 = Solution()
    s2 = "bbbbb"
    print(1, s2, a2.lengthOfLongestSubstring(s2))

    a3 = Solution()
    s3 = "pwwkew"
    print(3, s3, a3.lengthOfLongestSubstring(s3))

    a4 = Solution()
    s4 = "dvdf"
    print(3, s4, a4.lengthOfLongestSubstring(s4))

    a5 = Solution()
    s5 = "tmmzuxt"
    print(5, s5, a5.lengthOfLongestSubstring(s5))