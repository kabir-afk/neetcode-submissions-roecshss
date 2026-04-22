class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        numMap = {}
        for num in nums:
            numMap[num]  = numMap.get(num,0) + 1
        sorted_numMap = sorted(numMap.items(),key=lambda x: x[1])
        sorted_numMap.reverse()
        for i in range(k):
            res.append(sorted_numMap[i][0])
        return res