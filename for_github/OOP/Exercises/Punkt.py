class Punkt:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __str__(self):
        return f"Punkt (x,y) ({self.x},{self.y})"
        
    def __call__(self,otherx, othery):
        dist=((self.x-otherx)**2+(self.y-othery)**2)**.5
        print(f" Distanz zwischen x:{self.x} y:{self.y} und x:{otherx} y:{othery} ist {dist:4.2f}")
        
p1=Punkt(3,4)
p1(4,5)
print(p1)