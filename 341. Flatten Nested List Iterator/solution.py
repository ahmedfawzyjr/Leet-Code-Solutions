# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       if value is None:
           self._list = []
           self._is_int = False
       elif isinstance(value, int):
           self._int = value
           self._is_int = True
       else:
           self._list = value
           self._is_int = False

   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
       return self._is_int

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
       return self._int if self._is_int else None

   def getList(self) -> ['NestedInteger']:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
       return self._list if not self._is_int else None

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Stack stores [list, index]
        self.stack = [[nestedList, 0]]
    
    def next(self) -> int:
        # hasNext() ensures the top of the stack is an integer
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            nestedList, i = self.stack[-1]
            if i == len(nestedList):
                self.stack.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                else:
                    self.stack[-1][1] += 1
                    self.stack.append([x.getList(), 0])
        return False

if __name__ == "__main__":
    # Helper to build NestedInteger from list
    def build_nested(l):
        res = []
        for x in l:
            if isinstance(x, int):
                res.append(NestedInteger(x))
            else:
                res.append(NestedInteger(build_nested(x)))
        return res

    # Example 1
    nestedList1 = build_nested([[1,1],2,[1,1]])
    i, v = NestedIterator(nestedList1), []
    while i.hasNext(): v.append(i.next())
    print(f"Example 1: {v}") # Expected: [1, 1, 2, 1, 1]
    
    # Example 2
    nestedList2 = build_nested([1,[4,[6]]])
    i, v = NestedIterator(nestedList2), []
    while i.hasNext(): v.append(i.next())
    print(f"Example 2: {v}") # Expected: [1, 4, 6]
