class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(char in jewels for char in stones)


if __name__ == '__main__':
    s1 = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    print(s1.numJewelsInStones(jewels, stones))

    s2 = Solution()
    jewels = "z"
    stones = "ZZ"
    print(s2.numJewelsInStones(jewels, stones))