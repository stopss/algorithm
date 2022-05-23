from typing import List

# for문 중첩
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_diff = 0
#         for i, p in enumerate(prices):
#             for j in range(i+1, len(prices)):
#                 if prices[i] < prices[j]:
#                     diff = prices[j] - prices[i]
#                     max_diff = max(max_diff, diff)
#
#         return print(max_diff)

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

