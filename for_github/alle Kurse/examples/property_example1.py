class P:

    def __init__(self,x):
        self.setX(x)

    def __getX(self):
        return self.__x

    def __setX(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(__getX, __setX)
    
p = P
p.x = 42
print(p.x)