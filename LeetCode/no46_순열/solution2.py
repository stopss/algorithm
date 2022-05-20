import itertools
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        return list(itertools.permutations(nums))


if __name__ == '__main__':
    a = Solution()
    nums = [1,2,3]
    a.permute(nums)


