from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        minimum = 999999

        for p in prices:
            minimum = min(minimum, p)
            diff = max(diff, p - minimum)
        return print(diff)



if __name__ == '__main__':
    a = Solution()
    prices = [7,1,5,3,6,4]
    a.maxProfit(prices)

