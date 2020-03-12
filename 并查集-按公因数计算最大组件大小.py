'''
给定一个由不同正整数的组成的非空数组 A，考虑下面的图：

有 A.length 个节点，按从 A[0] 到 A[A.length - 1] 标记；
只有当 A[i] 和 A[j] 共用一个大于 1 的公因数时，A[i] 和 A[j] 之间才有一条边。
返回图中最大连通组件的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-component-size-by-common-factor
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from math import sqrt
from typing import List


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]

            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)
                if root_x != root_y:
                    self.parent[root_x] = root_y

            def find(self, x):
                while x != self.parent[x]:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x

        max_val = max(A)
        union_find = UnionFind(max_val + 1)

        for num in A:
            up_bound = int(sqrt(num))
            for i in range(2, up_bound + 1):
                if num % i == 0:
                    union_find.union(num, i)
                    union_find.union(num, num // i)

        cnt = [0 for _ in range(max_val + 1)]
        res = 0
        for num in A:
            root = union_find.find(num)
            cnt[root] += 1
            res = max(res, cnt[root])
        return res

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/largest-component-size-by-common-factor/solution/bing-cha-ji-java-python-by-liweiwei1419/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
test = [2, 3, 6, 7, 4, 12, 21, 39]
p = Solution()
print('===================', p.largestComponentSize(test))
