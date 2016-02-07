import os
import wall_prefab
import ground_prefab

open('Script_.tmp', 'w').close()
def service_func():
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
    service_func()
    wall_prefab.find()

