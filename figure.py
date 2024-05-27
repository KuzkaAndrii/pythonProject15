from programobgect import *
class Truba(PObj):
    def __init__(self, fon, x, y, r, lx, ly, uvx, uvy, dvx, dvy):
        super().__init__(fon, x, y, r)
        self._lx=lx
        self._ly=ly
        self._uvx=uvx
        self._uvy=uvy
        self._dvx=dvx
        self._dvy=dvy
        self._obj=self._fon.create_polygon(self._lx+self._uvx, self._ly+self._uvy,
                                           self._x+self._uvx, self._y+self._uvy,
                                           self._x+self._dvx, self._y+self._dvy,
                                           self._lx+self._dvx, self._ly+self._dvy,
                                           fill="grey", tag="stvol")
if __name__=="__main__":
    print("figure")