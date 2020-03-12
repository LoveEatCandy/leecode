class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        mode = list(range(1, 10))
        count = 1

        def do(cur, others):
            nonlocal count
            if m <= len(cur) <= n:
                count += 1
            for i, w in enumerate(others):
                do(cur+[w], others[:i]+others[i+1:])

        do([], mode)
        return count




