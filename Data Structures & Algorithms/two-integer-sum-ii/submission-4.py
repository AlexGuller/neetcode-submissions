class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lt = 0
        rt = len(numbers) - 1
        while lt < rt:
            if numbers[rt] + numbers[lt] == target:
                return [lt + 1, rt + 1]
            elif numbers[rt] + numbers[lt] < target:
                lt += 1
            elif numbers[rt] + numbers[lt] > target:
                rt -= 1
        return [-1, -1]
