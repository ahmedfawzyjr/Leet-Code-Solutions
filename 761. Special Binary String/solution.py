class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        l = 0
        res = []
        for r, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(s[l+1:r]) + '0')
                l = r + 1
        return "".join(sorted(res, reverse=True))
