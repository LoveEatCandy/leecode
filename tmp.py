from collections import defaultdict


class Solution:
    def minTransfers(self, transactions: list(list(int))) -> int:
        people = defaultdict(int)
        for x, y, z in transactions:
            people[x] -= z
            people[y] += z
        price = []
        for v in people.values():
            if v != 0:
                price.append(v)
        res = float('inf')

        def dfs(i, cnt):
            nonlocal res
            while cnt > res: return
            while i < len(price) and price[i] == 0: i += 1
            if i == len(price):
                res = min(res, cnt)
                return
            for j in range(i + 1, len(price)):
                if price[i] * price[j] < 0:
                    price[j] += price[i]
                    dfs(i + 1, cnt + 1)
                    price[j] -= price[i]

        return res
