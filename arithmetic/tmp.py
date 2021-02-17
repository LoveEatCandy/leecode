from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def do(others, xy, old):
            if not others:
                return True
            _next, others = others[0], others[1:]
            for xx, yy in direct:
                cur = (xy[0] + xx, xy[1] + yy)
                print(cur, old)
                if 0 <= cur[0] < len(board) and 0 <= cur[1] < len(board[0]) and board[cur[0]][cur[1]] == _next and cur not in old:
                    old.add(cur)
                    if do(others, cur, old):
                        return True
                    old.remove(cur)
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if do(word[1:], (i, j), {(i, j)}):
                        return True
        return False


print(Solution().exist([["a", "a"]], "aaa"))
