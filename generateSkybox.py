import os

def createSkyboxLeft(gridx,gridy,skyboxz,id_num,world_id_num):
    values = []
    f = open('prefab_template/skybox_worldgeo/skybox_side.txt','r+')
    lines = f.readlines()
    values = "".join(lines)
    ogvalues = "".join(lines)
    values = values.replace("world_idnum", str(world_id_num))
    world_id_num += 1
    values = values.replace("skyboxz",str(skyboxz))
    values = values.replace("ynum",str(gridy*-512))

    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        id_num = id_num+1

    return values, id_num, world_id_num

def createSkyboxNorth(gridx,gridy,skyboxz,id_num,world_id_num):
    values = []
    f = open('prefab_template/skybox_worldgeo/skybox_north.txt','r+')
    lines = f.readlines()
    values = "".join(lines)
    ogvalues = "".join(lines)
    values = values.replace("skyboxz",str(skyboxz))
    values = values.replace("world_idnum",str(world_id_num))
    world_id_num += 1
    values = values.replace("numx",str(gridx*512))
    
    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        id_num = id_num+1

    return values, id_num, world_id_num

def createSkyboxTop(gridx,gridy,skyboxz,id_num,world_id_num):
    values = []
    f = open('prefab_template/skybox_worldgeo/skybox_top.txt','r+')
    lines = f.readlines()
    values = "".join(lines)
    ogvalues = "".join(lines)
    values = values.replace("skyboxz",str(skyboxz))
    values = values.replace("numx",str(gridx*512))
    values = values.replace("numy",str(gridy*-512))
    values = values.replace("world_idnum",str(world_id_num))
    world_id_num += 1
    values = values.replace("skyboxadd",str(skyboxz+64))

    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        id_num = id_num+1

    return values, id_num, world_id_num

def createSkyboxRight(gridx,gridy,skyboxz,id_num,world_id_num):
    values = []
    f = open('prefab_template/skybox_worldgeo/skybox_right.txt','r+')
    lines = f.readlines()
    values = "".join(lines)
    ogvalues = "".join(lines)
    values = values.replace("skyboxz",str(skyboxz))
    values = values.replace("xnum",str((gridx*512)+64))
    values = values.replace("numx",str(gridx*512))
    values = values.replace("numy",str(gridy*-512))
    values = values.replace("world_idnum",str(world_id_num))
    world_id_num += 1

    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        id_num = id_num+1

    return values, id_num, world_id_num

def createSkyboxSouth(gridx,gridy,skyboxz,id_num,world_id_num):
    values = []
    f = open('prefab_template/skybox_worldgeo/skybox_south.txt','r+')
    lines = f.readlines()
    values = "".join(lines)
    ogvalues = "".join(lines)
    values = values.replace("skyboxz",str(skyboxz))
    values = values.replace("ynum",str((gridy*-512)-64))
    values = values.replace("numy",str(gridy*-512))
    values = values.replace("numx",str(gridx*512))
    values = values.replace("world_idnum",str(world_id_num))
    world_id_num += 1

    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        id_num = id_num+1

    return values, id_num, world_id_num
