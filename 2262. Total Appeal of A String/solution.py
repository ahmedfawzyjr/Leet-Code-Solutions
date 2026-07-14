class Solution:
    def appealSum(self, s: str) -> int:
        last_pos = {}
        total_appeal = 0
        current_appeal_sum = 0
        
        for i, char in enumerate(s):
            prev = last_pos.get(char, -1)
            current_appeal_sum += i - prev
            total_appeal += current_appeal_sum
            last_pos[char] = i
            
        return total_appeal
