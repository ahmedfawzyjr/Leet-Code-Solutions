class Solution:
    """
    3704. Count No-Zero Pairs That Sum to N
    Difficulty: Hard

    A no-zero integer is a positive integer that does not contain the digit 0 in its decimal representation.
    Given an integer n, count the number of pairs (a, b) where:
    - a and b are no-zero integers.
    - a + b = n.

    Return an integer denoting the number of such pairs.
    """
    def countNozeroPairs(self, n: int) -> int:
        digits = []
        temp = n
        while temp > 0:
            digits.append(temp % 10)
            temp //= 10
        
        K = len(digits)
        # dp state: (carry, a_state, b_state) -> count
        # state: 0 = ACTIVE, 1 = FINISHED
        dp = {(0, 0, 0): 1}
        
        for i in range(K):
            D = digits[i]
            next_dp = {}
            for (carry, a_st, b_st), count in dp.items():
                # a choices: (v_a, next_a_st)
                if a_st == 1:
                    a_choices = [(0, 1)]
                else:
                    if i == 0:
                        a_choices = [(d, 0) for d in range(1, 10)]
                    else:
                        a_choices = [(0, 1)] + [(d, 0) for d in range(1, 10)]
                
                # b choices: (v_b, next_b_st)
                if b_st == 1:
                    b_choices = [(0, 1)]
                else:
                    if i == 0:
                        b_choices = [(d, 0) for d in range(1, 10)]
                    else:
                        b_choices = [(0, 1)] + [(d, 0) for d in range(1, 10)]
                
                for va, nxt_a in a_choices:
                    for vb, nxt_b in b_choices:
                        s = va + vb + carry
                        if s % 10 == D:
                            nxt_carry = s // 10
                            st = (nxt_carry, nxt_a, nxt_b)
                            next_dp[st] = next_dp.get(st, 0) + count
            dp = next_dp
        
        ans = 0
        for (carry, a_st, b_st), count in dp.items():
            if carry == 0:
                ans += count
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(f"n=2: {sol.countNozeroPairs(2)}")  # Expected: 1
    print(f"n=3: {sol.countNozeroPairs(3)}")  # Expected: 2
    print(f"n=11: {sol.countNozeroPairs(11)}")  # Expected: 8
