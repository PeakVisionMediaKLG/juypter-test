

import pickle
class Student():
    
    
    def __init__(self,vorname,name):
        self.tests={}
        self.vorname=vorname
        self.name=name
    
    def mache_examen(self,test,answers):
        percent,how_many=0,len(answers)
        
        for index in range(len(test.fragen)):
            if index < len(test.fragen):
                if test.fragen[index]==answers[index]:
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
    
    
    def __init__(self,fach,fragen,quote):
        self.fach=fach
        self.fragen=fragen
        self.quote=quote
    
    
        

# Laden:
f = open('papers.pickle','rb')
p = pickle.Unpickler(f)
paper1 = p.load()
paper2 = p.load()
paper3 = p.load()
f.close() 
  
# paper1 = Examen("Maths", ["1A", "2C", "3D", "4A", "5A"], 60)
# paper2 = Examen("Chemistry", ["1C", "2C", "3D", "4A"], 75)
# paper3 = Examen("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], 60)

student1 = Student("Silvia","Meier")
student2 = Student("Klaus","Weber")       
print(paper1.fragen)        

student1.mache_examen(paper1, ["1A", "2D", "3D", "4A", "5A"])
student1.übersicht_examen()# ➞ {"Maths" : "Passed! (80%)"}

student2.mache_examen(paper2, ["1C", "2D", "3A", "4C"])
student2.mache_examen(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
student2.übersicht_examen()# ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}  

# Speichern:
 
# f = open('papers.pickle','wb') 
# p = pickle.Pickler(f)
# p.dump(paper1)
# p.dump(paper2)
# p.dump(paper3)
# f.close()
# print(globals()) 