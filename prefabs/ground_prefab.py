#file for getting coords of a ground tile
import os

def createTile(posx, posy, id_num, world_id_num):
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
    f = open('prefab_template/ground_prefab.txt', 'r+')
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
    
            values = values.replace(var + str(count),str(eval(var + str(count))))

    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        id_num = id_num+1
  
    return values, id_num, world_id_num
