import random
from fractions import Fraction
from itertools import product
from itertools import permutations
from itertools import combinations

def num1 (d_size=6):
    d1 = range(1, d_size + 1)
    d2 = range(1, d_size + 1)
    denom = d_size * d_size

    cp_itr = product(d1, d2)

    ctr = 0
    for cp in cp_itr:
        if cp[0] != cp[1] and cp[0] + cp[1] == 6:
            ctr += 1

    print(f'{ctr} / {denom}')
    print(Fraction(ctr, denom))

def num2():
    x = ['r']*4 + ['b']*3
    y = ['r']*5 + ['b']*4
    z = ['r']*4 + ['b']*4

    p_itr = product(x, y, z)
    denom = len(x) * len(y) * len(z)

    ctr = 0
    for p in p_itr:
        if p.count('r') == 2 and p.count('b') == 1:
            ctr +=1
    print(f'{ctr} / {denom}')
    print(Fraction(ctr, denom))

def num3():
    x = ['r']*4 + ['b']*5
    y = ['r']*3 + ['b']*7

    y_choose_2 = permutations(y, 2)
    p_itr = product(x, y_choose_2)

    denom = len(x) * len(y_choose_2)

    ctr = 0
    for p in p_itr:
        if p.count('r') == 1 and p.count('b') == 2:
            ctr +=1
    print(f'{ctr} / {denom}')
    print(Fraction(ctr, denom))
    print('break')        
    
num3()

print('end')

