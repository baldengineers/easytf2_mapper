#file for testing out the algorithms for the coordinates of each chunk

import os
start = 6
looplist = '1'
values=[]
open('Srcipt_.tmp', 'w').close()
f = open('prefabs\prefab_blanktile.txt', 'r+')
lines = f.readlines()

strings = ('z3','z4','z5','z6')

for line in lines:
    if any(s in line for s in strings):
        looplist += '1'

print(looplist)
for i in range(len(looplist)-1):
    values.append(lines[start])
    start += 11
        
print(values)

