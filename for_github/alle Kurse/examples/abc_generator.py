def abc():
    while True:
        yield("a")
        yield("b")
        yield("c")
        yield("d")
        yield("e")


def firstn(g, n):
	for i in range(n):
		yield next(g)

print(list(firstn(abc(), 8)))

