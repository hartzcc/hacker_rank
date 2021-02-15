import numpy

if __name__ != 'main':
    
    inp = '1 2 3 4 5 6 7 8 9'
    inp = inp.split()
    arr = numpy.array(inp, dtype=int)
    arr = arr.reshape((3,3))

    print(arr)