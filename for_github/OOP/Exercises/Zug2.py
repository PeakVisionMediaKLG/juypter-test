
class Zug:
    counter=0
    def __init__(self,x,vmax):
        self.vmax=vmax
        self.x=x
        Zug.counter+=1
    def  treffen(self,other):        
        zeit=(self.x-other.x)/(other.vmax-self.vmax)
        if zeit<0:
            return "geht nicht"
        else:
            stunden=int(zeit)
            minuten=int((zeit-stunden)*60)
            ort=self.x+self.vmax*zeit
            return f" Zeit: {stunden}:{minuten:02d} Ort: {ort:6.3f} km"
    def __del__(self):
        Zug.counter-=1
        
    def count():
        print(f"{Zug.counter} Züge")
        
zug1=Zug(20,40)
zug2=Zug(10,80)
print(zug1.treffen(zug2))
Zug.count()
zug3=Zug(34,23)
Zug.count()
del(zug1)
Zug.count()