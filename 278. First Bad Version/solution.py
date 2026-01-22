# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    # Mocking the API for local testing
    bad_version = 4
    def isBadVersion(version: int) -> bool:
        return version >= bad_version

    s = Solution()
    n = 5
    result = s.firstBadVersion(n)
    print(f"n={n}, bad={bad_version}, result={result}, {'PASS' if result == bad_version else 'FAIL'}")

    bad_version = 1
    n = 1
    result = s.firstBadVersion(n)
    print(f"n={n}, bad={bad_version}, result={result}, {'PASS' if result == bad_version else 'FAIL'}")
