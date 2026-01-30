import random

class Solution:
    def __init__(self, nums: list[int]):
        self.original = list(nums)
        self.array = nums

    def reset(self) -> list[int]:
        self.array = list(self.original)
        return self.array

    def shuffle(self) -> list[int]:
        # Fisher-Yates shuffle
        n = len(self.array)
        for i in range(n):
            j = random.randint(i, n - 1)
            self.array[i], self.array[j] = self.array[j], self.array[i]
        return self.array

if __name__ == "__main__":
    nums = [1, 2, 3]
    obj = Solution(nums)
    print(f"Original: {nums}")
    print(f"Shuffled: {obj.shuffle()}")
    print(f"Reset: {obj.reset()}")
    print(f"Shuffled again: {obj.shuffle()}")
