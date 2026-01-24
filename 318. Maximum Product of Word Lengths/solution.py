class Solution:
    def maxProduct(self, words: list[str]) -> int:
        masks = {}
        for word in words:
            mask = 0
            for char in word:
                mask |= (1 << (ord(char) - ord('a')))
            masks[mask] = max(masks.get(mask, 0), len(word))
        
        max_prod = 0
        mask_list = list(masks.keys())
        for i in range(len(mask_list)):
            for j in range(i + 1, len(mask_list)):
                if mask_list[i] & mask_list[j] == 0:
                    max_prod = max(max_prod, masks[mask_list[i]] * masks[mask_list[j]])
        
        return max_prod
