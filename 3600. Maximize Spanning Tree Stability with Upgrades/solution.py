import bisect

class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        mandatory = []
        optional = []
        
        limit = float('inf')
        for u, v, s, m in edges:
            if m == 1:
                mandatory.append((u, v, s))
                if s < limit:
                    limit = s
            else:
                optional.append((u, v, s))
        
        # dsu_find function (iterative with path compression)
        def get_root(i, p):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != root:
                nxt = p[i]
                p[i] = root
                i = nxt
            return root

        # Check mandatory cycles and initial connectivity
        parent = list(range(n))
        init_comp = n
        for u, v, s in mandatory:
            ru = get_root(u, parent)
            rv = get_root(v, parent)
            if ru == rv:
                return -1 # Mandatory cycle
            parent[ru] = rv
            init_comp -= 1
            
        # Check if connected at all with all edges
        full_parent = parent[:]
        full_comp = init_comp
        for u, v, s in optional:
            ru = get_root(u, full_parent)
            rv = get_root(v, full_parent)
            if ru != rv:
                full_parent[ru] = rv
                full_comp -= 1
        if full_comp > 1:
            return -1 # Graph disconnected

        # Sort optional edges by strength for efficient slicing in check(X)
        optional.sort(key=lambda x: x[2])
        opt_u = [x[0] for x in optional]
        opt_v = [x[1] for x in optional]
        opt_s = [x[2] for x in optional]
        n_opt = len(optional)

        # Possible values of X
        # Stability can't exceed min mandatory strength (if any)
        vals = set()
        for u, v, s, m in edges:
            if s <= limit:
                vals.add(s)
            if m == 0 and 2 * s <= limit:
                vals.add(2 * s)
        
        # If no mandatory edges, limit remains inf, so all s and 2s are added.
        sorted_vals = sorted(list(vals))
        
        def check(X):
            curr_parent = parent[:]
            curr_comp = init_comp
            
            # Type A: optional edges that already have strength >= X
            idx1 = bisect.bisect_left(opt_s, X)
            for i in range(idx1, n_opt):
                u, v = opt_u[i], opt_v[i]
                ru = get_root(u, curr_parent)
                rv = get_root(v, curr_parent)
                if ru != rv:
                    curr_parent[ru] = rv
                    curr_comp -= 1
            
            if curr_comp == 1:
                return True
                
            # Type B: optional edges that can reach strength >= X by upgrading (s < X <= 2s)
            # 2s >= X  => s >= (X + 1) // 2
            idx2 = bisect.bisect_left(opt_s, (X + 1) // 2)
            upgrades_used = 0
            for i in range(idx2, idx1):
                u, v = opt_u[i], opt_v[i]
                ru = get_root(u, curr_parent)
                rv = get_root(v, curr_parent)
                if ru != rv:
                    curr_parent[ru] = rv
                    curr_comp -= 1
                    upgrades_used += 1
                    if upgrades_used > k:
                        return False
            
            return curr_comp == 1

        ans = -1
        l, r = 0, len(sorted_vals) - 1
        while l <= r:
            mid = (l + r) // 2
            if check(sorted_vals[mid]):
                ans = sorted_vals[mid]
                l = mid + 1
            else:
                r = mid - 1
        
        return ans

# Testing with examples
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxStability(3, [[0,1,2,1], [1,2,3,0]], 1)) # Output: 2
    print(sol.maxStability(3, [[0,1,4,0], [1,2,3,0], [0,2,1,0]], 2)) # Output: 6
    print(sol.maxStability(3, [[0,1,1,1], [1,2,1,1], [2,0,1,1]], 0)) # Output: -1
