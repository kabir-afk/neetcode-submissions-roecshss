class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict={}
        result=[]
        for i in nums:
            numDict[i] =  numDict.get(i,0) + 1
        sorted_numDict_by_value = sorted(numDict.items(),key = lambda x:x[1])
        sorted_numDict_by_value.reverse()
        for i in range(k):
            result.append(sorted_numDict_by_value[i][0])
        return result