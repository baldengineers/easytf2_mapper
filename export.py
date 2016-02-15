import os

def execute(totalblocks):

    beg_template = """
versioninfo
{
    "editorversion" "400"
    "editorbuild" "7026"
    "mapversion" "1"
    "formatversion" "100"
    "prefab" "0"
}
visgroups
{
}
viewsettings
{
    "bSnapToGrid" "1"
    "bShowGrid" "1"
    "bShowLogicalGrid" "0"
    "nGridSpacing" "64"
    "bShow3DGrid" "0"
}
world
{
    "id" "1"
    "mapversion" "1"
    "classname" "worldspawn"
    "skyname" "sky_tf2_04"
    "maxpropscreenwidth" "-1"
    "detailvbsp" "detail_2fort.vbsp"
    "detailmaterial" "detail/detailsprites_2fort"
"""
    end_template = """ 
}
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
    compiledblocks = "".join(totalblocks) #totalblocks will be a list of each "block" from each chunk in the map, put into 1 string here.
    compiledblocks = compiledblocks.replace('EMPTY_SLOT','')
    whole = beg_template + compiledblocks + end_template
    return whole

