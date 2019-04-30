# Coin Change 2
# https://leetcode.com/problems/coin-change-2/
# Completed 4/26/19

class Coin:
    def __init__(self, value: int):
        self.value = value

class Currency:
    def __init__(self, coins: [int]):
        self.coins = [ Coin(coin) for coin in coins ]

    def change_permutations(self, target: int) -> int:
        # Return the number of ways to make the target out of this currency
        counting_up = [1] + [ 0 for _ in range(target) ]
        for coin in self.coins:
            for i in range(target + 1):
                next_sum = i + coin.value
                
                if next_sum <= target:
                    counting_up[next_sum] += counting_up[i]

        return counting_up[target]

class Solution:
    def change(self, target: int, coins: List[int]) -> int:
        return Currency(coins).change_permutations(target)
