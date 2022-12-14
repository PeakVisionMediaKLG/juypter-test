class Bruch:
    def __init__(self,zähler,nenner):
        if nenner==0:
            print("Kein gültiger Bruch!")
            return
        self.zähler=zähler
        self.nenner=nenner
        
    def __str__(self):
        if self.nenner==1:
            return f"{int(self.zähler)}"
        else:
            return f"Bruch:{self.zähler}/{self.nenner}"
    
    def __add__(self,other):
        new_nenner=self.nenner*other.nenner        
        self.zähler*=other.nenner       
        other.zähler*=self.nenner        
        new_zähler=self.zähler+other.zähler
        return Bruch.kürze(new_zähler,new_nenner)
    
    def __sub__(self,other):
        new_nenner=self.nenner*other.nenner        
        self.zähler*=other.nenner       
        other.zähler*=self.nenner        
        new_zähler=self.zähler-other.zähler 
        return Bruch.kürze(new_zähler,new_nenner)  
    
    def __mul__(self,other):
        new_nenner=self.nenner*other.nenner
        new_zähler=self.zähler*other.zähler
        return Bruch.kürze(new_zähler,new_nenner)
    
    def __truediv__(self,other):
        new_nenner=self.nenner*other.zähler
        new_zähler=self.zähler*other.nenner
        return Bruch.kürze(new_zähler,new_nenner)
    
    def kürze(z,n):        
        if z%n==0:
            return Bruch(int(z/n),int(n/n))
        else:
            div=2
            while True:
                if z%div==0 and n%div==0:
                    z=z/div
                    n=n/div
                else:
                    div+=1
                    if div>n//2+1:
                        break
            
            return Bruch(int(z),int(n))
                
        

