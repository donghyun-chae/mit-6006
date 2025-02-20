class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t) :
            return False

        letters = dict()
        letters2 = dict()

        for i in range(len(s)):

            if s[i] in letters:
                letters[s[i]] += 1
            else:
                letters[s[i]] = 1

            if t[i] in letters2:
                letters2[t[i]] += 1
            else:
                letters2[t[i]] = 1
        
        return letters == letters2 