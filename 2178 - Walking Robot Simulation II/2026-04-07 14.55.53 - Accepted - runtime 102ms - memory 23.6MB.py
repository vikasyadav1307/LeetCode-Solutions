from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0  # 0=East, 1=North, 2=West, 3=South
        self.cycle = 2 * (width + height - 2)

    def step(self, num: int) -> None:
        num %= self.cycle
        
        # handle full cycle case
        if num == 0:
            num = self.cycle

        while num > 0:
            if self.dir == 0:  # East
                move = min(num, self.w - 1 - self.x)
                self.x += move
            elif self.dir == 1:  # North
                move = min(num, self.h - 1 - self.y)
                self.y += move
            elif self.dir == 2:  # West
                move = min(num, self.x)
                self.x -= move
            else:  # South
                move = min(num, self.y)
                self.y -= move

            num -= move

            # turn if cannot move further
            if move == 0:
                self.dir = (self.dir + 1) % 4

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return ["East", "North", "West", "South"][self.dir]