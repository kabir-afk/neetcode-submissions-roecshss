class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        k = len(s1)
        occ={}
        perm={}
        for ch in s1:
            occ[ch] = occ.get(ch,0) + 1
        while j < len(s2):
            perm[s2[j]] = perm.get(s2[j],0) + 1
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                if perm == occ:
                    return True
                perm[s2[i]] -= 1
                if perm[s2[i]] == 0:
                    del perm[s2[i]]
                i += 1
                j += 1
        return False

