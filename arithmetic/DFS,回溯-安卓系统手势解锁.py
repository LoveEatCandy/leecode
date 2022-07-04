"""
我们都知道安卓有个手势解锁的界面，是一个 3 x 3 的点所绘制出来的网格。

给你两个整数，分别为 ​​m 和 n，其中 1 ≤ m ≤ n ≤ 9，那么请你统计一下有多少种解锁手势，是至少需要经过 m 个点，但是最多经过不超过 n 个点的。

 

先来了解下什么是一个有效的安卓解锁手势:

每一个解锁手势必须至少经过 m 个点、最多经过 n 个点。
解锁手势里不能设置经过重复的点。
假如手势中有两个点是顺序经过的，那么这两个点的手势轨迹之间是绝对不能跨过任何未被经过的点。
经过点的顺序不同则表示为不同的解锁手势。
 


 

解释:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
无效手势：4 - 1 - 3 - 6
连接点 1 和点 3 时经过了未被连接过的 2 号点。

无效手势：4 - 1 - 9 - 2
连接点 1 和点 9 时经过了未被连接过的 5 号点。

有效手势：2 - 4 - 1 - 3 - 6
连接点 1 和点 3 是有效的，因为虽然它经过了点 2 ，但是点 2 在该手势中之前已经被连过了。

有效手势：6 - 5 - 4 - 1 - 9 - 2
连接点 1 和点 9 是有效的，因为虽然它经过了按键 5 ，但是点 5 在该手势中之前已经被连过了。

 

示例:

输入: m = 1，n = 1
输出: 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/android-unlock-patterns
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        mode = list(range(1, 10))
        count = 0
        condition = {
            "13": 2,
            "39": 6,
            "79": 8,
            "17": 4,
            "19": 5,
            "37": 5,
            "46": 5,
            "28": 5,
        }

        def do(cur, others):
            nonlocal count
            if m <= len(cur) <= n:
                count += 1
                if len(cur) == n:
                    return
            if others:
                for i, w in enumerate(others):
                    if len(cur) > 0:
                        key = "%d%d" % (min(w, cur[-1]), max(w, cur[-1]))
                        if key in condition and condition.get(key) not in cur:
                            continue
                    do(cur + [w], others[:i] + others[i + 1 :])

        do([1], mode[1:])
        do([2], mode[:1] + mode[2:])
        count *= 4
        do([5], mode[:4] + mode[5:])
        return count


from functools import lru_cache


class Solution2:
    def numberOfPatterns(self, m: int, n: int) -> int:
        graph = {
            1: {3: 2, 7: 4, 9: 5},
            2: {8: 5},
            3: {1: 2, 7: 5, 9: 6},
            4: {6: 5},
            5: {},
            6: {4: 5},
            7: {1: 4, 3: 5, 9: 8},
            8: {2: 5},
            9: {1: 5, 3: 6, 7: 8},
        }
        ans = 0

        @lru_cache(None)
        def dfs(status, current, count):
            if count == n:
                return 1
            current_ans = 0 if count < m else 1
            for i in range(1, 10):
                if status & (1 << i) == 0:
                    if i not in graph[current] or ((1 << graph[current][i]) & status):
                        current_ans += dfs(status | (1 << i), i, count + 1)
            return current_ans

        # for cur in range(1, 10):
        # ans += dfs(1 << cur, cur, 1)

        ans += 4 * dfs(1 << 1, 1, 1)
        ans += 4 * dfs(1 << 2, 2, 1)
        ans += dfs(1 << 5, 5, 1)

        return ans


"""
作者：amchor
链接：https: // leetcode - cn.com / problems / android - unlock - patterns / solution / dai - zhuang - tai - de - shen - du - you - xian - by - amchor /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
