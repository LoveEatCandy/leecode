from typing import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        cache = {coin: 1 for coin in coins}

        def do(balance):
            if balance in cache:
                return cache[balance]
            rr = float('inf')
            for coin in coins:
                if balance == coin:
                    return 1
                elif coin < balance:
                    r = do(balance - coin)
                    if r:
                        rr = min(rr, r + 1)
            rr = None if rr == float('inf') else rr
            cache[balance] = rr
            return rr

        return do(amount) or -1


coins = [186, 419, 83, 408]
amount = 6249
print(Solution().coinChange(coins, amount))
