""" This module contains some interesting ....."""


shopping_list = [(3, 'bananas'), (2, 'bread'), (6, 'breadrolls'), 
                 (1, 'butter')]

prices = [2.39, 1.88, 2.67, 5.60]

#prices = dict(zip(shopping_list, prices))

def create_prices_dict(article_list):
    """ this function ..."""
    prices = {}
    for article in article_list:
        price = input("Wie ist der Preis von " + article + "? ")
        prices[article] = price
    return prices

def read_data(fname):
    """ 'read_data' reads in data file 'fname' assuming..
    """
    with open(fname, "r") as fh:
        d = {}
        for line in fh:
            res = line.split(",")
            if len(res) == 2:
                article, price = res
                d[article] = float(price)     
    return d

def go_shopping(shopping_list, prices, logfile):
    with open(logfile, "w") as fh:
        saldo = 0
        for quantity, article in shopping_list:
            p = prices[article]
            q = quantity
            fh.write(f"{q:3d} {article:10s}\t{p:6.2f}{p*q:6.2f}\n")
            saldo += p*q
    
    return saldo
            


prices = read_data("daten.txt")
res = go_shopping(shopping_list, prices, "kassenzettel.txt")
print("Du musst ", res, " zahlen!")