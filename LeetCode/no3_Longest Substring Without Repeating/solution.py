class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = start = 0
        used = {}

        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1

            else:
                max_len = max(max_len, index - start + 1)

            used[char] = index

        return max_len


if __name__ == '__main__':
    a1 = Solution()
    s1 = "abcabcbb"
    print(s1, a1.lengthOfLongestSubstring(s1))

    a2 = Solution()
    s2 = "bbbbb"
    print(s2, a2.lengthOfLongestSubstring(s2))

    a3 = Solution()
    s3 = "pwekew"
    print(s3, a3.lengthOfLongestSubstring(s3))
