class Solution:
    def findProductsOfElements(self, queries: list[list[int]]) -> list[int]:
        def count_set_bits_at_position(N, i):
            period = 1 << (i + 1)
            full = (N + 1) // period
            rem = (N + 1) % period
            return full * (1 << i) + max(0, rem - (1 << i))

        def total_count(N):
            if N <= 0:
                return 0
            ans = 0
            for i in range(60):
                ans += count_set_bits_at_position(N, i)
            return ans

        def total_exponent_sum(N):
            if N <= 0:
                return 0
            ans = 0
            for i in range(60):
                ans += i * count_set_bits_at_position(N, i)
            return ans

        def get_exponent_sum_prefix(K):
            if K <= 0:
                return 0
            # Binary search for N such that total_count(N) <= K
            low = 0
            high = K
            N = 0
            while low <= high:
                mid = (low + high) // 2
                if total_count(mid) <= K:
                    N = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            ans = total_exponent_sum(N)
            rem_len = K - total_count(N)
            if rem_len > 0:
                next_num = N + 1
                bit_idx = 0
                while rem_len > 0:
                    if (next_num >> bit_idx) & 1:
                        ans += bit_idx
                        rem_len -= 1
                    bit_idx += 1
            return ans

        res = []
        for from_i, to_i, mod_i in queries:
            exponent_sum = get_exponent_sum_prefix(to_i + 1) - get_exponent_sum_prefix(from_i)
            res.append(pow(2, exponent_sum, mod_i))
        return res
