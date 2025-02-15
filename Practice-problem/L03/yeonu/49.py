class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dicts = [] 
        answer = []
        for str in strs:
            letters = {}
            for letter in str:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
                
            isNew = True
            for (i, d) in enumerate(dicts):
                if d == letters:
                    answer[i].append(str)
                    isNew = False
                    break
            if isNew:
                dicts.append(letters)
                answer.append([str])

        return answer