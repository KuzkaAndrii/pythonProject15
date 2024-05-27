from tkinter import *
from random import randint, random
class PObj:
    def __init__(self, fon, x, y, r):
        self._x = x
        self._y = y
        self._fon = fon
        self._r = r
class Plain(PObj):
    def __init__(self, fon, x, y, r, gr):
        self._dam=False
        self._gr=gr
        super().__init__(fon, x, y, r)
        self._speed=randint(4, 8)
        self.go()
    def go(self):
        self._plane = self._fon.create_polygon(self._x, self._y, self._x + 0.3 * self._r, self._y - 0.1 * self._r,
                                               self._x + 0.3 * self._r, self._y + self._r * 0.1, self._x, self._y,
                                               fill="green")
        return self._fon.after(45, self.move,)
    def move(self):
        self._x-=self._speed
        self._fon.move(self._plane, -1*self._speed, 0)
        if self._x<=self._r*(-0.3):
            self._fon.delete(self._plane)
            del self
            return
        return self._fon.after(45, self.move,)
class GameRule:
    def __init__(self, fon, r, lab):
        self._planelist=[]
        self._fon=fon
        self._r=r
        self._n=0
        self._lab=lab
    def event_crash(self, b, i):
        line1 = (b._x - self._planelist[i]._x) + 3 * (b._y - self._planelist[i]._y) >= 0
        line2 = b._x <= self._planelist[i]._x + self._planelist[i]._r * 0.3
        line3 = (b._x - self._planelist[i]._x) - 3 * (b._y - self._planelist[i]._y) >= 0
        if line1 and line2 and line3:
            if b._y <= self._planelist[i]._y - 0.1 * self._planelist[i]._r:
                return False
            else:
                b._fon.delete(self._planelist[i]._plane)
                del self._planelist[i]
                self._n+=1
                self._lab["text"]="shooted: "+str(self._n)
                return True
    def event_shooted(self, b):
        for i in range(len(self._planelist)):
            if self.event_crash(b, i):
                return True
        return False
    def planegen(self):
        res=int(4*random()+1)
        return self._fon.after(res, self.createplane(),)
    def createplane(self):
        self._planelist.append(Plain(self._fon, 600, randint(100, 275), self._r, self))
        return
    def check(self):
        if len(self._planelist)<=randint(1, 4):
            self.planegen()
        elif len(self._planelist)!=0:
            for i in range(len(self._planelist)):
                if self._planelist[i]._x < 0:
                    self._fon.delete(self._planelist[i]._plane)
                    del self._planelist[i]
                    break
        return

if __name__=="__main__":
    print("programobject")