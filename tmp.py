class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if len(word1) > len(word2):
            word1, word2 = word2, word1
        start = 0
        m_len = len(word1)
        m_count = 0
        while start < m_len - m_count:

            tmp = word1[start:]
            cur_count = 0
            for i, w in enumerate(tmp):
                if word2[i] != w and cur_count > 0:
                    break
                elif word2[i] == w:
                    cur_count += 1
            m_count = max(m_count, cur_count)
        return len(word1) + len(word2) - m_count * 2





