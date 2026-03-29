class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        res = 0 
        occ = {}
        for j in range(len(s)):
            occ[s[j]] = occ.get(s[j],0) + 1
            max_occ = max(occ.values())
            if (j - i + 1) - max_occ > k:
                occ[s[i]] -= 1
                i += 1
            res = max(res,j - i + 1)
        return res