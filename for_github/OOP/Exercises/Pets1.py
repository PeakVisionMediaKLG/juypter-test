class Pets:
    count_dict={"Hund":0,"Katze":0,"Papagei":0,"Fisch":0}
    
    def __init__(self,name):
        self.name=name
        print(type(self),type(self).__name__)
        Pets.count_dict[type(self).__name__]+=1
    def __del__(self):
        Pets.count_dict[type(self).__name__]-=1
    
    
    def show_counts():
        print(Pets.count_dict)
        
    def kompatibel(*args):
        not_komp_set=set()
        for inst in args:
            if type(inst).__name__ in not_komp_set: #der Klassenname wird überprüft, ob er in not_komp_set steht
                return  "Geht nicht!"
            for elem in inst.inkomp:
                not_komp_set.add(elem) #inkompatible Pets werden in all_not_komp_l aufgenommen
                 #print(not_komp_set)
        return "Alles oK!"
        
    
    
    def gib_name(self):
        print(self.name)

class Hund(Pets):
    inkomp=["Katze"]    
                

class Katze(Pets):
    inkomp=["Hund","Papagei","Fisch"]    
    

class Papagei(Pets):
    inkomp=["Katze","Hund"]    
    
class Fisch(Pets):
    inkomp=[]    
    


x=Hund("Bello")
y=Hund("Wuff")
z=Katze("miau")
Pets.show_counts()
print(Pets.kompatibel(x,y,z))
x.gib_name()



