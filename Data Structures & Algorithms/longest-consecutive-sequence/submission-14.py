class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        notFound = set(nums)
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] in notFound:
                currCount = 1
                curr = nums[i]
                notFound.remove(nums[i])

                #left
                left = curr
                while left - 1 in notFound:
                    left -= 1
                    notFound.remove(left)
                    currCount += 1
                
                #right
                right = curr
                while right + 1 in notFound:
                    right += 1
                    notFound.remove(right)
                    currCount += 1
                maxCount = max(currCount, maxCount)
        return maxCount