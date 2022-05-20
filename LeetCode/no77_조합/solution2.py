import itertools
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))


if __name__ == '__main__':
    a = Solution()
    print(a.combine(5,3))
