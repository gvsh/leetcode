
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # Find the index of the pivot element (the smallest element)
        right_most_elem = nums[-1]
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > right_most_elem:
                left = mid + 1
            else:
                right = mid - 1

        # Binary search over an inclusive range [left_boundary ~ right_boundary]
        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        # Binary search over elements on the pivot element's left
        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer

        # Binary search over elements on the pivot element's right
        return binarySearch(left, n - 1, target)



# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

#         n = len(nums)
#         left, right = 0, n - 1
        
#         while left <= right:

#             mid = left + (right - left) // 2

#             # Case 1: find target
#             if nums[mid] == target:
#                 return mid

#             # Case 2: subarray on mid's left is sorted
#             elif nums[mid] >= nums[left]:
#                 if target >= nums[left] and target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1

#             # Case 3: subarray on mid's right is sorted.
#             else:
#                 if target <= nums[right] and target > nums[mid]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1

#         return -1
    

if __name__ == "__main__":

    solution = Solution()

    # print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 2))  # 6

    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))  # -1

    print(solution.search([1], 0))  # -1

    print(solution.search([1, 3], 3))  # 1

    print(solution.search([3, 1], 1))  # 1
