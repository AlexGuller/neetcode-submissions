class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr = 0
        res = []
        while curr < len(nums) - 2:
            if nums[curr] > 0:
                break
            lt = curr + 1
            rt = len(nums) - 1
            while lt < rt:
                if nums[curr] + nums[lt] + nums[rt] == 0:
                    res.append([nums[curr], nums[lt], nums[rt]])
                    #skip dupes
                    while lt < rt and nums[lt + 1] == nums[lt]:
                        lt += 1
                    while rt > lt and nums[rt - 1] == nums[rt]:
                        rt -= 1
                    lt += 1
                    rt -= 1
                elif nums[curr] + nums[lt] + nums[rt] < 0:
                    lt += 1
                else:
                    rt -= 1
            while curr < len(nums) - 1 and nums[curr + 1] == nums[curr]:
                curr += 1
            curr += 1
        return res