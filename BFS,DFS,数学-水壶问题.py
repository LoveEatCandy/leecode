'''
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
示例 2:

输入: x = 2, y = 6, z = 5
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/water-and-jug-problem
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# BFS
class Solution1:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        from collections import deque
        queue = deque([[0, 0]])
        visited = set([(0, 0)])

        while queue:
            cur_x, cur_y = queue.pop()
            if z in [cur_x, cur_y, cur_x + cur_y]:
                return True
            for item in [
                # 加满水
                (x, cur_y), (cur_x, y),
                # 清空水
                (0, cur_y), (cur_x, 0),
                # x -> y
                (cur_x + cur_y - y, y) if cur_x + cur_y >= y else (0, cur_x + cur_y),
                # y -> x
                (x, cur_x + cur_y - x) if cur_x + cur_y >= x else (cur_x + cur_y, 0)]:
                if item not in visited:
                    queue.appendleft(item)
                    visited.add(item)
        return False


# DFS
class Solution2:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        visited = set()

        def helper(cur_x, cur_y):
            # print(cur_x, cur_y)
            if z in [cur_x, cur_y, cur_x + cur_y]:
                return True
            for item in [
                # 加满水
                (x, cur_y), (cur_x, y),
                # 清空水
                (0, cur_y), (cur_x, 0),
                # x -> y
                (cur_x + cur_y - y, y) if cur_x + cur_y >= y else (0, cur_x + cur_y),
                # y -> x
                (x, cur_x + cur_y - x) if cur_x + cur_y >= x else (cur_x + cur_y, 0)]:
                if item not in visited:
                    visited.add(item)
                    if helper(*item):
                        return True
                    visited.remove(item)

            return False

        return helper(x, y)


# 数学
class Solution3:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        import math
        if x + y < z: return False
        if x == z or y == z or x + y == z: return True
        return z % math.gcd(x, y) == 0

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/water-and-jug-problem/solution/bao-li-shu-xue-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
