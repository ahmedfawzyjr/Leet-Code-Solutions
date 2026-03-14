class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count = 0
        self.result = ""
        
        def backtrack(current):
            if len(current) == n:
                self.count += 1
                if self.count == k:
                    self.result = current
                    return True
                return False
            
            for char in ['a', 'b', 'c']:
                if not current or current[-1] != char:
                    if backtrack(current + char):
                        return True
            return False

        backtrack("")
        return self.result
