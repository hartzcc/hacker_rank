# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        if i < n: print(i**2)

