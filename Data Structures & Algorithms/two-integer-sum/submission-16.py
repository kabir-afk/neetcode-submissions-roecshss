class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            index[nums[i]] = i
        print(index)
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in index and i != index[difference]:
                print()
                return [i , index[difference]]
        return []