
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums: List[int], l: int, r: int) -> int:
        if l == r:
            return l
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            return self.search(nums, l, mid)
        return self.search(nums, mid + 1, r)
    

if __name__ == "__main__":

    solution = Solution()

    print(solution.findPeakElement([1, 2, 3, 1]))  # 2

    print(solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # 5
