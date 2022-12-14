a = float(input("Please enter a number: "))

eps = 0.000001
x_n = 1
x_n_1 = 0.5

while abs(x_n - x_n_1) > eps:
    print(x_n, x_n_1)
    (x_n,x_n_1) = ((x_n_1 + a / x_n_1)/2.0, x_n)

print(x_n)

