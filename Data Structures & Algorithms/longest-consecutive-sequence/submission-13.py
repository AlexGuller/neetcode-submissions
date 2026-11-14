class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] in seen:
                currCount = 1

                curr = nums[i]
                seen.remove(curr)

                lt = curr
                rt = curr

                #right
                while seen and rt + 1 in seen:
                    seen.remove(rt + 1)
                    rt += 1
                    currCount += 1
                #left
                while seen and lt - 1 in seen:
                    seen.remove(lt - 1)
                    lt -= 1
                    currCount += 1
            maxCount = max(maxCount, currCount)
        return maxCount
                
                