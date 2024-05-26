from programobgect import *
class Head(PObj):
    def __init__(self, fon, x, y, r):
        super().__init__(fon, x, y, r)
        self.truba=self._fon.create_polygon(x+1.25*r, y+r*0.03, x+0.5*r, y+r*0.03, x+0.5*r, y-r*0.02, x+1.25*r, y-r*0.02, fill="grey", tag="stvol")
        self.hole = self._fon.create_oval(x + 1.2 * r, y + r * 0.03, x + 1.3 * r, y - r * 0.02, fill="black", tag="stvol")
class Turel(PObj):
    def __init__(self, fon, x, y, r):
        super().__init__(fon, x, y, r)
        self._stvol=Head(fon, x, y, r)
        self._ground=self._fon.create_arc(self._x, self._y, self._x + self._r, self._y + self._r, start=0, extent=180, fill="gray")
    def piw_paw(self):
        pass
    def muve(self):
        pass
if __name__=="__main__":
    print("turel")