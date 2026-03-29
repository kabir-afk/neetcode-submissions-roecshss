class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ={}
        result=[]
        for i in nums:
            if i not in occ:
                occ[i] = 1
            occ[i] += 1
        sorted_occ_by_value = sorted(occ.items(),key = lambda x:x[1])
        sorted_occ_by_value.reverse()
        for i in range(k):
            result.append(sorted_occ_by_value[i][0])
        return result