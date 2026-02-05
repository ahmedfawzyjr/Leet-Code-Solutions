class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        
        s1cnt, s2cnt, index = 0, 0, 0
        # recall[index] = (s1cnt, s2cnt)
        # Store state (index in s2) to detect cycles
        recall = {}
        
        while True:
            s1cnt += 1
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2cnt += 1
                        index = 0
            
            if s1cnt == n1:
                return s2cnt // n2
            
            if index in recall:
                s1cnt_prev, s2cnt_prev = recall[index]
                # Pattern found: cycle length in s1 is (s1cnt - s1cnt_prev)
                # s2 count in one cycle is (s2cnt - s2cnt_prev)
                period = s1cnt - s1cnt_prev
                # How many full cycles fit in remaining s1
                num_cycles = (n1 - s1cnt_prev) // period
                ans = s2cnt_prev + num_cycles * (s2cnt - s2cnt_prev)
                # Leftover s1 count after full cycles
                remainder = (n1 - s1cnt_prev) % period
                
                for _ in range(remainder):
                    for ch in s1:
                        if ch == s2[index]:
                            index += 1
                            if index == len(s2):
                                ans += 1
                                index = 0
                return ans // n2
            
            recall[index] = (s1cnt, s2cnt)
