from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def binary_search(numbers, target, idx):
            left = 0
            right = len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2
                # 겹쳐지는 숫자가 나오는 경우 -> mid를 오늘쪽으로 한 칸 이동
                if mid == idx:
                    mid += 1
                if numbers[mid] == target:
                    return mid
                elif numbers[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return None


        for i, n in enumerate(numbers):
            t = target - n
            result = binary_search(numbers, t, i)
            if result != None:
                return [i+1, result+1]
            else:
                continue

if __name__ == '__main__':
    a = Solution()
    numbers = [1, 2, 3, 4, 4, 9, 56, 90]
    target = 8
    print(a.twoSum(numbers, target))





