import os
import math

def rotatePoint(centerPoint,point,angle):
    angle = math.radians(angle)
    temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
    return temp_point

def createTile(posx, posy, id_num, world_id_num, entity_num, placeholder_list, rotation, level):
    
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
    f = open('prefab_template/test.txt', 'r+')
    lines = f.readlines() #gathers each line of the prefab and puts numbers them
#INSERT_ROT_IF
    x1 = posx*1*512
    y1 = posy*-1*512
    z1 = level*512 + 64
    x2 = posx*1*512 + (512)
    y2 = posy*-1*512
    z2 = level*512 + 64
    x3 = posx*1*512 + (512)
    y3 = posy*-1*512 + (-512)
    z3 = level*512 + 64
    x4 = posx*1*512
    y4 = posy*-1*512 + (-512)
    z4 = level*512 + 0
    x5 = posx*1*512 + (512)
    y5 = posy*-1*512 + (-512)
    z5 = level*512 + 0
    x6 = posx*1*512 + (512)
    y6 = posy*-1*512
    z6 = level*512 + 0
    x7 = posx*1*512
    y7 = posy*-1*512
    z7 = level*512 + 64
    x8 = posx*1*512
    y8 = posy*-1*512 + (-512)
    z8 = level*512 + 64
    x9 = posx*1*512
    y9 = posy*-1*512 + (-512)
    z9 = level*512 + 0
    x10 = posx*1*512 + (512)
    y10 = posy*-1*512
    z10 = level*512 + 0
    x11 = posx*1*512 + (512)
    y11 = posy*-1*512 + (-512)
    z11 = level*512 + 0
    x12 = posx*1*512 + (512)
    y12 = posy*-1*512 + (-512)
    z12 = level*512 + 64
    x13 = posx*1*512 + (512)
    y13 = posy*-1*512
    z13 = level*512 + 64
    x14 = posx*1*512
    y14 = posy*-1*512
    z14 = level*512 + 64
    x15 = posx*1*512
    y15 = posy*-1*512
    z15 = level*512 + 0
    x16 = posx*1*512 + (512)
    y16 = posy*-1*512 + (-512)
    z16 = level*512 + 0
    x17 = posx*1*512
    y17 = posy*-1*512 + (-512)
    z17 = level*512 + 0
    x18 = posx*1*512
    y18 = posy*-1*512 + (-512)
    z18 = level*512 + 64
    x19 = posx*1*512 + (64)
    y19 = posy*-1*512 + (-64)
    z19 = level*512 + 128
    x20 = posx*1*512 + (448)
    y20 = posy*-1*512 + (-64)
    z20 = level*512 + 128
    x21 = posx*1*512 + (448)
    y21 = posy*-1*512 + (-448)
    z21 = level*512 + 128
    x22 = posx*1*512 + (64)
    y22 = posy*-1*512 + (-448)
    z22 = level*512 + 64
    x23 = posx*1*512 + (448)
    y23 = posy*-1*512 + (-448)
    z23 = level*512 + 64
    x24 = posx*1*512 + (448)
    y24 = posy*-1*512 + (-64)
    z24 = level*512 + 64
    x25 = posx*1*512 + (64)
    y25 = posy*-1*512 + (-64)
    z25 = level*512 + 128
    x26 = posx*1*512 + (64)
    y26 = posy*-1*512 + (-448)
    z26 = level*512 + 128
    x27 = posx*1*512 + (64)
    y27 = posy*-1*512 + (-448)
    z27 = level*512 + 64
    x28 = posx*1*512 + (448)
    y28 = posy*-1*512 + (-64)
    z28 = level*512 + 64
    x29 = posx*1*512 + (448)
    y29 = posy*-1*512 + (-448)
    z29 = level*512 + 64
    x30 = posx*1*512 + (448)
    y30 = posy*-1*512 + (-448)
    z30 = level*512 + 128
    x31 = posx*1*512 + (448)
    y31 = posy*-1*512 + (-64)
    z31 = level*512 + 128
    x32 = posx*1*512 + (64)
    y32 = posy*-1*512 + (-64)
    z32 = level*512 + 128
    x33 = posx*1*512 + (64)
    y33 = posy*-1*512 + (-64)
    z33 = level*512 + 64
    x34 = posx*1*512 + (448)
    y34 = posy*-1*512 + (-448)
    z34 = level*512 + 64
    x35 = posx*1*512 + (64)
    y35 = posy*-1*512 + (-448)
    z35 = level*512 + 64
    x36 = posx*1*512 + (64)
    y36 = posy*-1*512 + (-448)
    z36 = level*512 + 128
    x37 = posx*1*512 + (128)
    y37 = posy*-1*512 + (-128)
    z37 = level*512 + 192
    x38 = posx*1*512 + (384)
    y38 = posy*-1*512 + (-128)
    z38 = level*512 + 192
    x39 = posx*1*512 + (384)
    y39 = posy*-1*512 + (-384)
    z39 = level*512 + 192
    x40 = posx*1*512 + (128)
    y40 = posy*-1*512 + (-384)
    z40 = level*512 + 128
    x41 = posx*1*512 + (384)
    y41 = posy*-1*512 + (-384)
    z41 = level*512 + 128
    x42 = posx*1*512 + (384)
    y42 = posy*-1*512 + (-128)
    z42 = level*512 + 128
    x43 = posx*1*512 + (128)
    y43 = posy*-1*512 + (-128)
    z43 = level*512 + 192
    x44 = posx*1*512 + (128)
    y44 = posy*-1*512 + (-384)
    z44 = level*512 + 192
    x45 = posx*1*512 + (128)
    y45 = posy*-1*512 + (-384)
    z45 = level*512 + 128
    x46 = posx*1*512 + (384)
    y46 = posy*-1*512 + (-128)
    z46 = level*512 + 128
    x47 = posx*1*512 + (384)
    y47 = posy*-1*512 + (-384)
    z47 = level*512 + 128
    x48 = posx*1*512 + (384)
    y48 = posy*-1*512 + (-384)
    z48 = level*512 + 192
    x49 = posx*1*512 + (384)
    y49 = posy*-1*512 + (-128)
    z49 = level*512 + 192
    x50 = posx*1*512 + (128)
    y50 = posy*-1*512 + (-128)
    z50 = level*512 + 192
    x51 = posx*1*512 + (128)
    y51 = posy*-1*512 + (-128)
    z51 = level*512 + 128
    x52 = posx*1*512 + (384)
    y52 = posy*-1*512 + (-384)
    z52 = level*512 + 128
    x53 = posx*1*512 + (128)
    y53 = posy*-1*512 + (-384)
    z53 = level*512 + 128
    x54 = posx*1*512 + (128)
    y54 = posy*-1*512 + (-384)
    z54 = level*512 + 192
    x55 = posx*1*512 + (192)
    y55 = posy*-1*512 + (-320)
    z55 = level*512 + 192
    x56 = posx*1*512 + (256)
    y56 = posy*-1*512 + (-256)
    z56 = level*512 + 448
    x57 = posx*1*512 + (320)
    y57 = posy*-1*512 + (-320)
    z57 = level*512 + 192
    x58 = posx*1*512 + (320)
    y58 = posy*-1*512 + (-192)
    z58 = level*512 + 192
    x59 = posx*1*512 + (192)
    y59 = posy*-1*512 + (-192)
    z59 = level*512 + 192
    x60 = posx*1*512 + (192)
    y60 = posy*-1*512 + (-320)
    z60 = level*512 + 192
    x61 = posx*1*512 + (192)
    y61 = posy*-1*512 + (-192)
    z61 = level*512 + 192
    x62 = posx*1*512 + (256)
    y62 = posy*-1*512 + (-256)
    z62 = level*512 + 448
    x63 = posx*1*512 + (192)
    y63 = posy*-1*512 + (-320)
    z63 = level*512 + 192
    x64 = posx*1*512 + (320)
    y64 = posy*-1*512 + (-192)
    z64 = level*512 + 192
    x65 = posx*1*512 + (320)
    y65 = posy*-1*512 + (-320)
    z65 = level*512 + 192
    x66 = posx*1*512 + (256)
    y66 = posy*-1*512 + (-256)
    z66 = level*512 + 448
    x67 = posx*1*512 + (320)
    y67 = posy*-1*512 + (-192)
    z67 = level*512 + 192
    x68 = posx*1*512 + (256)
    y68 = posy*-1*512 + (-256)
    z68 = level*512 + 448
    x69 = posx*1*512 + (192)
    y69 = posy*-1*512 + (-192)
    z69 = level*512 + 192
