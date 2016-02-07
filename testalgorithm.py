#file for testing out the algorithms for the coordinates of each chunk

import os
start = 6
values=[]
open('Srcipt_.tmp', 'w').close()
f = open('prefabs\prefab_blanktile.txt', 'r+')
lines = f.readlines()

for i in range(6):
    values.append(lines[start])
    start += 11
        
print(values)

