from turel import *
from plane import *
#from background import *
if __name__=="__main__":
    root=Tk()

    canvas=Canvas(root, width=600, height=500)
    canvas.pack()


    tur = Turel(canvas, 30, 180, 100)
    pl = Plain(canvas, 500, 50, 200)
    # fonn=Background(canvas)
    root.bind("w", lambda event: tur.muve(0.1))
    root.bind("s", lambda event: tur.muve(-0.1))
    root.mainloop()
    print("main")