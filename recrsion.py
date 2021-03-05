# add 1 + 2 + 3 + n

def sums(n):
    if n == 0:
        return 0 # end case
    else:
        return(n + sums(n - 1))

# sum of x -> n   add (n^2 + n) /2
def power_sum(n, p):
    if n == 0:
        return 0
    else:
        return(n**p + power_sum(n - 1, 1))

def superDigit(n, k=1):

    number = str(n)
    total = 0
    for c in number:
        total += int(c)
            
    for _ in range(k-1):
        number += str(n)
    
    if len(number) < 10:
        return number
    else:
        return superDigit(str(total * k))
    

    print('end')