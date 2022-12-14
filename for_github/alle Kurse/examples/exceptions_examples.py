import sys

try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())

except IOError as err:
    (errno, strerror) = err.args
    print("I/O error({0}): {1}".format(errno, strerror))

except ValueError:
    print("No valid integer in line.")

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except (IOError, ValueError):
    print("An I/O error or a ValueError occurred")
except:
    print("An unexpected error occurred")
    raise