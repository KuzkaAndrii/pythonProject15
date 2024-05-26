from programobgect import *
class Plain(PObj):
    def __init__(self, fon, x, y, r):
        self._genpos=x
        self._dam=False
        super().__init__(fon, x, y, r)
        self._plane=self._fon.create_polygon(self._x, self._y, self._x+0.3*self._r, self._y-0.1*self._r, self._x+0.3*self._r, self._y+self._r*0.1, self._x, self._y, fill="green")
        self._fon.after(45, self.move, self._plane)
    def move(self, p):
        self._x-=5
        if self._x<=0 or self._dam==True:
            self._dam=False
            self.repid(p)
        self._fon.move(p, -5, 0)
        self._fon.after(45, self.move, p)
    def repid(self, p):
        self._fon.move(p, abs(self._x - self._genpos), 0)
        self._x = self._genpos
if __name__=="__main__":
    print("plain")