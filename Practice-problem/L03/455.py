class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        i = 0
        j = 0
        while (i < len(s) and j < len(g)):
            if s[i] >= g[j]:
                j += 1
                result += 1
            i += 1

        return result