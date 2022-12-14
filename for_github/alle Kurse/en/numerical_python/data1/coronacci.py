k = 3.2
lst = [1, 1, 1, 1, 1]

k = 5
for i in range(30):
    lst.append(lst[-5]*3.2 + lst[-1])

print(lst)
