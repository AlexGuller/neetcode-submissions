class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lt = 0
        rt = len(numbers) -1
        while lt < rt:
            if target == numbers[lt] + numbers[rt]:
                return [lt + 1, rt + 1]
            elif target > numbers[lt] + numbers[rt]:
                lt += 1
            else:
                rt -= 1
        return [-1, -1]