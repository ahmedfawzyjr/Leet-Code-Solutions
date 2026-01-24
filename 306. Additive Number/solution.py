class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                s1, s2 = num[:i], num[i:j]
                if (len(s1) > 1 and s1.startswith('0')) or \
                   (len(s2) > 1 and s2.startswith('0')):
                    continue
                
                while j < n:
                    s3 = str(int(s1) + int(s2))
                    if not num.startswith(s3, j):
                        break
                    j += len(s3)
                    s1, s2 = s2, s3
                
                if j == n:
                    return True
        return False
