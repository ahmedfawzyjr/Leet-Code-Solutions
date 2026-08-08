from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        """
        Finds the lexicographically smallest sequence of indices in word1 of length len(word2)
        such that the formed string is almost equal to word2 (at most 1 mismatch).

        Complexity:
        - Time: O(N + M) where N = len(word1), M = len(word2).
        - Space: O(M) to store suffix matching positions and the answer array.
        """
        n, m = len(word1), len(word2)

        # last[j] stores the maximum index in word1 to match word2[j] 
        # such that suffix word2[j..m-1] matches word1[last[j]..n-1] with 0 mismatches.
        last = [-1] * m
        curr = n - 1
        for j in range(m - 1, -1, -1):
            while curr >= 0 and word1[curr] != word2[j]:
                curr -= 1
            if curr < 0:
                break
            last[j] = curr
            curr -= 1

        ans = []
        used_mismatch = False
        prev_i = -1

        for j in range(m):
            found = False
            for i in range(prev_i + 1, n):
                if word1[i] == word2[j]:
                    if not used_mismatch:
                        if j == m - 1 or last[j + 1] > i or j == m - 2 or last[j + 2] > i + 1:
                            found = True
                    else:
                        if j == m - 1 or last[j + 1] > i:
                            found = True
                else:
                    if not used_mismatch:
                        if j == m - 1 or last[j + 1] > i:
                            found = True
                            used_mismatch = True

                if found:
                    ans.append(i)
                    prev_i = i
                    break

            if not found:
                return []

        return ans
