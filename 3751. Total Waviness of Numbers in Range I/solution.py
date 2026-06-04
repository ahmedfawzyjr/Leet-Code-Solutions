
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        
        for num in range(num1, num2 + 1):
            digits = list(map(int, str(num)))
            if len(digits) < 3:
                continue
            for i in range(1, len(digits) - 1):
                prev = digits[i-1]
                curr = digits[i]
                next_d = digits[i+1]
                if (curr > prev and curr > next_d) or (curr < prev and curr < next_d):
                    total += 1
        return total
