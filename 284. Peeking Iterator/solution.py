# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure with the given iterator.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked_element = None
        if self.iterator.hasNext():
            self.peeked_element = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the array without moving the pointer.
        :rtype: int
        """
        return self.peeked_element

    def next(self):
        """
        Returns the next element in the array and moves the pointer.
        :rtype: int
        """
        res = self.peeked_element
        if self.iterator.hasNext():
            self.peeked_element = self.iterator.next()
        else:
            self.peeked_element = None
        return res

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.peeked_element is not None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
