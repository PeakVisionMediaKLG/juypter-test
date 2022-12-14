import pickle

class Train:
    
    def __init__(self,route,est):
        self.route=route
        self.est=est
        self.expected_time=est
        
    def manage_delays(self,block,amount):
                
        if block in self.route:
            hour,minute=self.est.split(":")            
            minute=int(minute)
            hour=int(hour)            
            minute+=amount
            if minute>=60:
                hour+=minute//60
                minute%=60
            print (f"{hour:02d}:{minute:02d}")
            return f"{hour:02d}:{minute:02d}"
        
        else:
            print(self.expected_time)
            return self.expected_time
    
    
dbfile = open('Fahrplan.pickle', 'rb')     
db = pickle.load(dbfile)
for plan in db:
    print(plan)
            
Schnunkel=Train(db[0][0],db[0][1])
print(Schnunkel.route)
print(Schnunkel.est)
Schnunkel.manage_delays("Suburbia",30)

