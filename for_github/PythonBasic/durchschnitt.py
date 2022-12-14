
def durchschnitt(*args):
    """Funktion zur berechnung des Durchschnitts, erwartet beliebig viele
    integer oder float als positionale Argumente
    gibt den Durchschitt als float aus"""
    
    result=0
    counter=0
    for arg in args:        
        result+=arg
        counter+=1
    return   result/counter 

if __name__=="__main__":
    print(f"Ergebnis {durchschnitt(1,2,3,4,5)}")
    help(durchschnitt)
