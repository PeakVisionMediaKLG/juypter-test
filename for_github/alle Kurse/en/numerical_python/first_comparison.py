import numpy
import time

def trad_version():
    t1 = time.time()
    X = xrange(10000000)
    Y = xrange(10000000)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    return time.time() - t1


def numpy_version():
    t1 = time.time()
    X = numpy.arange(10000000)
    Y = numpy.arange(10000000)
    Z = X + Y
    return time.time() - t1


trad_vers = trad_version()
numpy_vers = numpy_version()

print(trad_vers, numpy_vers, trad_vers / numpy_vers)
