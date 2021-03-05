def staircase(n):

    output = ''
    for i in range(n):
        for j in range(n):
            if i < j:
                output += ' '
            else:
                output += '#'
    print(output)


staircase(6)



    
