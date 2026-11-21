class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        notSeen = set(nums)
        maxCtr = 0
        for n in nums:
            currCtr = 0
            if n in notSeen:
                curr = n
                notSeen.remove(n)
                currCtr += 1
                #lt
                lt = curr
                while notSeen and lt - 1 in notSeen:
                    lt -= 1
                    notSeen.remove(lt)
                    currCtr += 1
                #rt
                rt = curr
                while notSeen and rt + 1 in notSeen:
                    rt += 1
                    notSeen.remove(rt)
                    currCtr += 1
            maxCtr = max(currCtr, maxCtr)
        return maxCtr