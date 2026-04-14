class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start,end = 1 , max(piles)
        res = end
        while start <= end:
            mid = start + (end - start)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours <= h:
                res = min(res,mid)
                end = mid - 1
            else:
                start = mid + 1
        return res