


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        size = len(nums)
        insertIndex = 1
        
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i]
                # Incrementing insertIndex count by 1
                insertIndex = insertIndex + 1
        
        return insertIndex
    

if __name__ == '__main__':

    solution = Solution()

    nums = [1, 1, 2]
    print(solution.removeDuplicates(nums))  # 2

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(solution.removeDuplicates(nums))  # 5
    