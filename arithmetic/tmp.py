from typing import List


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        less_item_num = [0] * x
        for s in staple:
            if s < x:
                less_item_num[s] += 1
        accu = 0
        for i in range(1, x):
            accu += less_item_num[i]
            less_item_num[i] = accu
        res = 0
        for d in drinks:
            if d < x:
                res += less_item_num[x - d]
        return res % (10 ** 9 + 7)


