class Cc():
    
    faktoren={"EUR":1,"GBP":.85,"USD":1.13,"SFR":1.04}
    
    def __init__(self,betrag,währung):
        self.betrag=betrag
        self.währung=währung

    def __str__(self):
        return f"Betrag: {self.betrag:6.2f} in {self.währung}"

    def __repr__(self):
        return f"Cc({self.betrag},\"{str(self.währung)}\")"

    def convert(self,neue_währung):
        self.betrag=1/Cc.faktoren[self.währung]*self.betrag
        #print("Euro",self.betrag)
        self.betrag=Cc.faktoren[neue_währung]*self.betrag
        #print(self.betrag)
        return Cc(self.betrag,neue_währung)
        
    def __add__(self,other):
        if type(other)==float or type (other)==int:
            return Cc(self.betrag+Cc.faktoren[self.währung]*other,self.währung)
        self.betrag=self.convert()
        other.betrag=other.convert()
        return Cc(self.betrag+other.betrag,"EUR")
    
    def __radd__(self, other):
        res = self + other
        if self.währung!= "EUR":
            res.convert("EUR")
        return Cc(res.betrag,"EUR")


