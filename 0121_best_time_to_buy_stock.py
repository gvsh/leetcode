
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            
        min_price = float('inf')
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price
                
            current_profit = price - min_price
            
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
    


if __name__ == '__main__':

    solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]

    print(solution.maxProfit(prices))  # 5

    prices = [7, 6, 4, 3, 1]

    print(solution.maxProfit(prices))  # 0

    prices = [7, 2, 5, 1, 6, 4]

    print(solution.maxProfit(prices))  # 5

    prices = [7, 2, 5, 1, 6, 4, 3]

    print(solution.maxProfit(prices))  # 5
    