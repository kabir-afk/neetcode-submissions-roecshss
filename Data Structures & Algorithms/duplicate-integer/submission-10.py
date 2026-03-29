class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occ = {}
        for i in nums:
            if i in occ:
                occ[i] += 1
            else:
                occ[i] = 1
        for i in occ:
            if occ[i] > 1:
                return True
        return False