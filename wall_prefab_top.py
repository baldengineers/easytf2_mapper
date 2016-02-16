import os

def createTile(posx, posy, id_num, world_id_num):
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
    f = open('prefab_template\\wall_prefab_top.txt', 'r+')
    lines = f.readlines() #gathers each line of the prefab and puts numbers them
    var_count = 0
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