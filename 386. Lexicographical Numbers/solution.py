class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res = []
        curr = 1
        for _ in range(n):
            res.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.lexicalOrder(13)) # Expected: [1,10,11,12,13,2,3,4,5,6,7,8,9]
    print(sol.lexicalOrder(2)) # Expected: [1, 2]
