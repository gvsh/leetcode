
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans
    

if __name__ == '__main__':
    solution = Solution()
    p1 = solution.permute([1, 2, 3])
    p2 = solution.permute([0, 1, 3, 4])

    print(f"{p1=}")
    print(f"{p2=}")

