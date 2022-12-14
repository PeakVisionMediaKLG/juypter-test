""" Modul Fibonnacci
Ein Modul zur Berechnung der Fibonacci-Zahlen
"""

def fib(n):
    """Berechnet den n-ten Fibonnaci-Wert
       Eingabe: n positive Integer
       Ausgabe: n-te Fibonacci-Zahl
    """
    if n == 0:
        return 0
    old, new = 0, 1
    for i in range(n-1):
        old, new = new, old + new
    return new

def rfib(n):
    """Berechnet den n-ten Fibonnaci-Wert rekursiv
       Eingabe: n positive Integer
       Ausgabe: n-te Fibonacci-Zahl
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rfib(n-1) + rfib(n-2)

def fiblist(n):
    """Berechnet die Liste der Fibonacci-Zahlen bis n"""
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]]
    return fib


if  __name__ == "__main__":
    print(fib(10))
    for i in range(5):
        print(fib(i) * 4)


