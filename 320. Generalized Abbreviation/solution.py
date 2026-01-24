class Solution:
    def generateAbbreviations(self, word: str) -> list[str]:
        res = []
        
        def backtrack(pos, current_str, count):
            if pos == len(word):
                if count > 0:
                    current_str += str(count)
                res.append(current_str)
                return
            
            # Option 1: Abbreviate current character
            backtrack(pos + 1, current_str, count + 1)
            
            # Option 2: Keep current character
            new_str = current_str
            if count > 0:
                new_str += str(count)
            new_str += word[pos]
            backtrack(pos + 1, new_str, 0)
            
        backtrack(0, "", 0)
        return res
