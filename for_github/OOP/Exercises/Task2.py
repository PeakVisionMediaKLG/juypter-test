class Roboter(object):
    
    def __init__(self,name,x,y,richtung):    
        self.name=name[:10]
        self.x=x
        self.y=y
        while richtung not in ["West","Ost","Süd","Nord"]:
            print("Diese Richtung gibt es nicht")
            richtung=input("Bitte Richtung angeben: ")
        self.richtung=richtung
        
    def move(self,distanz):
        richt_dict={"West":[-1,0],"Ost":[1,0],"Nord":[0,1],"Süd":[0,-1]}
        self.x+=distanz*richt_dict[self.richtung][0]
        self.y+=distanz*richt_dict[self.richtung][1]
        
    def change_orientierung(self,richtung):
        while richtung not in ["West","Ost","Süd","Nord"]:
            print("Diese Richtung gibt es nicht")
            richtung=input("Bitte Richtung angeben: ")
        self.richtung=richtung
        
        
        

x=Roboter("Calibanbanbabn",2,2,"Ost")
x.move(4)
print(x.name,x.x,x.y,x.richtung)
x.change_orientierung("G")
x.move(4)
print(x.name,x.x,x.y,x.richtung)
