#file for testing out the algorithms for the coordinates of each chunk

import os
start = 7
values=[]
open('Srcipt_.tmp', 'w').close
f = open('prefabs\prefab_blanktile.txt', 'r+')

for i in range(5):
    values.append(f.readlines(start))
    start += 11

print(values)
    
