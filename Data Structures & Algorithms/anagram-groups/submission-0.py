class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        occ={}
        for s in strs:
            sorted_key = ''.join(sorted(s))
            if sorted_key in occ:
                occ[sorted_key].append(s)
            else:
                occ[sorted_key] = [s]
        print(occ)
        for key,value in occ.items():
            res.append(value)
        return res