import pickle

class Smoothie:
    ingr_dict={}
    # ingr_dict={"Erdbeeren":1.50,
    #            "Bananen":0.50,
    #            "Mangos":2.50,
    #            "Blaubeeren":1.00,
    #            "Himbeeren":1.00,
    #            "Äpfel":1.75,
    #            "Ananas":3.50, 
    #            }
    
    def __init__(self,inhaltsstoffe,name):
        self.inhaltsstoffe=inhaltsstoffe
        self.name=name
    
    def get_kosten(self):
        sum=0
        for stoff in self.inhaltsstoffe:            
            sum+=Smoothie.ingr_dict[stoff]
        return f" {round(sum,2):5.2f}"
    
    def get_preis(self):
        return f" {2.5*float(Smoothie.get_kosten(self)):5.2f}"
    
    def get_name(self):
        ing_list=[]
        for stoff in self.inhaltsstoffe:
            ing_list.append(stoff)
        res=" ".join(sorted(ing_list))
        return f" {res} sind in {self.name}"
            

## Laden:
f = open('inhaltsstoffe.pickle','rb')
p = pickle.Unpickler(f)
Smoothie.ingr_dict = p.load()
f.close() 
    


s1=Smoothie(["Bananen"],"BBKing")  
print(s1.inhaltsstoffe) 
print(s1.get_kosten())
print(s1.get_preis())
s2=Smoothie(["Himbeeren","Erdbeeren","Blaubeeren"],"All_Fruits")
print(s2.inhaltsstoffe)
print(s2.get_kosten())
print(s2.get_preis())
print(s2.get_name())



# ## Speichern:
 
# f = open('inhaltsstoffe.pickle','wb') 
# p = pickle.Pickler(f)
# p.dump(Smoothie.ingr_dict)
# f.close()
 


