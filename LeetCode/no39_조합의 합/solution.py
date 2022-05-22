from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def dfs(csum, index, path):
            # 종료 조건 2가지
            # csum < 0 : 목표값을 초과한 경우로 탐색을 종료한다.
            if csum < 0:
                return

            # csum = 0 : csum의 초기값은 target이며 csum의 0은 target가 정답이 일치하는 정답.
            if csum == 0:
                results.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return print(results)

if __name__ == '__main__':
    a = Solution()
    candidates = [2, 3, 6, 7]
    target = 7

    a.combinationSum(candidates, target)