#INSERT_ROT_CODE

    var_count = 69
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
        if "ROTATION_RIGHT" in values:
            if rotation == 0:
                values = values.replace("ROTATION_RIGHT","0 0 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_RIGHT","0 270 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_RIGHT","0 180 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_RIGHT","0 90 0",1)
        if "ROTATION_UP" in values:
            if rotation == 0:
                values = values.replace("ROTATION_UP","0 90 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_UP","0 0 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_UP","0 270 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_UP","0 180 0",1)
        if "ROTATION_LEFT" in values:
            if rotation == 0:
                values = values.replace("ROTATION_LEFT","0 180 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_LEFT","0 90 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_LEFT","0 0 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_LEFT","0 270 0",1)
        if "ROTATION_DOWN" in values:
            if rotation == 0:
                values = values.replace("ROTATION_DOWN","0 270 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_DOWN","0 180 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_DOWN","0 90 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_DOWN","0 0 0",1)

    values = values.replace('"[0 0 0 1] 0.25"','"[1 1 1 1] 0.25"')
    values = values.replace('"[0 0 1 0] 0.25"','"[1 1 1 1] 0.25"')
    values = values.replace('"[0 1 0 0] 0.25"','"[1 1 1 1] 0.25"')       
    values = values.replace('"[1 0 0 0] 0.25"','"[1 1 1 1] 0.25"')
        
#INSERT_ENT_CODE

    return values, id_num, world_id_num