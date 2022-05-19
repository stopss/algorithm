# collection.defaultdict를 이용한 비교 방식
import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # defaultdict - 존재하지 않는 키에 대해 디폴트를 리턴해준다.
        freqs = collections.defaultdict(int)
        count = 0

        # stone의 빈도 수 계산
        for char in stones:
            freqs[char] += 1

        # jewels 빈도 수 계싼
        for char in jewels:
            count += freqs[char]

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
