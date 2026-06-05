class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        from functools import cache

        def count_waviness(n: int) -> int:
            # Base case: Numbers with fewer than 3 digits have 0 waviness
            if n < 100:
                return 0
            s = str(n)
            
            # dp returns a tuple: (number_of_valid_paths, total_waviness_sum)
            @cache
            def dp(idx: int, tight: bool, is_lz: bool, prev_d: int, prev_prev_d: int) -> tuple[int, int]:
                # Reached the end of the digit string
                if idx == len(s):
                    return (1, 0)
                    
                limit = int(s[idx]) if tight else 9
                total_ways = 0
                total_wave = 0
                
                for d in range(limit + 1):
                    new_tight = tight and (d == limit)
                    new_lz = is_lz and (d == 0)
                    
                    # Update history of digits to pass down to the next state
                    if new_lz:
                        nxt_prev = -1
                        nxt_prev_prev = -1
                    else:
                        nxt_prev = d
                        nxt_prev_prev = prev_d if not is_lz else -1
                        
                    # Recurse to process the next digit
                    ways, wave = dp(idx + 1, new_tight, new_lz, nxt_prev, nxt_prev_prev)
                    
                    # Check if the digit placed PREVIOUSLY forms a peak or valley
                    is_peak_or_valley = 0
                    if prev_prev_d != -1 and prev_d != -1 and not new_lz:
                        is_peak = prev_prev_d < prev_d and prev_d > d
                        is_valley = prev_prev_d > prev_d and prev_d < d
                        if is_peak or is_valley:
                            is_peak_or_valley = 1
                            
                    # Aggregate results
                    total_ways += ways
                    # The total waviness includes waviness from deeper branches PLUS 
                    # the waviness created right here, multiplied by the paths that contain it.
                    total_wave += wave + (is_peak_or_valley * ways)
                    
                return (total_ways, total_wave)
                
            # Start evaluating from index 0, bounded tightly by 'n', with leading zeros true
            return dp(0, True, True, -1, -1)[1]

        # The answer is the total waviness up to num2 minus the total waviness up to num1 - 1
        return count_waviness(num2) - count_waviness(num1 - 1)