def abc():
    s = "abcdef"
    count = 0
    while True:
        i = (yield s[count % 6])
        if i:
            count = i
        else:
            count += 1

if __name__ == "__main__":
    x = abc()
    print(next(x))
    print(next(x))
    print(x.send(4))
    print(next(x))
