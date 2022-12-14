def subgenerator():
    yield 1
    yield 2
    return 42

def delegating_generator():
    x = yield from subgenerator()
    print("subgenerator returned: ", x)

for x in delegating_generator():
    print("value of x in loop: ", x)