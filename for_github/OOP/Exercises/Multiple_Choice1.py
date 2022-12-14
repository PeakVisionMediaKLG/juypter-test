

import pickle
class Student():
    
    
    def __init__(self,vorname,name):
        self.tests={}
        self.vorname=vorname
        self.name=name
    
    def mache_examen(self,test,answers):
        #print(test.fach,test.fragen)
        percent,how_many=0,len(answers)
        
        for index in range(len(test.fragen)):            
                if test.fragen[index]==answers[index] and index<len(answers):
                    percent+=100/how_many
        remark="Durchgefallen!" if percent<test.quote else "Bestanden!"
        self.tests[test.fach]=f" {remark}  ({percent:4.1f}%) "
        return 
    
    def übersicht_examen(self):
        if self.tests=={}:
            print( f"{self.vorname} , {self.name} noch kein Examen")
        else:
            print(f"{self.vorname} , {self.name} {self.tests}")
        return

class Examen ():
    instanzes=[]
    
    def __init__(self,fach,fragen,quote):
        self.fach=fach
        self.fragen=fragen
        self.quote=quote
        Examen.instanzes.append(self)
    
    
        

# Laden:
f = open('papers.pickle1','rb')
p = pickle.Unpickler(f)
Examen.instanzes=[]
while True:
    try:
        Examen.instanzes.append(p.load())
    except: 
        f.close()
        break
            
for i in range(len(Examen.instanzes)):
    print(i,Examen.instanzes[i].fach,Examen.instanzes[i].fragen,Examen.instanzes[i].quote)

########## neues Examen #################
# instanzes.append(Examen("Chemistry", ["1C", "2C", "3D", "4A"], 75))
# instanzes.append(Examen("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], 60))
# instanzes.append(Examen("Math", ["1C", "2C", "3A", "4B", "5A", "6C", "7B"], 75))


student1 = Student("Silvia","Meier")
student2 = Student("Klaus","Weber")       
        

student1.mache_examen(Examen.instanzes[0], ["1A", "2D", "3D", "4A", "5A"])
student1.übersicht_examen()# ➞ {"Chemistry" : "Durchgefallen! (40.0%)"}

student2.mache_examen(Examen.instanzes [1], ['1D', '2C', '3D', '4B', '5D', '6C', '7A'])
student2.mache_examen(Examen.instanzes[2], ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
student2.übersicht_examen()# ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}  

# Speichern:
 
f = open('papers.pickle1','wb') 
p = pickle.Pickler(f)
for instanz in Examen.instanzes:
    p.dump(instanz)
f.close()
# # print(globals()) 