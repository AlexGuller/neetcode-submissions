from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = defaultdict(list)
        for string in strs:
            charList = [0] * 26
            for ch in list(string):
                charList[ord(ch) - ord('a')] += 1
            track[tuple(charList)].append(string)
        result = []
        for value in track.values():
            result.append(value)
        return result