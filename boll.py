from programobgect import *
from math import sin, cos
class Ball(PObj):
    def __init__(self, fon, x, y, r):
        super().__init__(fon, x, y, r)
        self._obj=self._fon.create_oval(self._x-0.025*r, self._y+0.025*r, self._x+0.25*r, self._y-0.025*r, fill="red")
    def move(self, fi):
        c, s=3*cos(fi), 3*sin(fi)
        self._fon.after(1, self.Move, self._obj, c, s)
        self._x = self._x + c
        self._y = self._y + s
    def Move(self, a, b, c):
        self._fon.move(a, b, c)
if __name__=="__main__":
    print("boll")