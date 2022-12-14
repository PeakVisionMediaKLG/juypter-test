def selections(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for ss in selections(items, n-1):
                if (not items[i] in ss):
                    yield [items[i]]+ss

print("6 out of 49")
i = 0
l = range(1,50)
for s in selections(l,6): 
    print(s)
    if i > 50:
        break
    else:
        i = i+1
