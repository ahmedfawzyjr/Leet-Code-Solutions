class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        You are given a string s. You can convert s to a palindrome by adding characters in front of it.
        Return the shortest palindrome you can find by performing this transformation.

        The problem is equivalent to finding the longest palindromic prefix of s.
        Once we find the longest palindromic prefix, say s[0:i], the remaining suffix s[i:]
        needs to be reversed and prepended to s to form the shortest palindrome.

        We can use the KMP algorithm's preprocessing step (building the failure function / pi table)
        to find this efficiently.
        Construct a new string `temp = s + '#' + s[::-1]`.
        The last value of the KMP table for this string will give us the length of the longest
        palindromic prefix of s.
        """
        rev_s = s[::-1]
        temp = s + "#" + rev_s
        n = len(temp)
        pi = [0] * n
        
        for i in range(1, n):
            j = pi[i-1]
            while j > 0 and temp[i] != temp[j]:
                j = pi[j-1]
            if temp[i] == temp[j]:
                j += 1
            pi[i] = j
            
        longest_palindromic_prefix_len = pi[-1]
        suffix_to_add = rev_s[:len(s) - longest_palindromic_prefix_len]
        return suffix_to_add + s
