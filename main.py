from background import *
from turel import *
if __name__=="__main__":
    root=Tk()
    canvas=Canvas(root, width=600, height=500)
    canvas.pack()
    #canvas.create_line(20, 20, 100, 20)
    #canvas.create_line(20, 20, 20, 200)
    fonn = Background(canvas)
    lab=Label(root, text="shooted: 0")
    lab.pack()
    gr=GameRule(canvas, 200, lab)

    tur = Turel(canvas, 30, 360, 100, 0.0, 10, gr)



    root.bind("w", lambda event: tur.muve(0.1))
    root.bind("s", lambda event: tur.muve(-0.1))
    root.bind("<Up>", lambda event: tur.muve(0.1))
    root.bind("<Down>", lambda event: tur.muve(-0.1))

    root.bind("<space>", lambda event: tur.piw_paw())
    root.bind("q", lambda event: tur.piw_paw())
    root.mainloop()
    print("main")