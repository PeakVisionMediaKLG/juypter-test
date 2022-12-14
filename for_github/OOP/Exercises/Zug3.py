

class Zug:
    count=0
    zugliste=[]
    def __init__(self,x,vmax,name):
        self.vmax=vmax
        self.x=x
        self.name=name
        Zug.count+=1
        Zug.zugliste.append(self)
                
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
            return f" {self.name} trifft {other.name} Zeit: {stunden}:{minuten:02d} Ort: {ort:6.3f} km"
    def __del__(self):
        Zug.count-=1
        
zug1=Zug(20,40,"Donauexpress")
zug2=Zug(30,40,"Alpenschleicher")
zug3=Zug(50,20,"Balkanpaprika")

for index1 in range(len(Zug.zugliste)):
    for index2 in range(index1,len(Zug.zugliste)):
        print(Zug.zugliste[index1].treffen(Zug.zugliste[index2]))