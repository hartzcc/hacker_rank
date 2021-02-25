#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    
    p_row, p_col = -1, -1
    m_row, m_col = -1, -1
    for key, row in enumerate(grid):
        col = row.find('p')
        if col != -1:
            p_row = key
            p_col = col
        col = row.find('m')
        if col != -1:
            m_row = key
            m_col = col
        
    while m_row != p_row and m_col != p_col:
        if m_col > p_col:
            m_col -= 1
            print('LEFT')
        if m_col < p_col:
            m_col += 1
            print('RIGHT')
        if m_row > p_row:
            m_row -= 1
            print('UP')
        if m_row < p_row:
            m_row += 1
            print('DOWN')


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)