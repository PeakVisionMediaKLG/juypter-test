
import random
class Betrunken():
    
    
    def __init__(self):
        self.__x=0
        self.__y=0
        
    def walk(self):
        self.__x+=random.choice([-1,0,1])
        self.__y+=random.choice([-1,0,1])
        
    def Strecke(self):
        return (self.__x**2 + self.__y**2)**.5
    
    def get_koords(self):
        return self.__x,self.__y
    
steps=[10,20,50]   
inst=[] #instanzen
strecken_summe=[] #Entfernung am Ende
results=[]
for number in steps:
    strecken_summe=[]
    for i in range(10):
        inst.append(Betrunken())
        for j in range(number):
            inst[i].walk()
        #print(inst[i].get_koords(),number,strecken_summe)
        strecken_summe.append(inst[i].Strecke())
    results.append(max(strecken_summe))
print(results)   
