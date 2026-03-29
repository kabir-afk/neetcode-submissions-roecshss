class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result=[]
        numsMap={}
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in numsMap:
                return [numsMap[difference],i+1]
            numsMap[numbers[i]] = i + 1
        return []
