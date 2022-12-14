class Roboter:
    def __init__(self,name,baujahr,energie):
        self.name=name
        self.baujahr=baujahr
        self.energie=energie
        self.alter=2021-self.baujahr
    
    def __befinden(self):
        if self.alter>20 and self.energie<50:
            return "In Anbetracht des Alters nicht schlecht"
        elif self.alter>20 and self.energie>=50:
            return "Super, vor allem in Anbetracht meines Alters"
        elif self.alter<20 and self.energie<50:
            return "Ausgelaugt"
        else:
            return "Super"
        

    
    p=property(__befinden)
x = Roboter("Hugo",1974,30)
print(x.p)
print(x.name)