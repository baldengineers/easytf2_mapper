import os
import wall_prefab
import ground_prefab

global values
global beg_template

open('Script_.tmp', 'w').close()

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
if __name__ == '__main__':
    # service.py executed as script
    # do something
    wall_prefab.find()
    whole = beg_template + """values from wall_prefab, how to?
                            You would have to import the wall_prefab.py
                            then use wall_prefab.variable to reference it"""

