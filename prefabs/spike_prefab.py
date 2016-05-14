import os

def createTile(posx, posy, id_num, world_id_num):
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
    f = open('prefab_template/spike_prefab.txt', 'r+')
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
    x19 = posx*512 + (64)
    y19 = posy*-512 + (-64)
    z19 = 128
    x20 = posx*512 + (448)
    y20 = posy*-512 + (-64)
    z20 = 128
    x21 = posx*512 + (448)
    y21 = posy*-512 + (-448)
    z21 = 128
    x22 = posx*512 + (64)
    y22 = posy*-512 + (-448)
    z22 = 64
    x23 = posx*512 + (448)
    y23 = posy*-512 + (-448)
    z23 = 64
    x24 = posx*512 + (448)
    y24 = posy*-512 + (-64)
    z24 = 64
    x25 = posx*512 + (64)
    y25 = posy*-512 + (-64)
    z25 = 128
    x26 = posx*512 + (64)
    y26 = posy*-512 + (-448)
    z26 = 128
    x27 = posx*512 + (64)
    y27 = posy*-512 + (-448)
    z27 = 64
    x28 = posx*512 + (448)
    y28 = posy*-512 + (-64)
    z28 = 64
    x29 = posx*512 + (448)
    y29 = posy*-512 + (-448)
    z29 = 64
    x30 = posx*512 + (448)
    y30 = posy*-512 + (-448)
    z30 = 128
    x31 = posx*512 + (448)
    y31 = posy*-512 + (-64)
    z31 = 128
    x32 = posx*512 + (64)
    y32 = posy*-512 + (-64)
    z32 = 128
    x33 = posx*512 + (64)
    y33 = posy*-512 + (-64)
    z33 = 64
    x34 = posx*512 + (448)
    y34 = posy*-512 + (-448)
    z34 = 64
    x35 = posx*512 + (64)
    y35 = posy*-512 + (-448)
    z35 = 64
    x36 = posx*512 + (64)
    y36 = posy*-512 + (-448)
    z36 = 128
    x37 = posx*512 + (128)
    y37 = posy*-512 + (-128)
    z37 = 192
    x38 = posx*512 + (384)
    y38 = posy*-512 + (-128)
    z38 = 192
    x39 = posx*512 + (384)
    y39 = posy*-512 + (-384)
    z39 = 192
    x40 = posx*512 + (128)
    y40 = posy*-512 + (-384)
    z40 = 128
    x41 = posx*512 + (384)
    y41 = posy*-512 + (-384)
    z41 = 128
    x42 = posx*512 + (384)
    y42 = posy*-512 + (-128)
    z42 = 128
    x43 = posx*512 + (128)
    y43 = posy*-512 + (-128)
    z43 = 192
    x44 = posx*512 + (128)
    y44 = posy*-512 + (-384)
    z44 = 192
    x45 = posx*512 + (128)
    y45 = posy*-512 + (-384)
    z45 = 128
    x46 = posx*512 + (384)
    y46 = posy*-512 + (-128)
    z46 = 128
    x47 = posx*512 + (384)
    y47 = posy*-512 + (-384)
    z47 = 128
    x48 = posx*512 + (384)
    y48 = posy*-512 + (-384)
    z48 = 192
    x49 = posx*512 + (384)
    y49 = posy*-512 + (-128)
    z49 = 192
    x50 = posx*512 + (128)
    y50 = posy*-512 + (-128)
    z50 = 192
    x51 = posx*512 + (128)
    y51 = posy*-512 + (-128)
    z51 = 128
    x52 = posx*512 + (384)
    y52 = posy*-512 + (-384)
    z52 = 128
    x53 = posx*512 + (128)
    y53 = posy*-512 + (-384)
    z53 = 128
    x54 = posx*512 + (128)
    y54 = posy*-512 + (-384)
    z54 = 192
    x55 = posx*512 + (192)
    y55 = posy*-512 + (-320)
    z55 = 192
    x56 = posx*512 + (256)
    y56 = posy*-512 + (-256)
    z56 = 448
    x57 = posx*512 + (320)
    y57 = posy*-512 + (-320)
    z57 = 192
    x58 = posx*512 + (320)
    y58 = posy*-512 + (-192)
    z58 = 192
    x59 = posx*512 + (192)
    y59 = posy*-512 + (-192)
    z59 = 192
    x60 = posx*512 + (192)
    y60 = posy*-512 + (-320)
    z60 = 192
    x61 = posx*512 + (192)
    y61 = posy*-512 + (-192)
    z61 = 192
    x62 = posx*512 + (256)
    y62 = posy*-512 + (-256)
    z62 = 448
    x63 = posx*512 + (192)
    y63 = posy*-512 + (-320)
    z63 = 192
    x64 = posx*512 + (320)
    y64 = posy*-512 + (-192)
    z64 = 192
    x65 = posx*512 + (320)
    y65 = posy*-512 + (-320)
    z65 = 192
    x66 = posx*512 + (256)
    y66 = posy*-512 + (-256)
    z66 = 448
    x67 = posx*512 + (320)
    y67 = posy*-512 + (-192)
    z67 = 192
    x68 = posx*512 + (256)
    y68 = posy*-512 + (-256)
    z68 = 448
    x69 = posx*512 + (192)
    y69 = posy*-512 + (-192)
    z69 = 192
    var_count = 69
    values = "".join(lines)#converting list to string
    ogvalues = "".join(lines)
	
    normal_list,axislist,negaxislist,vaxis,uaxis=[],['1 0 0 1','0 1 0 1','0 0 1 1'],['-1 0 0 1','0 -1 0 1','0 0 -1 1'],0,0
    def evaluate(coords):
        dist_x,dist_y,dist_z = abs(coords[0]),abs(coords[1]),abs(coords[2]),
        if dist_x >= dist_y and dist_x >= dist_z:
            return axislist[0]
        if dist_y >= dist_z:
            return axislist[1]
        return axislist[2]

    def get_normal(coord_list):
        vector_a = (coord_list[1][0]-coord_list[0][0],coord_list[1][1]-coord_list[0][1],coord_list[1][2]-coord_list[0][2])
        vector_b = (coord_list[2][0]-coord_list[0][0],coord_list[2][1]-coord_list[0][1],coord_list[2][2]-coord_list[0][2])
        
        normal = (vector_a[1]*vector_b[2]-vector_a[2]*vector_b[1],vector_a[2]*vector_b[0]-vector_a[0]*vector_b[2],vector_a[0]*vector_b[1]-vector_a[1]*vector_b[0])
        return normal
    
    for normal_num in range(1,var_count+1,3):
        normal_list=[]
        for i in range(3):
            normal_list.append([])
            for var in ["x", "y", "z"]:
                normal_list[i].append(eval(var+str(normal_num+i)))
        coords = get_normal(normal_list)  
        response = evaluate(coords)
        if response == axislist[0]:
            uaxis = axislist[1]
        else:
            uaxis = axislist[0]
        if response == axislist[2]:
            vaxis = negaxislist[1]
        else:
            vaxis = negaxislist[2]
        values = values.replace('AXIS_REPLACE_U',uaxis,1)
        values = values.replace('AXIS_REPLACE_V',vaxis,1)

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
