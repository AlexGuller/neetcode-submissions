class Solution:
    def checkValidString(self, s: str) -> bool:
        # track the minimum and maximum # of '(' available at any point in time
        leftMin, leftMax = 0, 0
        for ch in s:
            if ch == '(':
                leftMin += 1
                leftMax += 1
            elif ch == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1 # '*' -> ')'
                leftMax += 1 # '*' -> '('
            # if at any point our maximum # of left is less than 0, that means we have too many ')' up till this and its impossible
            leftMin = max(0, leftMin)
            if leftMax < 0:
                return False
        # we know that the possible open '(' is more than ')', so now we just have to check that we don't have too many '(' by the end
        return leftMin == 0