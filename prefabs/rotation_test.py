import os

def createTile(posx, posy, id_num, world_id_num, entity_num, placeholder_list, rotation):
    
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
    f = open('prefab_template/rotation_test.txt', 'r+')
    lines = f.readlines() #gathers each line of the prefab and puts numbers them

    if rotation == 0:

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
        x19 = posx*512 + (192)
        y19 = posy*-512 + (-192)
        z19 = 320
        x20 = posx*512 + (384)
        y20 = posy*-512 + (-192)
        z20 = 320
        x21 = posx*512 + (384)
        y21 = posy*-512 + (-320)
        z21 = 320
        x22 = posx*512 + (192)
        y22 = posy*-512 + (-320)
        z22 = 64
        x23 = posx*512 + (384)
        y23 = posy*-512 + (-320)
        z23 = 64
        x24 = posx*512 + (384)
        y24 = posy*-512 + (-192)
        z24 = 64
        x25 = posx*512 + (192)
        y25 = posy*-512 + (-192)
        z25 = 320
        x26 = posx*512 + (192)
        y26 = posy*-512 + (-320)
        z26 = 320
        x27 = posx*512 + (192)
        y27 = posy*-512 + (-320)
        z27 = 64
        x28 = posx*512 + (384)
        y28 = posy*-512 + (-192)
        z28 = 64
        x29 = posx*512 + (384)
        y29 = posy*-512 + (-320)
        z29 = 64
        x30 = posx*512 + (384)
        y30 = posy*-512 + (-320)
        z30 = 320
        x31 = posx*512 + (384)
        y31 = posy*-512 + (-192)
        z31 = 320
        x32 = posx*512 + (192)
        y32 = posy*-512 + (-192)
        z32 = 320
        x33 = posx*512 + (192)
        y33 = posy*-512 + (-192)
        z33 = 64
        x34 = posx*512 + (384)
        y34 = posy*-512 + (-320)
        z34 = 64
        x35 = posx*512 + (192)
        y35 = posy*-512 + (-320)
        z35 = 64
        x36 = posx*512 + (192)
        y36 = posy*-512 + (-320)
        z36 = 320
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
        x19 = posx*512 + (192) 
        y19 = posy*-512 + (-192) 
        z19 = 320
        x20 = posx*512 + (384) 
        y20 = posy*-512 + (-192) 
        z20 = 320
        x21 = posx*512 + (384) 
        y21 = posy*-512 + (-320) 
        z21 = 320
        x22 = posx*512 + (192) 
        y22 = posy*-512 + (-320) 
        z22 = 64
        x23 = posx*512 + (384) 
        y23 = posy*-512 + (-320) 
        z23 = 64
        x24 = posx*512 + (384) 
        y24 = posy*-512 + (-192) 
        z24 = 64
        x25 = posx*512 + (192) 
        y25 = posy*-512 + (-192) 
        z25 = 320
        x26 = posx*512 + (192) 
        y26 = posy*-512 + (-320) 
        z26 = 320
        x27 = posx*512 + (192) 
        y27 = posy*-512 + (-320) 
        z27 = 64
        x28 = posx*512 + (384) 
        y28 = posy*-512 + (-192) 
        z28 = 64
        x29 = posx*512 + (384) 
        y29 = posy*-512 + (-320) 
        z29 = 64
        x30 = posx*512 + (384) 
        y30 = posy*-512 + (-320) 
        z30 = 320
        x31 = posx*512 + (384) 
        y31 = posy*-512 + (-192) 
        z31 = 320
        x32 = posx*512 + (192) 
        y32 = posy*-512 + (-192) 
        z32 = 320
        x33 = posx*512 + (192) 
        y33 = posy*-512 + (-192) 
        z33 = 64
        x34 = posx*512 + (384) 
        y34 = posy*-512 + (-320) 
        z34 = 64
        x35 = posx*512 + (192) 
        y35 = posy*-512 + (-320) 
        z35 = 64
        x36 = posx*512 + (192) 
        y36 = posy*-512 + (-320) 
        z36 = 320
