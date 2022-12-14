

class Zug:
    def __init__(self,x,vmax):
        self.vmax=vmax
        self.x=x
    def  treffen(self,other):
        try:        
            zeit=(self.x-other.x)/(other.vmax-self.vmax)
        except:
            return "geht nicht"
        if zeit<0:
            return "geht nicht"
        else:
            stunden=int(zeit)
            minuten=int((zeit-stunden)*60)
            ort=self.x+self.vmax*zeit
            return f" Zeit: {stunden}:{minuten:02d} Ort: {ort:6.3f} km"
        
zug1=Zug(20,40)
zug2=Zug(30,40)
print(zug1.treffen(zug2))
