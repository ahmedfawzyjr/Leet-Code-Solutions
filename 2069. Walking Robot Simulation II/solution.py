class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.P = 2 * (width + height - 2)
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        if num > 0:
            self.moved = True
            self.pos = (self.pos + num) % self.P

    def getPos(self) -> list[int]:
        i = self.pos
        if 0 <= i <= self.w - 1:
            return [i, 0]
        elif self.w <= i <= self.w + self.h - 2:
            return [self.w - 1, i - (self.w - 1)]
        elif self.w + self.h - 1 <= i <= 2 * self.w + self.h - 3:
            return [self.w - 1 - (i - (self.w + self.h - 2)), self.h - 1]
        else:
            return [0, self.h - 1 - (i - (2 * self.w + self.h - 3))]

    def getDir(self) -> str:
        i = self.pos
        if i == 0:
            return "South" if self.moved else "East"
        if 1 <= i <= self.w - 1:
            return "East"
        if self.w <= i <= self.w + self.h - 2:
            return "North"
        if self.w + self.h - 1 <= i <= 2 * self.w + self.h - 3:
            return "West"
        return "South"

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
