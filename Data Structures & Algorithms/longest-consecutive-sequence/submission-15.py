class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        notSeen = set(nums)
        maxCount = 0
        for n in nums:
            if n in notSeen:
                currCount = 1
                curr = n
                notSeen.remove(n)
                #left
                left = curr
                while left - 1 in notSeen:
                    left -= 1
                    currCount += 1
                    notSeen.remove(left)
                
                #right
                right = curr
                while right + 1 in notSeen:
                    right += 1
                    currCount += 1
                    notSeen.remove(right)
                maxCount = max(currCount, maxCount)
        return maxCount