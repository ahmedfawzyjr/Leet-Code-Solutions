class Solution:
    def findComplement(self, num: int) -> int:
        # Find the number of bits in num
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
