class Memories:
    
    
    
    def __init__(self):
        self.memories={}
        
    
    def remember(self,memory):
        
##        if memory in Memories.memories:
##            return f"Das war {self.memories[memory]}"
##        else:
##            return "Kenne ich nicht"
        
        return self.memories.get(memory,"Kenne ich nicht")
    def add(self,**kwargs):
        for key, value in kwargs.items():
            self.memories[key]=value
        return True
    

m=Memories()
m.add(Name="Petra",Auto="VW")
print(m.remember("Auto"))
m1=Memories()
m1.add(Name="Claudia",Kleidergrösse=40)
print(m1.remember("Kleidergrösse"))
print(m.remember("Name"))
print(m.remember("Bla"))
