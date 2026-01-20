from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # Rotate the queue so the new element is at the front (simulating stack top)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

# Test cases
if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(f"Top: {obj.top()}") # returns 2
    print(f"Pop: {obj.pop()}") # returns 2
    print(f"Empty: {obj.empty()}") # returns False
