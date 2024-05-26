from turel import *
from math import sin, cos
def event_crash(b, p):
    line1=(b._x-p._x)+3*(b._y-p._y)>=0
    line2=b._x<=p._x+p._r*0.3
    line3=(b._x-p._x)-3*(b._y-p._y)>=0
    if line1 and line2 and line3:
        if b._y<=p._y-0.1*p._r:
            return False
        else:
            return True
class Ball(PObj):
    def __init__(self, fon, x, y, r, aim, fi):
        super().__init__(fon, x, y, r)
        self._c, self._s=10*cos(fi), 10*sin(fi)
        self._aim=aim
        self._obj=self._fon.create_oval(self._x-0.025*r, self._y+0.025*r, self._x+0.025*r, self._y-0.025*r, fill="red")
    def move(self):
        self._fon.move(self._obj, self._c, self._s)
        self._x = self._x + self._c
        self._y = self._y + self._s
        if self._y <= 0:
            self._fon.delete(self._obj)
            del self
            return
        elif event_crash(self, self._aim):
            self._aim._dam = True
            self._aim.repid(self._aim)
            self._fon.delete(self._obj)
            del self
            return
        return self._fon.after(30, self.move, )
if __name__=="__main__":
    print("boll")