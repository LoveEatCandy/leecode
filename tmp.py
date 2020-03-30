class Solution:
    def trap(self, height: 'List[int]') -> int:
        res = 0
        stack = []

        def get_cur(l):
            print(l)
            if len(l) <= 2:
                return 0
            m = min(l[0], l[-1])
            if m == 0:
                return 0
            total = 0
            for i in l:
                cur = m - i
                if cur > 0:
                    total += cur
            return total

        down = True
        for h in height:
            if len(stack) == 1:
                if h <= stack[-1]:
                    stack.append(h)
                else:
                    stack = [h]
            elif len(stack) > 1:
                if h == stack[-1]:
                    stack.append(h)
                elif h > stack[-1]:
                    down = False
                    stack.append(h)
                elif down and h < stack[-1]:
                    stack.append(h)
                else:
                    res += get_cur(stack)
                    down = True
                    if stack[-1] > h:
                        stack = [stack[-1], h]
                    else:
                        stack = [h]
            else:
                if h > 0:
                    stack.append(h)
        if len(stack) > 0:
            res += get_cur(stack)
        return res


tmp = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
a = Solution()
print(a.trap(tmp))
