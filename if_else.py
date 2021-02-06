if __name__ == '__main__':
    #n = int(input().strip())
    numbers = range(100)

for n in numbers:
    if n%2 == 1: # n is odd
        print('Weird')
    else:
        if n >= 2 and n <= 5: print('Not Weird')
        if n >= 6 and n <= 20: print('Weird')
        if n > 20: print('Not Weird')