class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        Bulls: Correct digit in correct position.
        Cows: Correct digit in wrong position.
        """
        bulls = 0
        cows = 0
        s_count = [0] * 10
        g_count = [0] * 10
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_count[int(s)] += 1
                g_count[int(g)] += 1
        
        for i in range(10):
            cows += min(s_count[i], g_count[i])
            
        return f"{bulls}A{cows}B"
