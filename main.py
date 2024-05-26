from turel import *
#from background import *
if __name__=="__main__":
    root=Tk()
    canvas=Canvas(root, width=600, height=500)
    canvas.pack()
    f=Turel(canvas, 30, 180, 200)
    f.go()
    #fonn=Background(canvas)
    root.mainloop()
    print("main")