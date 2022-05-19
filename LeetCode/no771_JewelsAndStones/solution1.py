# collection.Counter를 이용
import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Counter를 사용해서 stones에 들어있는 각 글자의 개수를 파악한다.
        a_hash = collections.Counter(stones)
        count = 0

        for char in jewels:
            # a_hash에 jewles에 들어있는 글자가 있다면
            if char in a_hash:
                # count에 해당 글자의 개수만큼 더한다.
                count += a_hash[char]

        return print(count)


if __name__ == '__main__':
    s1 = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    s1.numJewelsInStones(jewels, stones)

    s2 = Solution()
    jewels = "z"
    stones = "ZZ"
    s2.numJewelsInStones(jewels, stones)
