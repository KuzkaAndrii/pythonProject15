from turel import *
from math import sin, cos
def event_crash(b, p):
    line1=(b._x-p._x)+3*(b._y-p._y)<=0
    line2=b._x<=p._x+p._r*0.3
    line3=(b._x-p._x)-3*(b._y-p._y)>=0
    return line1 and line2 and line3
class Ball(PObj):
    def __init__(self, fon, x, y, r, aim):
        super().__init__(fon, x, y, r)
        self._aim=aim
        self._obj=self._fon.create_oval(self._x-0.025*r, self._y+0.025*r, self._x+0.025*r, self._y-0.025*r, fill="red")
    def move(self, fi):
        c, s=5*cos(fi), 5*sin(fi)
        self._fon.after(1, self.Move, self._obj, c, s)
    def Move(self, o, c, s):
        self._fon.move(o,c,s)
        self._x = self._x + c
        self._y = self._y + s
        if event_crash(self, self._aim):
            self._aim._dam=True
            self._aim.repid(self._aim)
            self._fon.delete(self._obj)
            del self
            return
        self._fon.after(30, self.Move, o, c, s)
if __name__=="__main__":
    print("boll")