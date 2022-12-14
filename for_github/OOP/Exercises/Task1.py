class Roboter(object):
    
    def __init__(self,name):
        if name == "Hugo":
            self.name="Marvin"
            print(f"Name wurde von 'Hugo' auf 'Marvin' geändert")
        else: 
            self.name=name

x=Roboter("Caliban")
print(x.name)
y=Roboter("Hugo")   
print(y.name)
