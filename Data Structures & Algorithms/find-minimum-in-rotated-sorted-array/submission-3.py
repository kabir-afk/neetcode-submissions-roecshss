class Solution:
    def findMin(self, nums: List[int]) -> int:
        window = {}
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                continue
            else:
                return nums[i + 1]
        return nums[0]