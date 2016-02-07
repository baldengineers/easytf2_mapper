#file for testing out the algorithms for the coordinates of each chunk
import os
from array import array
posx = -1
posy = 1
start = 6
looplist = '1'
values=[]#Values are all of the lines of a prefab that have the vertex coords
f = open('prefabs\prefab_blanktile.txt', 'r+')
lines = f.readlines() #gathers each line of the prefab and puts numbers them

stringsz = ['z1','z2','z3','z4','z5','z6','z8'] #keywords to search for
stringsx = ['x1','x2','x3','x4','x5','x6','x8']
stringsy = ['y1','y2','y3','y4','y5','y6','y8']

for line in lines:
    if any(s in line for s in stringsz):
        looplist += '1'
#adds all the lines with coords to a list
print(looplist)
for i in range(len(looplist)-1):
    values.append(lines[start])
    start += 11
    
print(values) #just testing
x1 = (posx*512)+512
y1 = (posy*512)-512
z1 = 64
x2 = posx*512
y2 = (posy*512)-512
z2 = 64
x3 = posx*512
y3 = posy*512
z3 = 64
x4 = posx*512
y4 = (posy*512)-512
z4 = 0
x5 = posx*512
y5 = posy*512
z5 = 0
x6 = (posx*512)+512
y6 = posy*512
z6 = 0
x7 = posx+posy
y7 = posx+posy
z7 = posx+posy
x8 = (posx*512)+512
y8 = posy*512
z8 = 64

values = "".join(lines)#converting list to string

values.replace('x1',str(x1))
values.replace('x2',str(x2))
values.replace('x3',str(x3))
values.replace('x4',str(x4))
values.replace('x5',str(x5))
values.replace('x6',str(x6))
values.replace('x7',str(x7))
values.replace('x8',str(x8))
values.replace('y1',str(y1))
values.replace('y2',str(y2))
values.replace('y3',str(y3))
values.replace('y4',str(y4))
values.replace('y5',str(y5))
values.replace('y6',str(y6))
values.replace('y7',str(y7))
values.replace('y8',str(y8))
values.replace('z1',str(z1))
values.replace('z2',str(z2))
values.replace('z3',str(z3))
values.replace('z4',str(z4))
values.replace('z5',str(z5))
values.replace('z6',str(z6))
values.replace('z7',str(z7))
values.replace('z8',str(z8))



print(values)

           
        
