class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Cantor's Diagonal Argument
        # For each index i, we pick a character that is different from 
        # the character at index i of the i-th string in 'nums'.
        # This guaranteed 'res' is different from every string in 'nums'.
        res = []
        for i in range(len(nums)):
            # If nums[i][i] is '0', we take '1', and vice versa.
            res.append('1' if nums[i][i] == '0' else '0')
        
        return "".join(res)
