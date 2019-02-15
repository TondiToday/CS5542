from functools import reduce
# We will be using the XOR operation in python to find integer that appears once

def oddmanout(array):
    print(reduce(lambda i, j: int(i) ^ int(j), array))