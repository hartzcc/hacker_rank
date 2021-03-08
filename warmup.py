import datetime

def staircase(n):

    for i in range(1, n+1):
        print(' '*(n-i) + '#'*i)


staircase(6)

s = '07:05:45PM'
dt = datetime.datetime.strptime(s, "%I:%M:%S%p")
print(datetime.datetime.strftime(dt, "%H:%M:%S"))

def climbingLeaderboard(ranked, player):
    # Write your code here
    
    a = [*ranked, *player]
   
    newp = sorted(a, reverse=True)

    newr = [1]
    for i in range(1, len(newp)):
        if newp[i-1] == newp[i]:
            newr.append(newr[i-1])
        else: 
            newr.append(newr[i-1]+1)
    
    
            
    player_ranks = []
    for p in player:
        player_ranks.append(newr[newp.index(p)])
        
    return player_ranks

climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])

print('endK')

    
