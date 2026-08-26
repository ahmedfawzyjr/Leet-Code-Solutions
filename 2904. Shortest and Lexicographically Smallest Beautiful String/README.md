# 2904. Shortest and Lexicographically Smallest Beautiful String

## Description

You are given a binary string `s` and a positive integer `k`.

A substring is **beautiful** if it contains exactly `k` occurrences of `1`.
Return the shortest beautiful substring. If several have the same length,
return the lexicographically smallest one. Return an empty string if no
beautiful substring exists.

## Examples

**Example 1:**

```text
Input: s = "100011001", k = 3
Output: "11001"
```

**Example 2:**

```text
Input: s = "1011", k = 2
Output: "11"
```

**Example 3:**

```text
Input: s = "000", k = 1
Output: ""
```

## Complexity

- Time: `O(n)`
- Space: `O(n)`