
import random
class Betrunken():
    
    
    def __init__(self,x0,y0):
        self.__set_koords_x(x0)
        self.__set_koords_y(y0)
        self.__startx=x0
        self.__starty=y0
        
    def walk(self):
        self.__x+=random.choice([-1,0,1])
        self.__y+=random.choice([-1,0,1])
        
    def Strecke(self):
        return ((self.__startx-self.__x)**2 + (self.__y-self.__starty)**2)**.5
    
    def __get_koords_x(self):
        return self.__x
    
    def __get_koords_y(self):
        return self.__y
    
    def __set_koords_x(self,x0):        
        self.__x=x0
        return self.__x
        
    def __set_koords_y(self,y0):
        self.__y=y0
        return self.__y
        
    x=property(__get_koords_x,__set_koords_x)
    y=property(__get_koords_y,__set_koords_y) 
    


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
