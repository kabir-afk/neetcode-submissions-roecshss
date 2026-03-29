class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}    
        for index,value in enumerate(nums):
            diff = target - value
            if diff in numsMap:
                return [numsMap[diff],index]
            numsMap[value] = index
        return []