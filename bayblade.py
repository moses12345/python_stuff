#10
#3 6 7 5 3 5 6 2 9 1
#2 7 0 9 3 6 0 6 2 6


#with current arrangement output 4
#optimal solution output 7 optimal winning arangement is :3 9 1 2 5 7 5 6 3 6
from itertools import permutations
g_force = [6,11,13]
opponent =[10,5,12]
wins=0
permu=permutations(g_force,len(g_force))

for x in list(permu):
    print(x)
    point=0
    for i,j in zip(x,opponent):
        if i>j:
            
            point+=1
    if wins < point:
        wins=point
                

print(wins)

#     print(i)