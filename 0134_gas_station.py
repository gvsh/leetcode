
from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        curr_gain = 0
        answer = 0

        for i in range(len(gas)):
            # gain[i] = gas[i] - cost[i]
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]

            # If we meet a "valley", start over from the next station
            # with 0 initial gas.
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1

        return answer if total_gain >= 0 else -1
    

if __name__ == '__main__':

    solution = Solution()

    gas = [1, 2, 3, 4, 5]

    cost = [3, 4, 5, 1, 2]

    print(solution.canCompleteCircuit(gas, cost))  # 3

    print(solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]))  # -1

    print(solution.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))  # 4

    print(solution.canCompleteCircuit([5, 8, 2, 8], [6, 5, 6, 6]))  # 3

    
    