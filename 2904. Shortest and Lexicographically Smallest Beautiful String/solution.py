class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        one_positions = [index for index, character in enumerate(s) if character == "1"]
        best = ""

        for start in range(len(one_positions) - k + 1):
            left = one_positions[start]
            right = one_positions[start + k - 1]
            candidate = s[left:right + 1]

            if not best or len(candidate) < len(best) or (
                len(candidate) == len(best) and candidate < best
            ):
                best = candidate

        return best


if __name__ == "__main__":
    solution = Solution()
    assert solution.shortestBeautifulSubstring("100011001", 3) == "11001"
    assert solution.shortestBeautifulSubstring("1011", 2) == "11"
    assert solution.shortestBeautifulSubstring("000", 1) == ""