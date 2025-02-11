def wordBreak(s, wordDict) -> bool:

  d = set(wordDict)

  curr = []
  for (i,c) in enumerate(s):
      if s[:i+1] in d:
          curr.append(i+1)
    
      for (j,last_idx) in enumerate(curr) :
          # print(s[last_idx:i+1])
          if s[last_idx:i+1] in d:
              curr[j] = i+1
      print(curr)

  if len(curr) == 0:
      return False
  if len(s) in curr:
      return True
  return False

# wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", 
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# )
# wordBreak("catsandog", ["cats","dog","sand","and","cat"])
wordBreak("catsandog", ["cats", "cat", "catsan", "dog"])