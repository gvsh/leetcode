

from typing import List

def longest_ones(nums, k):

    left = 0
    right = 0
    zeroes_count = 0
    max_count = 0
    # pdb.set_trace()
    for i in range(len(nums)):

        if nums[i] == 0:
            zeroes_count += 1

        if zeroes_count > k:
            max_count = max(max_count, i - left + 1)
            while zeroes_count > k and left < len(nums):
                if nums[left] == 0:
                    left += 1
                    zeroes_count -= 1
                else:
                    left += 1
    
    return max_count

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(longest_ones(nums, k))



