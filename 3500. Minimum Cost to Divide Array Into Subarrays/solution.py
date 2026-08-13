from typing import List

class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        C = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]
            C[i + 1] = C[i] + cost[i]

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        ans = float('inf')

        # CHT helper for lines y = m_line * x + c_line
        # Slopes m_line = -C[l] are strictly decreasing
        # Query x = P[j] + m * k are strictly increasing
        for m in range(1, n + 1):
            next_dp = [float('inf')] * (n + 1)
            lines = []
            ptr = 0

            def add_line(m_line, c_line):
                line = (m_line, c_line)
                while len(lines) >= 2:
                    l1, l2 = lines[-2], lines[-1]
                    # Check if l2 is redundant
                    # Intersection of l1 and line <= Intersection of l1 and l2
                    # (line.c - l1.c) / (l1.m - line.m) <= (l2.c - l1.c) / (l1.m - l2.m)
                    if (c_line - l1[1]) * (l1[0] - l2[0]) <= (l2[1] - l1[1]) * (l1[0] - m_line):
                        lines.pop()
                    else:
                        break
                lines.append(line)

            def query(x):
                nonlocal ptr
                if not lines:
                    return float('inf')
                if ptr >= len(lines):
                    ptr = len(lines) - 1
                while ptr + 1 < len(lines):
                    y1 = lines[ptr][0] * x + lines[ptr][1]
                    y2 = lines[ptr + 1][0] * x + lines[ptr + 1][1]
                    if y2 <= y1:
                        ptr += 1
                    else:
                        break
                return lines[ptr][0] * x + lines[ptr][1]

            for j in range(m, n + 1):
                l = j - 1
                if dp[l] != float('inf'):
                    add_line(-C[l], dp[l])
                x = P[j] + m * k
                val = query(x)
                if val != float('inf'):
                    next_dp[j] = val + x * C[j]
            
            dp = next_dp
            ans = min(ans, dp[n])

        return ans
