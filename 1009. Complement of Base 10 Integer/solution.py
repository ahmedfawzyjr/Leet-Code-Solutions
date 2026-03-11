class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        # n.bit_length() returns the number of bits needed to represent an integer in binary, excluding the sign and leading zeros.
        mask = (1 << n.bit_length()) - 1
        return n ^ mask
