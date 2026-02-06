class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0: return 0
        if n <= 3: return 1
        
        s = [1, 2, 2]
        head = 2
        while len(s) < n:
            # s[head] tells us how many times the next number should appear
            # The next number is alternating between 1 and 2
            # current last number is s[-1], next is 3 - s[-1]
            next_num = 3 - s[-1]
            s += [next_num] * s[head]
            head += 1
            
        return s[:n].count(1)
