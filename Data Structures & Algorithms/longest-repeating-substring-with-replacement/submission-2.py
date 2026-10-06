class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            l = 0
            r = 0
            count = 0
            while r < len(s):
                # count of same chars used to figure out replacements
                if s[r] == c:
                    count += 1
                # check how many replacements we've done, if too many then we have to decrease substring
                while (r - l + 1) - count > k:
                    # if we remove matching char then decrement count
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)

                r += 1
        return res