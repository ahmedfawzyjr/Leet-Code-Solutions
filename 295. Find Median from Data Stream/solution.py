import heapq

class MedianFinder:

    def __init__(self):
        """
        Initialize the data structure.
        We use two heaps:
        1. small: A max-heap to store the smaller half of the numbers.
        2. large: A min-heap to store the larger half of the numbers.
        """
        # small stores the smaller half, max-heap (using negative values)
        self.small = []
        # large stores the larger half, min-heap
        self.large = []

    def addNum(self, num: int) -> None:
        """
        Adds a number into the data structure.
        """
        # Always push to small first, then move the largest of small to large
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Balance sizes: small can have at most one more element than large
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        """
        Returns the median of all elements so far.
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
