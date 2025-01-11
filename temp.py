
glu-neg 
bil- 1+ 1mg/dl 
ket +- 5 mg/dl 
sg- 1.030 
blo-neg 
ph- 6.0 
pro- neg 
uro- 0.2 mg/dl 
nit-neg 
leu- 3+ 500leu/ul
URINE IS CLEAR YELLOW 
GLU-NEG 
BIL-NEG 
KET-NEG 
SG-1.010 
BLO-NEG 
PH-7.0 
PRO-NEG 
URO- 0.2 MG/DL 
NIT-NEG 
LEU-NEG


from typing import List



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


solution = Solution()

longest_streak_01 = solution.longestConsecutive([100, 4, 200, 1, 3, 2]) # 4

longest_streak_02 = solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) # 9

longest_streak_03 = solution.longestConsecutive([1,2,0,1]) # 3

longest_streak_04 = solution.longestConsecutive([1,2,0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]) # 100


print(f"longest_streak_01: {longest_streak_01}")
print(f"longest_streak_02: {longest_streak_02}")
print(f"longest_streak_03: {longest_streak_03}")
print(f"longest_streak_04: {longest_streak_04}")



