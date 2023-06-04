class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for R in range(len(s)): 
            count[s[R]] = 1 + count.get(s[R], 0)
            while (R-l+1) - max(count.values())>k:
                count[s[l]] -= 1
                l += 1
            res = max(res, R - l + 1)
        return res 