class R2D2:
    instanzes=[]
    def __init__(self,name,baujahr):
        self.name=name
        self.baujahr=baujahr
        R2D2.instanzes.append(self)
        

x=R2D2("Hugo",1982)
y=R2D2("Egon",1988)
for inst in R2D2.instanzes:
    if 2020 - inst.baujahr>10:
        print(f"  {inst.name} wurde gelöscht")
        del inst

