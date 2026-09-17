class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on max hours
        rt = max(piles)
        lt = 1
        mh = sys.maxsize
        while lt <= rt:
            mid = (rt + lt) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
            if hours <= h:
                mh = min(mh, mid)
                rt = mid - 1
            elif hours > h:
                lt = mid + 1
        return mh