from programobgect import *
class Plain(PObj):
    def __init__(self, fon, x, y, r):
        super().__init__(fon, x, y, r)
        self._plane=self._fon.create_polygon(self._x, self._y, self._x+0.3*self._r, self._y-0.1*self._r, self._x+0.3*self._r, self._y+self._r*0.1, self._x, self._y, fill="green")

if __name__=="__main__":
    print("plain")