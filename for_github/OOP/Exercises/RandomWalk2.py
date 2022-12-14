
import random
class Betrunken():
    
    
    def __init__(self,x0,y0):
        self.x=x0
        self.y=y0
        #input()
        self.__startx=x0
        self.__starty=y0
        
    def walk(self):
        self.__x+=random.choice([-1,0,1])
        self.__y+=random.choice([-1,0,1])
        
    def Strecke(self):
        return ((self.__startx-self.x)**2 + (self.y-self.__starty)**2)**.5
    
    @property
    def x(self):
        print("x bekommen hier")
        return self.__x    
    @property
    def y(self):
        print("y bekommen hier")
        return self.__y
    @x.setter
    def x(self,x0):
        print(f"x gesetzt hier auf {x0}")   
        self.__x=x0
        return 
    @y.setter   
    def y(self,y0):
        print(f"y gesetzt hier auf {y0}\n") 
        self.__y=y0
        return 
        
    


steps=[10,20,50]   
inst=[] #instanzen
strecken_summe=[] #entfernung am Ende
results=[]
for number in steps:
      strecken_summe=[]
      for i in range(10):
          inst.append(Betrunken(random.randint(-10,10),random.randint(-10,10)))
         
          for _ in range(number):              
              inst[i].walk()
              
          #print(inst[i].get_koords_x(),number,strecken_summe)
          strecken_summe.append(inst[i].Strecke())
      results.append(max(strecken_summe))
print(results)
#inst[1].x+=5   # Achtung prints einschalten
