from programobgect import *
from math import sin, cos

class Head(PObj):
    def __init__(self, fon, x, y, r):
        super().__init__(fon, x+0.5*r, y+r*0.005, r)
        self.truba=self._fon.create_polygon(self._x+0.75*self._r, self._y+self._r*0.025, self._x, self._y+self._r*0.03, self._x, self._y-self._r*0.025, self._x+0.75*self._r, self._y-self._r*0.025, fill="grey", tag="stvol")
        self.hole = self._fon.create_oval(self._x+0.7*self._r, self._y+self._r*0.025, self._x+0.8*self._r, self._y-self._r*0.025, fill="black", tag="stvol")
    def muve(self, ar):
        co=cos(-1*ar)
        si=sin(-1*ar)



class Turel(PObj):
    def __init__(self, fon, x, y, r):
        super().__init__(fon, x, y, r)
        self._stvol=Head(fon, x, y, r)
        self._ground=self._fon.create_arc(self._x, self._y, self._x + self._r, self._y + self._r, start=0, extent=180, fill="gray")
    def piw_paw(self):
        pass
    def muve(self):
        ar=1
        self._stvol.muve(ar)
if __name__=="__main__":
    print("turel")