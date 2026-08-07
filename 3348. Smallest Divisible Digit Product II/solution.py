class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Check prime factors of t (must only be 2, 3, 5, 7)
        temp_t = t
        counts = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in (2, 3, 5, 7):
            while temp_t % p == 0:
                counts[p] += 1
                temp_t //= p
        if temp_t > 1:
            return "-1"

        def min_digits(c2: int, c3: int, c5: int, c7: int) -> int:
            c2 = max(0, c2)
            c3 = max(0, c3)
            c5 = max(0, c5)
            c7 = max(0, c7)
            
            cnt = c5 + c7
            n9 = c3 // 2
            rem3 = c3 % 2
            n8 = c2 // 3
            rem2 = c2 % 3
            
            cnt += n9 + n8
            if rem3 == 1 and rem2 == 1:
                cnt += 1
            else:
                if rem3 == 1:
                    cnt += 1
                if rem2 > 0:
                    cnt += 1
            return cnt

        factors = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        def fill_suffix(rem_len: int, c2: int, c3: int, c5: int, c7: int) -> str:
            res = []
            for pos in range(rem_len):
                for d in range(1, 10):
                    fc2, fc3, fc5, fc7 = factors[d]
                    nc2 = max(0, c2 - fc2)
                    nc3 = max(0, c3 - fc3)
                    nc5 = max(0, c5 - fc5)
                    nc7 = max(0, c7 - fc7)
                    if min_digits(nc2, nc3, nc5, nc7) <= rem_len - 1 - pos:
                        res.append(str(d))
                        c2, c3, c5, c7 = nc2, nc3, nc5, nc7
                        break
            return "".join(res)

        N = len(num)
        
        # Check first zero position in num
        first_zero = N
        for idx, ch in enumerate(num):
            if ch == '0':
                first_zero = idx
                break

        # Calculate prefix counts up to first_zero
        prefix_c2 = [0] * (N + 1)
        prefix_c3 = [0] * (N + 1)
        prefix_c5 = [0] * (N + 1)
        prefix_c7 = [0] * (N + 1)

        for i in range(first_zero):
            d = int(num[i])
            fc2, fc3, fc5, fc7 = factors[d]
            prefix_c2[i + 1] = prefix_c2[i] + fc2
            prefix_c3[i + 1] = prefix_c3[i] + fc3
            prefix_c5[i + 1] = prefix_c5[i] + fc5
            prefix_c7[i + 1] = prefix_c7[i] + fc7

        # Case 1: num itself (if zero-free and length N matches)
        if first_zero == N:
            if (prefix_c2[N] >= counts[2] and 
                prefix_c3[N] >= counts[3] and 
                prefix_c5[N] >= counts[5] and 
                prefix_c7[N] >= counts[7]):
                return num

        # Try prefix matching of length i from min(N-1, first_zero) down to 0
        max_i = min(N - 1, first_zero)
        for i in range(max_i, -1, -1):
            cur_c2 = prefix_c2[i]
            cur_c3 = prefix_c3[i]
            cur_c5 = prefix_c5[i]
            cur_c7 = prefix_c7[i]

            start_d = int(num[i]) + 1
            rem_len = N - 1 - i

            for d in range(start_d, 10):
                fc2, fc3, fc5, fc7 = factors[d]
                req2 = max(0, counts[2] - cur_c2 - fc2)
                req3 = max(0, counts[3] - cur_c3 - fc3)
                req5 = max(0, counts[5] - cur_c5 - fc5)
                req7 = max(0, counts[7] - cur_c7 - fc7)

                if min_digits(req2, req3, req5, req7) <= rem_len:
                    prefix_str = num[:i] + str(d)
                    suffix_str = fill_suffix(rem_len, req2, req3, req5, req7)
                    return prefix_str + suffix_str

        # Case 2: Length > N
        target_len = max(N + 1, min_digits(counts[2], counts[3], counts[5], counts[7]))
        return fill_suffix(target_len, counts[2], counts[3], counts[5], counts[7])
