class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = 0
        while curr < len(nums) - 2:
            if nums[curr] > 0:
                break

            lt = curr + 1
            rt = len(nums) - 1
            while lt < rt:
                tot = nums[curr] + nums[lt] + nums[rt]
                if tot == 0:
                    res.append([nums[curr], nums[lt], nums[rt]])
                    while lt < rt and nums[lt] == nums[lt + 1]:
                        lt += 1
                    while lt < rt and nums[rt] == nums[rt - 1]:
                        rt -= 1
                    lt += 1
                    rt -= 1
                elif tot < 0:
                    lt += 1
                else:
                    rt -= 1
            while curr < len(nums) - 1 and nums[curr] == nums[curr + 1]:
                curr += 1
            curr += 1
        return  res