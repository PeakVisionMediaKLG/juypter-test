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
    
    

            

# Fahrplan = [(['Townsville', 'Suburbia', 'Urbantska'], '13:04'),
# (['Farmsdale', 'Suburbia', 'Lakeside Valley'], '13:20'),
# (['Suburbia', 'Townsville', 'Lakeside Valley'], '13:22')]
# f = open('Fahrplan.pickle','wb') 
# p=pickle.Pickler(f)
# p.dump(Fahrplan)
# f.close()


f = open('Fahrplan.pickle','rb') 
p = pickle.Unpickler(f)
Fahrplan=p.load()
f.close()
print(Fahrplan)
trains=[]
for index in range(len(Fahrplan)):    
    trains.append(Train(Fahrplan[index][0],Fahrplan[index][1]))


for t in trains:
    t.manage_delays( 'Farmsdale', 20)
		
trains[0].expected_time # 13:04
trains[1].expected_time # 13:40
trains[2].expected_time # 13:22


for t in trains:
    t.manage_delays( 'Townsville', 100)
 		
trains[0].expected_time # 14:44
trains[1].expected_time # 13:20
trains[2].expected_time # 15:02

