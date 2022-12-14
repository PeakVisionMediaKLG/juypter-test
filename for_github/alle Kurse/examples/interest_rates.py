K = float(input("Starting capital? "))
p = float(input("Interest rate? "))
n = int(input("Number of years? "))
# python2: raw_input instead of input

i = 0
while (i < n):
    K +=  K * p / 100.0
    i += 1
    print(i)
print("Capital after " + str(n) + " ys: " + str(K))

