class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charsInS={}
        charsInT={}
        for i in s:
            if i in charsInS:
                charsInS[i] +=1
            else:
                charsInS[i] = 1
        for i in t:
            if i in charsInT:
                charsInT[i] +=1
            else:
                charsInT[i] = 1
        return charsInS == charsInT