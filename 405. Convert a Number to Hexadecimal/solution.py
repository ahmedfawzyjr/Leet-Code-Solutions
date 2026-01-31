class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
            
        # Handle 32-bit two's complement for negative numbers
        if num < 0:
            num += 2**32
            
        chars = "0123456789abcdef"
        res = []
        while num > 0:
            res.append(chars[num % 16])
            num //= 16
            
        return "".join(res[::-1])
