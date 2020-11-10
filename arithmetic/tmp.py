from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s:
            return []
        r = set()

        def do(tmp, other):
            if not other:
                r.add(tmp)
            else:
                for i, ss in enumerate(other):
                    do(tmp+ss, other[:i-1]+other[i+1:])
        do('', s)
        return list(r)

