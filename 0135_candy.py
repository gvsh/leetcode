
from typing import List


class Solution:

    def candy(self, ratings: List[int]) -> int:
        
        sum = 0
        n = len(ratings)
        left2right = [1] * n
        right2left = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1
        
        for i in range(n):
            sum += max(left2right[i], right2left[i])

        return sum


if __name__ == '__main__':
    
    solution = Solution()

    print(solution.candy([1, 0, 2]))  # 5

    print(solution.candy([1, 2, 2]))  # 4

    print(solution.candy([1, 2, 3, 4, 5]))  # 15

    print(solution.candy([1, 3, 2, 2, 1]))  # 7

    print(solution.candy([1, 0, 2, 2, 1]))  # 7

    print(solution.candy([1, 2, 87, 87, 87, 2, 1]))  # 13

    print(solution.candy([1, 2, 87, 87, 87, 2, 1, 2]))  # 15
