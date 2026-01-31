class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_type = 1
        count = 9
        start = 1
        
        while n > digit_type * count:
            n -= digit_type * count
            digit_type += 1
            count *= 10
            start *= 10
            
        # The number is start + (n - 1) // digit_type
        num = start + (n - 1) // digit_type
        # The digit is the (n - 1) % digit_type-th digit of num
        return int(str(num)[(n - 1) % digit_type])