#INSERT_ROT_0_PY_LIST
    elif rotation == 1:
        x1 = posy*-512 + 512
        y1 = -1*posx*512 
        z1 = 64
        x2 = posy*-512 + (512) + 512
        y2 = -1*posx*512 
        z2 = 64
        x3 = posy*-512 + (512) + 512
        y3 = -1*posx*512 + (-512) 
        z3 = 64
        x4 = posy*-512 + 512
        y4 = -1*posx*512 + (-512) 
        z4 = 0
        x5 = posy*-512 + (512) + 512
        y5 = -1*posx*512 + (-512) 
        z5 = 0
        x6 = posy*-512 + (512) + 512
        y6 = -1*posx*512 
        z6 = 0
        x7 = posy*-512 + 512
        y7 = -1*posx*512 
        z7 = 64
        x8 = posy*-512 + 512
        y8 = -1*posx*512 + (-512) 
        z8 = 64
        x9 = posy*-512 + 512
        y9 = -1*posx*512 + (-512) 
        z9 = 0
        x10 = posy*-512 + (512) + 512
        y10 = -1*posx*512 
        z10 = 0
        x11 = posy*-512 + (512) + 512
        y11 = -1*posx*512 + (-512) 
        z11 = 0
        x12 = posy*-512 + (512) + 512
        y12 = -1*posx*512 + (-512) 
        z12 = 64
        x13 = posy*-512 + (512) + 512
        y13 = -1*posx*512 
        z13 = 64
        x14 = posy*-512 + 512
        y14 = -1*posx*512 
        z14 = 64
        x15 = posy*-512 + 512
        y15 = -1*posx*512 
        z15 = 0
        x16 = posy*-512 + (512) + 512
        y16 = -1*posx*512 + (-512) 
        z16 = 0
        x17 = posy*-512 + 512
        y17 = -1*posx*512 + (-512) 
        z17 = 0
        x18 = posy*-512 + 512
        y18 = -1*posx*512 + (-512) 
        z18 = 64
        x19 = posy*-512 + (192) + 512
        y19 = -1*posx*512 + (-192) 
        z19 = 320
        x20 = posy*-512 + (384) + 512
        y20 = -1*posx*512 + (-192) 
        z20 = 320
        x21 = posy*-512 + (384) + 512
        y21 = -1*posx*512 + (-320) 
        z21 = 320
        x22 = posy*-512 + (192) + 512
        y22 = -1*posx*512 + (-320) 
        z22 = 64
        x23 = posy*-512 + (384) + 512
        y23 = -1*posx*512 + (-320) 
        z23 = 64
        x24 = posy*-512 + (384) + 512
        y24 = -1*posx*512 + (-192) 
        z24 = 64
        x25 = posy*-512 + (192) + 512
        y25 = -1*posx*512 + (-192) 
        z25 = 320
        x26 = posy*-512 + (192) + 512
        y26 = -1*posx*512 + (-320) 
        z26 = 320
        x27 = posy*-512 + (192) + 512
        y27 = -1*posx*512 + (-320) 
        z27 = 64
        x28 = posy*-512 + (384) + 512
        y28 = -1*posx*512 + (-192) 
        z28 = 64
        x29 = posy*-512 + (384) + 512
        y29 = -1*posx*512 + (-320) 
        z29 = 64
        x30 = posy*-512 + (384) + 512
        y30 = -1*posx*512 + (-320) 
        z30 = 320
        x31 = posy*-512 + (384) + 512
        y31 = -1*posx*512 + (-192) 
        z31 = 320
        x32 = posy*-512 + (192) + 512
        y32 = -1*posx*512 + (-192) 
        z32 = 320
        x33 = posy*-512 + (192) + 512
        y33 = -1*posx*512 + (-192) 
        z33 = 64
        x34 = posy*-512 + (384) + 512
        y34 = -1*posx*512 + (-320) 
        z34 = 64
        x35 = posy*-512 + (192) + 512
        y35 = -1*posx*512 + (-320) 
        z35 = 64
        x36 = posy*-512 + (192) + 512
        y36 = -1*posx*512 + (-320) 
        z36 = 320
