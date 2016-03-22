import os

def execute(totalblocks, entity_list,levels, skybox, skyboxgeolist):
    compiledblocks=''
    totalentities=''
    beg_template = open('prefab_template/beginning_template.txt', 'r+')
    beg_template = beg_template.readlines()
    beg_template = "".join(beg_template)
    beg_template = beg_template.replace('CURRENT_SKYBOX',skybox)
    skyboxgeolist = "".join(skyboxgeolist)
    end_template = """ 
cameras
{
    "activecamera" "-1"
}
cordon
{
    "mins" "(-1024 -1024 -1024)"
    "maxs" "(1024 1024 1024)"
    "active" "0"
}
    """
    #end of file template that ends each vmf
    #print(totalblocks)
    for i in range(levels):
        compiledblocks += "".join(totalblocks[i]) #totalblocks will be a list of each "block" from each chunk in the map, put into 1 string here.
        totalentities += "".join(entity_list[i])
    compiledblocks = compiledblocks.replace('EMPTY_SLOT','')
    #totalentities = "".join(entity_list)
    totalentities = totalentities.replace('NO_ENTITY','')
    whole = beg_template + compiledblocks + skyboxgeolist + "}\n"+totalentities + end_template
    #whole = beg_template + compiledblocks + "}\n"+ end_template
    

    return whole

