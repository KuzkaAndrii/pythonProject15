from turel import *
from plane import *
def event_crash(b, p):
    line1=b._x+3*b._y-p._x-3*p._y<=0
    line2=b._y<=p._x+p._r*0.3
    line3=b._x-3*b._y-p._x+3*p_y<=0
    return line1 and line2 and line3
if __name__=="__main__":
    print("eve")