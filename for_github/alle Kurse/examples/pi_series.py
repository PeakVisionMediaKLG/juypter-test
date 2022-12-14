def pi_series():
	sum = 0
	i = 1.0; j = 1
	while True:
		sum = sum + j/i
		yield 4*sum
		i = i + 2; j = j * - 1

def firstn(g, n):
	for i in range(n):
		yield next(g)

print(list(firstn(pi_series(), 8)))

