# 1002. Find Common Characters

**Difficulty:** Easy  
**Topics:** Array, Hash Table, String

## Problem Description

Given a string array `words`, return *an array of all characters that show up in all strings within the* `words` *(including duplicates)*. You may return the answer in **any order**.

---

### Example 1:

**Input:** `words = ["bella","label","roller"]`  
**Output:** `["e","l","l"]`

### Example 2:

**Input:** `words = ["cool","lock","cook"]`  
**Output:** `["c","o"]`

---

### Constraints:

- $1 \le \text{words.length} \le 100$
- $1 \le \text{words}[i].\text{length} \le 100$
- `words[i]` consists of lowercase English letters.

---

## Solution Approach

To find all characters that appear in every word along with their exact duplicate counts:

1. **Multiset Intersection via Character Frequencies:**
   - Initialize a frequency counter `common` with the character frequencies of the first word (`words[0]`).
   - Iterate through each subsequent word in `words` and compute the multiset intersection (`&`), which retains the minimum count of each character:
     $$\text{common}[c] = \min(\text{common}[c], \text{count}(c, \text{word})) \quad \forall c \in ['a'..'z']$$
   - Characters not present in any word will drop to a count of `0`.

2. **Result Construction:**
   - Expand the resulting frequency map into a list of characters, where each character $c$ appears $\text{common}[c]$ times.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \times L)$, where $N$ is the number of words in `words` and $L$ is the maximum length of a string in `words`. Processing each string takes $\mathcal{O}(L)$ time and intersecting frequency maps takes $\mathcal{O}(\Sigma) = \mathcal{O}(26) = \mathcal{O}(1)$ time.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (or $\mathcal{O}(\Sigma)$ where $\Sigma = 26$) to store the character frequency counts.
