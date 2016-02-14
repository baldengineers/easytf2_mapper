#file for getting coords of a ground tile
import os

def createTile(posx, posy, id_num, world_id_num):
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
    f = open('prefabs\prefab_blanktile.txt', 'r+')
    lines = f.readlines() #gathers each line of the prefab and puts numbers them

    x1 = posx*512
    y1 = (posy*(-512))
    z1 = 64
    x2 = (posx*512)+512
    y2 = (posy*(-512))
    z2 = 64
    x3 = (posx*512)+512
    y3 = (posy*(-512))-512
    z3 = 64
    x4 = posx*512
    y4 = (posy*(-512))-512
    z4 = 0
    x5 = (posx*512)+512
    y5 = (posy*(-512))-512
    z5 = 0
    x6 = (posx*512)+512
    y6 = posy*(-512)
    z6 = 0
    x7 = posx*512
    y7 = (posy*(-512))-512
    z7 = 64
    x8 = posx*512
    y8 = posy*(-512)
    z8 = 0

    var_count = 8 #var_count stores the last variable "number." In this case it's 8 because z8
      
    values = "".join(lines)#converting list to string
    ogvalues = "".join(lines)
    values = values.replace('world_idnum', str(world_id_num))
    #world_id_num += 1
    
    for var in ["x", "y", "z"]:
        for count in range(1,var_count+1):
    
            values = values.replace(var + str(count),str(eval(var + str(count))))

    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        id_num = id_num+1
  
    return values
