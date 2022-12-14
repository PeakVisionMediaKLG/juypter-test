class plist:
    
    def __init__(self,value):
        self.value=value
        
        
    def __str__(self):
        
        return f" Liste: {self.value}"
    
    def splice(self,offset,length,other):        
        replacement=other.value
        res=self.value[:offset]
        res.extend(other.value)
        res.extend(self.value[offset+length:])         
        return plist(res)
    
l1=plist([1,2,3,4,5])    
print(l1)
l2=plist([-1,-2,-3])
print(l1.splice(2,2,l2))