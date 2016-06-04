import os

def execute(totalblocks, entity_list,levels, skybox, skyboxgeolist, light):
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
    "mins" "(-10240 -10240 -10240)"
    "maxs" "(10240 10240 10240)"
    "active" "0"
}
    """
    #end of file template that ends each vmf
    #print(totalblocks)
    compiledblocks = "".join(totalblocks) #totalblocks will be a list of each "block" from each chunk in the map, put into 1 string here.
    totalentities = "".join(entity_list)
    compiledblocks = compiledblocks.replace('EMPTY_SLOT','')
    #totalentities = "".join(entity_list)
    totalentities = totalentities.replace('NO_ENTITY','')
    whole = beg_template + compiledblocks + skyboxgeolist + "}\n"+totalentities + light + end_template
    #whole = beg_template + compiledblocks + "}\n"+ end_template
    

    return whole

