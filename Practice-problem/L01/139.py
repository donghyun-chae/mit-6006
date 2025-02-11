#!/usr/bin/env python3

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def recursion(s, wordDict):
            if len(s) < 0:
                return True

            for word in wordDict:
                if s[0] == word[0]:
                    recursion(new_s, wordDict)
            return False
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def recursion(s, wordDict):
            if len(s) < 0:
                return True

            for word in wordDict:
                if s[0] == word[0]:
                    recursion(new_s, wordDict)
            return Fquie
