from turel import *
from math import sin, cos

class Ball(PObj):
    def __init__(self, fon, x, y, r, fi, sp, gr):
        super().__init__(fon, x, y, r)
        self._gr=gr
        self._gr.check()
        self._sp=sp
        self._c, self._s = self._sp * cos(fi), self._sp * sin(fi)
        self._obj=self._fon.create_oval(self._x-0.025*r, self._y+0.025*r, self._x+0.025*r, self._y-0.025*r, fill="red")
    def move(self):
        self._fon.move(self._obj, self._c, self._s)
        self._x = self._x + self._c
        self._y = self._y + self._s
        if self._y <= 0 or self._x>=600:
            self._fon.delete(self._obj)
            self._gr.check()
            del self
            return
        elif self._gr.event_shooted(self):
            self._gr.check()
            self._fon.delete(self._obj)
            del self
            return
        return self._fon.after(30, self.move, )
if __name__=="__main__":
    print("boll")