from tkinter import *
class Background:
    def __init__(self, fon):
        self._fon=fon
        self._obj1=self._fon.create_polygon(0, 0, 600, 0, 600, 350, 0, 350, 0, 0, fill="blue")
        self._obj2=self._fon.create_polygon(0, 350, 600, 350, 600, 500, 0,500, fill="green")
if __name__=="main":
    print("background")