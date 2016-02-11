import os

def createTile(posx, posy, id_num):
    looplist = 'a'
    f = open('prefabs\prefab_wall.txt', 'r+')
    lines = f.readlines()
      
    stringsz = ['z1','z2','z3','z4','z5','z6','z8']
      
    x1 = posx*512
    y1 = ((posy-1)*512)+64
    z1 = 256
    x2 = (posx*512)+512
    y2 = ((posy-1)*512)+64
    z2 = 256
    x3 = (posx*512)+512
    y3 = (posy-1)*512
    z3 = 256
    x4 = posx*512
    y4 = (posy-1)*512
    z4 = 64
    x5 = (posx*512)+512
    y5 = (posy*512)-512
    z5 = 64
    x6 = (posx*512)+512
    y6 = ((posy-1)*512)+64
    z6 = 64
    x7 = posx*512
    y7 = (posy-1)*512
    z7 = 256
    x8 = posx*512
    y8 = ((posy-1)*512)+64
    z8 = 64
      
    values = "".join(lines)#converting list to string
    ogvalues = "".join(lines)
      
    values = values.replace('x1',str(x1))
    values = values.replace('x2',str(x2))
    values = values.replace('x3',str(x3))
    values = values.replace('x4',str(x4))
    values = values.replace('x5',str(x5))
    values = values.replace('x6',str(x6))
    values = values.replace('x7',str(x7))
    values = values.replace('x8',str(x8))
    values = values.replace('y1',str(y1))
    values = values.replace('y2',str(y2))
    values = values.replace('y3',str(y3))
    values = values.replace('y4',str(y4)) #replacing the variables in the prefab with the values it will use
    values = values.replace('y5',str(y5))
    values = values.replace('y6',str(y6))
    values = values.replace('y7',str(y7))
    values = values.replace('y8',str(y8))
    values = values.replace('z1',str(z1))
    values = values.replace('z2',str(z2))
    values = values.replace('z3',str(z3))
    values = values.replace('z4',str(z4))
    values = values.replace('z5',str(z5))
    values = values.replace('z6',str(z6))
    values = values.replace('z7',str(z7))
    values = values.replace('z8',str(z8))

    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        #id_num += 1
  
    return values
