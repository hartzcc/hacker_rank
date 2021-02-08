# https://www.hackerrank.com/challenges/the-minion-game/problem

import time

if __name__ == '__main__':
    start = time.time()
    s  = "oisunpceoaiwecoinnocngaisjdhfijsahdibaiefbiajsbiashfiufhaijdbjkabsdkfjhaiuoisdhfkjnsekjnkdjvosidhfi"
    stuart = 0
    kevin = 0
    vowels = 'AEIOU'
    
    s_len = len(s)+1

    for i in range(s_len):
            if s[i] in vowels:
                 kevin += len(s) - i
            if s[i] not in vowels:
                stuart += 1 len(s) - i



    if stuart > kevin:
        print(f'Stuart {stuart}')
    if kevin > stuart:
        print(f'Kevin {kevin}')
    if stuart == kevin:
        print('Draw')
    end = time.time()
    print((end-start)*1000000) 
    
    

   