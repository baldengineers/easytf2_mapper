import os

def execute(totalblocks, entity_list, skybox):

    beg_template = open('prefab_template/beginning_template.txt', 'r+')
    beg_template = beg_template.readlines()
    beg_template = "".join(beg_template)
    beg_template = beg_template.replace('CURRENT_SKYBOX',skybox)
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
    print(entity_list)
    compiledblocks = "".join(totalblocks) #totalblocks will be a list of each "block" from each chunk in the map, put into 1 string here.
    compiledblocks = compiledblocks.replace('EMPTY_SLOT','')
    totalentities = "".join(entity_list)
    totalentities = totalentities.replace('NO_ENTITY','')
    whole = beg_template + compiledblocks + "}\n"+totalentities + end_template
    #whole = beg_template + compiledblocks + "}\n"+ end_template

    return whole

