#fibonaci

class Fibonaci:
    def fibonaci(self):
        f0=0
        f1=1
        for i in range(20):
            f2=f0+f1
            print(f2)
            f0=f1
            f1=f2


fb=Fibonaci()
fb.fibonaci()