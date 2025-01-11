
from typing import List



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        i = 1
        j = 1
        count = 1

        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    i += 1
                    continue
            else:
                count = 1
            nums[j] = nums[i]
            j += 1
            i += 1

        del nums[j:]
        
        return len(nums)



    
if __name__ == "__main__":

    solution = Solution()
    print(solution.removeDuplicates([1, 1, 1, 2, 2, 3]))  # 5

    print(solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))  # 7

    print(solution.removeDuplicates([1, 2, 3]))  # 3

    print(solution.removeDuplicates([1, 1, 1, 1]))  # 2
