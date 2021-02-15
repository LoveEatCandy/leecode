from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = wordDict[::-1]
        r = []

        def do(before, others):
            nonlocal r
            print(before, others)
            for cur in wordDict:
                if others.startswith(cur):
                    tmp = others[len(cur):]
                    tmp_ = before + " " + cur if before else cur
                    if tmp:
                        do(tmp_, tmp)
                    else:
                        r.append(tmp_)
            return

        do("", s)
        return r


a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
b = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
print(Solution().wordBreak(a, b))
