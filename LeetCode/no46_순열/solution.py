from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        results = []
        prev_element = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            # 리프 노드는 자식이 없는 노드
            if len(elements) == 0:
                results.append(prev_element[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_element.append(e)
                dfs(next_elements)
                prev_element.pop()

        dfs(nums)

        return print(results)


if __name__ == '__main__':
    a = Solution()
    nums = [1,2,3]
    a.permute(nums)


