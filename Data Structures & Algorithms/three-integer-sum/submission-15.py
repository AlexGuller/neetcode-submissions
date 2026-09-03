class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        result = []
        for i in range(len(num)):
            if i > 0 and num[i] == num[i - 1]:
                continue
            left = i + 1
            right = len(num) - 1
            while left < right:
                value = num[i] + num[left] + num[right]
                if value < 0:
                    left += 1
                elif value > 0:
                    right -= 1
                else:
                    result.append([num[i], num[left], num[right]])
                    left += 1
                    while left < right and num[left - 1] == num[left]:
                        left += 1
                    right -= 1
        return result