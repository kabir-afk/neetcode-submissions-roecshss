class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0
        j = 0
        res = []
        while i < len(temperatures):
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    i += 1
                    j = i
                else:
                    j += 1
            res.append(0)
            i += 1
            j = i
        return res