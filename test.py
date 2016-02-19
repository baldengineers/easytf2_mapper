import os

def createTile(posx, posy, id_num, world_id_num):
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
    f = open('prefab_template/test.txt', 'r+')
    lines = f.readlines() #gathers each line of the prefab and puts numbers them
    x1 = posx*512
    y1 = posy*-512
    z1 = 64
    x2 = posx*512 + (512)
    y2 = posy*-512
    z2 = 64
    x3 = posx*512 + (512)
    y3 = posy*-512 + (-512)
    z3 = 64
    x4 = posx*512
    y4 = posy*-512 + (-512)
    z4 = 0
    x5 = posx*512 + (512)
    y5 = posy*-512 + (-512)
    z5 = 0
    x6 = posx*512 + (512)
    y6 = posy*-512
    z6 = 0
    x7 = posx*512
    y7 = posy*-512
    z7 = 64
    x8 = posx*512
    y8 = posy*-512 + (-512)
    z8 = 64
    x9 = posx*512
    y9 = posy*-512 + (-512)
    z9 = 0
    x10 = posx*512 + (512)
    y10 = posy*-512
    z10 = 0
    x11 = posx*512 + (512)
    y11 = posy*-512 + (-512)
    z11 = 0
    x12 = posx*512 + (512)
    y12 = posy*-512 + (-512)
    z12 = 64
    x13 = posx*512 + (512)
    y13 = posy*-512
    z13 = 64
    x14 = posx*512
    y14 = posy*-512
    z14 = 64
    x15 = posx*512
    y15 = posy*-512
    z15 = 0
    x16 = posx*512 + (512)
    y16 = posy*-512 + (-512)
    z16 = 0
    x17 = posx*512
    y17 = posy*-512 + (-512)
    z17 = 0
    x18 = posx*512
    y18 = posy*-512 + (-512)
    z18 = 64
    var_count = 18
    values = "".join(lines)#converting list to string
    ogvalues = "".join(lines)
    
    for i in range(ogvalues.count("world_idnum")):
        values = values.replace('world_idnum', str(world_id_num), 1)
        world_id_num += 1
    
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
  
    return values, id_num, world_id_num