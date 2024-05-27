from programobgect import *
from random import randint
class Plain(PObj):
    def __init__(self, fon, x, y, r):
        self._genpos=x
        self._dam=False
        super().__init__(fon, x, y, r)
        self._speed=5
        self.go()
    def go(self):
        self._plane = self._fon.create_polygon(self._x, self._y, self._x + 0.3 * self._r, self._y - 0.1 * self._r,
                                               self._x + 0.3 * self._r, self._y + self._r * 0.1, self._x, self._y,
                                               fill="green")
        return self._fon.after(45, self.move,)
    def move(self):
        self._x-=self._speed
        self._fon.move(self._plane, -1*self._speed, 0)
        if self._x<=self._r*(-0.3) or self._dam==True:
            self._dam=False
            self.repid()
        return self._fon.after(45, self.move,)
    def repid(self):
        self._speed=randint(4, 8)
        y=randint(100, 300)
        self._fon.move(self._plane, abs(self._x - self._genpos), y-self._y)
        self._x = self._genpos
        self._y=y
if __name__=="__main__":
    print("plain")