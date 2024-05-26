from programobgect import *
from math import sin, cos
from eventfunc import *
class Ball(PObj):
    def __init__(self, fon, x, y, r):
        super().__init__(fon, x, y, r)
        self._obj=self._fon.create_oval(self._x-0.025*r, self._y+0.025*r, self._x+0.025*r, self._y-0.025*r, fill="red")
    def move(self, fi):
        c, s=5*cos(fi), 5*sin(fi)
        self._fon.after(1, self.Move, self._obj, c, s)
    def Move(self, o, c, s):
        self._fon.move(o,c,s)
        self._x = self._x + c
        self._y = self._y + s
        self._fon.after(30, self.Move, o, c, s)
if __name__=="__main__":
    print("boll")