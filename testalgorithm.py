#file for testing out the algorithms for the coordinates of each chunk
import os
start = 6
looplist = '1'
values=[]#Values are all of the lines of a prefab that have the vertex coords
f = open('prefabs\prefab_blanktile.txt', 'r+')
lines = f.readlines() #gathers each line of the prefab and puts numbers them

strings = ('z3','z4','z5','z6') #keywords to search for

#for every line that has a keyword, add to a counter
for line in lines:
    if any(s in line for s in strings):
        looplist += '1'
#adds all the lines with coords to a list
print(looplist)
for i in range(len(looplist)-1):
    values.append(lines[start])
    start += 11
        
print(values) #just testing

    x6 = (posx*512)+512
    y6 = posy*512
    z6 = 0
    x7 = posx+posy
    y7 = posx+posy
    z7 = posx+posy
    x8 = (posx*512)+512
    y8 = posy*512
    z8 = 64
    
