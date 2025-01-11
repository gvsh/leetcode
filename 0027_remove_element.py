
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n
    

if __name__ == '__main__':

    solution = Solution()

    nums = [3, 2, 2, 3]
    val = 3
    print(solution.removeElement(nums, val))  # 2

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(solution.removeElement(nums, val))  # 5

    nums = [1]
    val = 1
    print(solution.removeElement(nums, val))  # 0

    nums = [1]
    val = 2
    print(solution.removeElement(nums, val))  # 1
