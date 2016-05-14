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
    f = open('prefab_template/blank_tile.txt', 'r+')
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
#INSERT_ROT_CODE

    var_count = 18
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
        

    g = open('prefab_template/blank_tile_entities.txt', 'r+')
    lines_ent = g.readlines()
#INSERT_ROT_IF
    px1 = posx*1*512
    py1 = posy*-1*512
    pz1 = level*512 + 73
#INSERT_ROT_ENT_CODE
    ent_var_count = 1
    ent_values = "".join(lines_ent)
    ent_values_split = ent_values.split("\"")
    valcount = "".join(lines_ent)

    for item in ent_values_split:
        if "entity_name" in item or "parent_name" in item or "door_large" in item:
            placeholder_list.append(item)

    for i in range(valcount.count('world_idnum')):
        ent_values = ent_values.replace('world_idnum', str(world_id_num), 1)
        world_id_num += 1

    for var in ["px", "py", "pz"]:
        for count in range(1,ent_var_count+1):
            string = var + str(count)
            string_var = str(eval(var + str(count)))

            if var == "pz":
                ent_values = ent_values.replace(string + "\"",string_var + "\"") #we need to do this or else it will mess up on 2 digit numbers
            else:
                ent_values = ent_values.replace(string + " ",string_var + " ")
                
    for var in ["x", "y", "z"]:
        for count in range(1,var_count+1):
            try:
                string = var + str(count)
                string_var = str(eval(var + str(count)))
                if var == "z":
                    ent_values = ent_values.replace(string + ")",string_var + ")") #we need to do this or else it will mess up on 2 digit numbers
                else:
                    ent_values = ent_values.replace(string + " ",string_var + " ")
            except:
                pass

    for i in range(valcount.count('id_num')):
        ent_values = ent_values.replace('id_num', str(id_num), 1)
        id_num = id_num+1

    for i in range(valcount.count("entity_name")):
        try:
            ent_values = ent_values.replace("entity_name", "entity" + str(entity_num), 1)
            ent_values = ent_values.replace("entity_same", "entity" + str(entity_num), 1)
            if "parent_name" in placeholder_list[entity_num]:
                ent_values = ent_values.replace("parent_name", "entity" + str(entity_num), 1)
                placeholder_list.remove(placeholder_list[entity_num])
            
            if "door_large" in ent_values:
                ent_values = ent_values.replace("door_large", "door_large" + str(entity_num), 4)
            if "\"respawn_name\"" in ent_values:
                ent_values = ent_values.replace("\"respawn_name\"", "\"respawn_name" + str(entity_num) + "\"", 2)
            if "ROTATION_RIGHT" in ent_values:
                if rotation == 0:
                    ent_values = ent_values.replace("ROTATION_RIGHT","0 0 0",1)
                elif rotation == 1:
                    ent_values = ent_values.replace("ROTATION_RIGHT","0 270 0",1)
                elif rotation == 2:
                    ent_values = ent_values.replace("ROTATION_RIGHT","0 180 0",1)
                elif rotation == 3:
                    ent_values = ent_values.replace("ROTATION_RIGHT","0 90 0",1)
            if "ROTATION_UP" in ent_values:
                if rotation == 0:
                    ent_values = ent_values.replace("ROTATION_UP","0 90 0",1)
                elif rotation == 1:
                    ent_values = ent_values.replace("ROTATION_UP","0 0 0",1)
                elif rotation == 2:
                    ent_values = ent_values.replace("ROTATION_UP","0 270 0",1)
                elif rotation == 3:
                    ent_values = ent_values.replace("ROTATION_UP","0 180 0",1)
            if "ROTATION_LEFT" in ent_values:
                if rotation == 0:
                    ent_values = ent_values.replace("ROTATION_LEFT","0 180 0",1)
                elif rotation == 1:
                    ent_values = ent_values.replace("ROTATION_LEFT","0 90 0",1)
                elif rotation == 2:
                    ent_values = ent_values.replace("ROTATION_LEFT","0 0 0",1)
                elif rotation == 3:
                    ent_values = ent_values.replace("ROTATION_LEFT","0 270 0",1)
            if "ROTATION_DOWN" in ent_values:
                if rotation == 0:
                    ent_values = ent_values.replace("ROTATION_DOWN","0 270 0",1)
                elif rotation == 1:
                    ent_values = ent_values.replace("ROTATION_DOWN","0 180 0",1)
                elif rotation == 2:
                    ent_values = ent_values.replace("ROTATION_DOWN","0 90 0",1)
                elif rotation == 3:
                    ent_values = ent_values.replace("ROTATION_DOWN","0 0 0",1)
            
            entity_num += 1
        except:
            pass



    return values, id_num, world_id_num, entity_num, ent_values, placeholder_list