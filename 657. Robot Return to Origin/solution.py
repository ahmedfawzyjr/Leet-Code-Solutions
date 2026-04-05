class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        :type moves: str
        :rtype: bool
        """
        # A robot ends up at (0, 0) if the number of U's equals number of D's
        # and the number of L's equals number of R's.
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
