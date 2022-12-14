def chain(*iterables):
    """ This generator is equivalent 
        to the chain
        method of iterables  """
    for iterable in iterables:
        yield from iterable

names1 = ["Pete", "Tom"]
names2 = ["Tom", "Oscar"]        
c = chain(names1, names2)
for el in c:
    print(el)
    
    
for _ in range(10):
    print("great")
    print(x[])