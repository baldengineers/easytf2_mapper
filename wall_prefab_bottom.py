import os

def createTile(posx, posy, id_num, world_id_num):
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
    f = open('prefab_template\\wall_prefab_bottom.txt', 'r+')
    lines = f.readlines() #gathers each line of the prefab and puts numbers them
    x1 = posx*512
    y1 = posy*-512 + (-448)
    z1 = 256
    x2 = posx*512 + (512)
    y2 = posy*-512 + (-448)
    z2 = 256
    x3 = posx*512 + (512)
    y3 = posy*-512 + (-512)
    z3 = 256
    x4 = posx*512
    y4 = posy*-512 + (-512)
    z4 = 64
    x5 = posx*512 + (512)
    y5 = posy*-512 + (-512)
    z5 = 64
    x6 = posx*512 + (512)
    y6 = posy*-512 + (-448)
    z6 = 64
    x7 = posx*512
    y7 = posy*-512 + (-448)
    z7 = 256
    x8 = posx*512
    y8 = posy*-512 + (-512)
    z8 = 256
    x9 = posx*512
    y9 = posy*-512 + (-512)
    z9 = 64
    x10 = posx*512 + (512)
    y10 = posy*-512 + (-448)
    z10 = 64
    x11 = posx*512 + (512)
    y11 = posy*-512 + (-512)
    z11 = 64
    x12 = posx*512 + (512)
    y12 = posy*-512 + (-512)
    z12 = 256
    x13 = posx*512 + (512)
    y13 = posy*-512 + (-448)
    z13 = 256
    x14 = posx*512
    y14 = posy*-512 + (-448)
    z14 = 256
    x15 = posx*512
    y15 = posy*-512 + (-448)
    z15 = 64
    x16 = posx*512 + (512)
    y16 = posy*-512 + (-512)
    z16 = 64
    x17 = posx*512
    y17 = posy*-512 + (-512)
    z17 = 64
    x18 = posx*512
    y18 = posy*-512 + (-512)
    z18 = 256
    var_count = 18
    values = "".join(lines)#converting list to string
    ogvalues = "".join(lines)
    values = values.replace('world_idnum', str(world_id_num))
    #world_id_num += 1
    
    for var in ["x", "y", "z"]:
        for count in range(1,var_count+1):
            string = var + str(count)
            string_var = str(eval(var + str(count)))

            if var == "z":
                values = values.replace(string + ")",string_var + ")") #we need to do this or else it will mess up on 2 digit numbers
            else:
                values = values.replace(string + " ",string_var + " ")

    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        id_num = id_num+1
  
    return values