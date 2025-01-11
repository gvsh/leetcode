
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(curr, first_num):
            if len(curr) == k:
                ans.append(curr[:])
                return

            for num in range(first_num, n + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()
        
        ans = []

        backtrack([], 1)

        return ans
    

if __name__ == '__main__':

    solution = Solution()

    comb_4_2 = solution.combine(4, 2)  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    print(f"{comb_4_2=}")

    comb_4_3 = solution.combine(4, 3)  # [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
    print(f"{comb_4_3=}")
    
    comb_5_3 = solution.combine(5, 3)  # [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]
    