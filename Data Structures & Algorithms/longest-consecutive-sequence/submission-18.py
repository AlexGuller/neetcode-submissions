class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        notFound = set(nums)
        maxCounter = 0
        for n in nums:
            if n in notFound:
                counter = 1
                curr = n
                notFound.remove(n)

                left = curr
                while len(notFound) > 0 and left + 1 in notFound:
                    counter += 1
                    left += 1
                    notFound.remove(left)
                
                right = curr
                while len(notFound) > 0 and right - 1 in notFound:
                    counter += 1
                    right -= 1
                    notFound.remove(right)
            maxCounter = max(counter, maxCounter)
        return maxCounter