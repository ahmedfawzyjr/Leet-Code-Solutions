class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        # If k is still > 0, remove from the end
        if k > 0:
            stack = stack[:-k]
            
        # Remove leading zeros and handle empty string
        res = "".join(stack).lstrip('0')
        return res if res else "0"
