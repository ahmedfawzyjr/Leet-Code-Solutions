# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # Generate a number between 1 and 49
            num = (rand7() - 1) * 7 + rand7()
            # If the number is in the range [1, 40], we can map it to [1, 10]
            if num <= 40:
                return (num - 1) % 10 + 1
            
            # Optional: Optimization using remaining bits
            # num is in [41, 49], so we have 9 values (41-49)
            num = (num - 40 - 1) * 7 + rand7() # num is in [1, 63]
            if num <= 60:
                return (num - 1) % 10 + 1
            
            # num is in [61, 63], so we have 3 values (61-63)
            num = (num - 60 - 1) * 7 + rand7() # num is in [1, 21]
            if num <= 20:
                return (num - 1) % 10 + 1
            # If we reach here (num = 21), we retry from the beginning
