class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        The Nim game logic:
        If n is a multiple of 4, the first player will always lose if the second player plays optimally.
        For any other n, the first player can always make a move to leave a multiple of 4 stones 
        for the second player, eventually winning the game.
        """
        return n % 4 != 0
