K = float(input("Startkapital? "))
p = float(input("Zinsrate? "))
n = int(input("Anzahl Jahre? "))
# python2: raw_input statt input

i = 0
while (i < n):
    K +=  K * p / 100.0
    i += 1
    print(i)
print("Kapital nach " + str(n) + " Jahren: " + str(K))

