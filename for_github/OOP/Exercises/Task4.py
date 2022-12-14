class Caveint:
    def __init__(self,dezimal):
        self.cipher="" if dezimal<=0 else "I"*abs(dezimal)
         
    def __str__(self):
        if self.cipher:
            return "I"*len(self.cipher)
        else:
            return "Kein Strich"
    def __int__(self):
        print(self)
        if self!=None:
            return len(self.cipher)
        
    def __add__(self,other):
        if self.cipher and other.cipher:
            return Caveint(len(self.cipher)+len(other.cipher))
        elif self.cipher=="":
            return other
        else:
            return self
    
    def __sub__(self,other):
        if not other.cipher:
            return self        
        elif (len(self.cipher)-len(other.cipher))<=0:
            return Caveint(0)
        else:
             return Caveint(len(self.cipher)-len(other.cipher))

    def __mul__(self,other):
        if self.cipher and other.cipher:
            return Caveint(len(self.cipher)*len(other.cipher))
        return Caveint(0)
        
    def __truediv__(self,other):
        if self.cipher and other.cipher:
            return Caveint(len(self.cipher)//len(other.cipher))
        return Caveint(0)






x=Caveint(5)
#print(x)

y=Caveint(2)
print(x,y)
print(x-y)
print(x/y)
#print(d,int(d))
d=x/y
print(int(y))
print(int(d))