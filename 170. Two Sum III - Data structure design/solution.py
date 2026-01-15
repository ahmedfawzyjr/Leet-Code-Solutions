class TwoSum:

    def __init__(self):
        self.nums = {}

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value: int) -> bool:
        for num in self.nums:
            complement = value - num
            if complement in self.nums:
                if complement != num or self.nums[num] > 1:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

if __name__ == "__main__":
    # Example 1
    obj = TwoSum()
    obj.add(1)
    obj.add(3)
    obj.add(5)
    print(f"Find 4: {obj.find(4)}") # Expected: True
    print(f"Find 7: {obj.find(7)}") # Expected: False
    
    # Example 2
    obj2 = TwoSum()
    obj2.add(3)
    obj2.add(1)
    obj2.add(2)
    print(f"Find 3: {obj2.find(3)}") # Expected: True
    print(f"Find 6: {obj2.find(6)}") # Expected: False
