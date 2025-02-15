class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
          
        accounts_dict = dict()
        
        temp = set()
        for acc in accounts:
            if acc[0] in accounts_dict:
            
                for i in range(1, len(acc)):
                    isNew = True
                    
                    for a in accounts_dict[acc[0]]:
                        if acc[i] in a:
                            
                            if not isNew:
                                accounts_dict[acc[0]].remove(temp)
                                temp.update(t)
                                a.update(temp)
                            temp = a.union(acc[1:])
                            t = a.union(acc[1:])
                            a.update(acc[1:])
                            isNew = False
                    if isNew:
                        accounts_dict[acc[0]].append(set(acc[1:]))
            else:
                accounts_dict[acc[0]] = [set(acc[1:])]
                
        result = []
        for person in accounts_dict:
            for acc in accounts_dict[person] :
                result.append([person])
                for a in sorted(acc):
                    result[-1].append(a)
        return result