#INSERT_ROT_1_PY_LIST
    elif rotation == 2:
        x1 = -1*posx*512 + 512
        y1 = -1*posy*-512 + 512
        z1 = 64
        x2 = -1*posx*512 + (512) + 512
        y2 = -1*posy*-512 + 512
        z2 = 64
        x3 = -1*posx*512 + (512) + 512
        y3 = -1*posy*-512 + (-512) + 512
        z3 = 64
        x4 = -1*posx*512 + 512
        y4 = -1*posy*-512 + (-512) + 512
        z4 = 0
        x5 = -1*posx*512 + (512) + 512
        y5 = -1*posy*-512 + (-512) + 512
        z5 = 0
        x6 = -1*posx*512 + (512) + 512
        y6 = -1*posy*-512 + 512
        z6 = 0
        x7 = -1*posx*512 + 512
        y7 = -1*posy*-512 + 512
        z7 = 64
        x8 = -1*posx*512 + 512
        y8 = -1*posy*-512 + (-512) + 512
        z8 = 64
        x9 = -1*posx*512 + 512
        y9 = -1*posy*-512 + (-512) + 512
        z9 = 0
        x10 = -1*posx*512 + (512) + 512
        y10 = -1*posy*-512 + 512
        z10 = 0
        x11 = -1*posx*512 + (512) + 512
        y11 = -1*posy*-512 + (-512) + 512
        z11 = 0
        x12 = -1*posx*512 + (512) + 512
        y12 = -1*posy*-512 + (-512) + 512
        z12 = 64
        x13 = -1*posx*512 + (512) + 512
        y13 = -1*posy*-512 + 512
        z13 = 64
        x14 = -1*posx*512 + 512
        y14 = -1*posy*-512 + 512
        z14 = 64
        x15 = -1*posx*512 + 512
        y15 = -1*posy*-512 + 512
        z15 = 0
        x16 = -1*posx*512 + (512) + 512
        y16 = -1*posy*-512 + (-512) + 512
        z16 = 0
        x17 = -1*posx*512 + 512
        y17 = -1*posy*-512 + (-512) + 512
        z17 = 0
        x18 = -1*posx*512 + 512
        y18 = -1*posy*-512 + (-512) + 512
        z18 = 64
        x19 = -1*posx*512 + (192) + 512
        y19 = -1*posy*-512 + (-192) + 512
        z19 = 320
        x20 = -1*posx*512 + (384) + 512
        y20 = -1*posy*-512 + (-192) + 512
        z20 = 320
        x21 = -1*posx*512 + (384) + 512
        y21 = -1*posy*-512 + (-320) + 512
        z21 = 320
        x22 = -1*posx*512 + (192) + 512
        y22 = -1*posy*-512 + (-320) + 512
        z22 = 64
        x23 = -1*posx*512 + (384) + 512
        y23 = -1*posy*-512 + (-320) + 512
        z23 = 64
        x24 = -1*posx*512 + (384) + 512
        y24 = -1*posy*-512 + (-192) + 512
        z24 = 64
        x25 = -1*posx*512 + (192) + 512
        y25 = -1*posy*-512 + (-192) + 512
        z25 = 320
        x26 = -1*posx*512 + (192) + 512
        y26 = -1*posy*-512 + (-320) + 512
        z26 = 320
        x27 = -1*posx*512 + (192) + 512
        y27 = -1*posy*-512 + (-320) + 512
        z27 = 64
        x28 = -1*posx*512 + (384) + 512
        y28 = -1*posy*-512 + (-192) + 512
        z28 = 64
        x29 = -1*posx*512 + (384) + 512
        y29 = -1*posy*-512 + (-320) + 512
        z29 = 64
        x30 = -1*posx*512 + (384) + 512
        y30 = -1*posy*-512 + (-320) + 512
        z30 = 320
        x31 = -1*posx*512 + (384) + 512
        y31 = -1*posy*-512 + (-192) + 512
        z31 = 320
        x32 = -1*posx*512 + (192) + 512
        y32 = -1*posy*-512 + (-192) + 512
        z32 = 320
        x33 = -1*posx*512 + (192) + 512
        y33 = -1*posy*-512 + (-192) + 512
        z33 = 64
        x34 = -1*posx*512 + (384) + 512
        y34 = -1*posy*-512 + (-320) + 512
        z34 = 64
        x35 = -1*posx*512 + (192) + 512
        y35 = -1*posy*-512 + (-320) + 512
        z35 = 64
        x36 = -1*posx*512 + (192) + 512
        y36 = -1*posy*-512 + (-320) + 512
        z36 = 320
