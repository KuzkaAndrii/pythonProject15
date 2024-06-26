from math import sin, cos, atan
from figure import *
from otherfunc import *
from boll import *
from time import *
class Head(PObj):
    def __init__(self, fon, x, y, r, h):
        super().__init__(fon, x+0.5*r, y+r*0.005, r)
        self.truba = Truba(fon, self._x, self._y, self._r, self._x+0.75*self._r, self._y, 0, self._r*0.025, 0, -1*self._r*0.025)
        self.h=h
    def muve(self, ar):
        if ar+self.h>=0.0 and ar+self.h<=1.5:
            co = cos(ar)
            si = sin(ar)
            nlx, nly = change(self.truba._lx - self.truba._x, self.truba._ly - self.truba._y, co, si)
            nlx, nly = nlx + self.truba._x, nly + self.truba._y
            uvx, uvy = change(self.truba._uvx, self.truba._uvy, co, si)
            dvx, dvy = change(self.truba._dvx, self.truba._dvy, co, si)
            h=self.h+ar
            self._fon.delete(self.truba._obj)
            self.truba.__init__(self.truba._fon, self.truba._x, self.truba._y, self.truba._r, nlx, nly, uvx, uvy, dvx, dvy)
            self.h=h
class Turel(PObj):
    def __init__(self, fon, x, y, r, h, bs, gr):
        super().__init__(fon, x, y, r)
        self._gr=gr
        self._stvol=Head(fon, x, y, r, h)
        self._ground=self._fon.create_arc(self._x, self._y, self._x + self._r, self._y + self._r, start=0, extent=180, fill="gray")
        self._bs = bs
        self._t = time()
        self._tlim = 0.1
    def piw_paw(self):
        tt=time()
        if float(tt-self._t)>=self._tlim:
            at = atan((self._stvol.truba._ly - self._stvol.truba._y) / (self._stvol.truba._lx - self._stvol.truba._x))
            ba = Ball(self._fon, self._stvol.truba._lx, self._stvol.truba._ly, self._r, at, self._bs, self._gr)
            self._t=tt
            return ba.move()
    def muve(self, ar):
        self._gr.check()
        self._stvol.muve(ar)
if __name__=="__main__":
    print("turel")