#INSERT_ROT_2_PY_LIST
    elif rotation == 3:
        x1 = -1*posy*-512 
        y1 = posx*512 + 512
        z1 = 64
        x2 = -1*posy*-512 + (512) 
        y2 = posx*512 + 512
        z2 = 64
        x3 = -1*posy*-512 + (512) 
        y3 = posx*512 + (-512) + 512
        z3 = 64
        x4 = -1*posy*-512 
        y4 = posx*512 + (-512) + 512
        z4 = 0
        x5 = -1*posy*-512 + (512) 
        y5 = posx*512 + (-512) + 512
        z5 = 0
        x6 = -1*posy*-512 + (512) 
        y6 = posx*512 + 512
        z6 = 0
        x7 = -1*posy*-512 
        y7 = posx*512 + 512
        z7 = 64
        x8 = -1*posy*-512 
        y8 = posx*512 + (-512) + 512
        z8 = 64
        x9 = -1*posy*-512 
        y9 = posx*512 + (-512) + 512
        z9 = 0
        x10 = -1*posy*-512 + (512) 
        y10 = posx*512 + 512
        z10 = 0
        x11 = -1*posy*-512 + (512) 
        y11 = posx*512 + (-512) + 512
        z11 = 0
        x12 = -1*posy*-512 + (512) 
        y12 = posx*512 + (-512) + 512
        z12 = 64
        x13 = -1*posy*-512 + (512) 
        y13 = posx*512 + 512
        z13 = 64
        x14 = -1*posy*-512 
        y14 = posx*512 + 512
        z14 = 64
        x15 = -1*posy*-512 
        y15 = posx*512 + 512
        z15 = 0
        x16 = -1*posy*-512 + (512) 
        y16 = posx*512 + (-512) + 512
        z16 = 0
        x17 = -1*posy*-512 
        y17 = posx*512 + (-512) + 512
        z17 = 0
        x18 = -1*posy*-512 
        y18 = posx*512 + (-512) + 512
        z18 = 64
        x19 = -1*posy*-512 + (192) 
        y19 = posx*512 + (-192) + 512
        z19 = 320
        x20 = -1*posy*-512 + (384) 
        y20 = posx*512 + (-192) + 512
        z20 = 320
        x21 = -1*posy*-512 + (384) 
        y21 = posx*512 + (-320) + 512
        z21 = 320
        x22 = -1*posy*-512 + (192) 
        y22 = posx*512 + (-320) + 512
        z22 = 64
        x23 = -1*posy*-512 + (384) 
        y23 = posx*512 + (-320) + 512
        z23 = 64
        x24 = -1*posy*-512 + (384) 
        y24 = posx*512 + (-192) + 512
        z24 = 64
        x25 = -1*posy*-512 + (192) 
        y25 = posx*512 + (-192) + 512
        z25 = 320
        x26 = -1*posy*-512 + (192) 
        y26 = posx*512 + (-320) + 512
        z26 = 320
        x27 = -1*posy*-512 + (192) 
        y27 = posx*512 + (-320) + 512
        z27 = 64
        x28 = -1*posy*-512 + (384) 
        y28 = posx*512 + (-192) + 512
        z28 = 64
        x29 = -1*posy*-512 + (384) 
        y29 = posx*512 + (-320) + 512
        z29 = 64
        x30 = -1*posy*-512 + (384) 
        y30 = posx*512 + (-320) + 512
        z30 = 320
        x31 = -1*posy*-512 + (384) 
        y31 = posx*512 + (-192) + 512
        z31 = 320
        x32 = -1*posy*-512 + (192) 
        y32 = posx*512 + (-192) + 512
        z32 = 320
        x33 = -1*posy*-512 + (192) 
        y33 = posx*512 + (-192) + 512
        z33 = 64
        x34 = -1*posy*-512 + (384) 
        y34 = posx*512 + (-320) + 512
        z34 = 64
        x35 = -1*posy*-512 + (192) 
        y35 = posx*512 + (-320) + 512
        z35 = 64
        x36 = -1*posy*-512 + (192) 
        y36 = posx*512 + (-320) + 512
        z36 = 320
#INSERT_ROT_3_PY_LIST
    var_count = 36
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
#INSERT_ENT_CODE
    return values, id_num, world_id_num