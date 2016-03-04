readme:

run the main.py or (maybe) the main.exe

Ctrl+G = resize grid. deletes all blocks.

Ctrl+S = choose skybox texture. I reccommend choosing one that you want, the default is pretty bland.

Ctrl+E = export vmf. do this when you're done.

Ctrl+J = Change environmental lighting (obsolete)

Ctrl+H = Opens Hammer. The first time you do this, you will have to point the program to your hammer.exe

Alt+click on a square with a prefab on it to remove it.

When creating a prefab, make it in the lower right quadrant of the grid, with one corner touching the origin.
Make the ground a 64 high 512*512 block for uniformity. Report bugs with this to toadsrc@gmail.com.

After exporting, open the .vmf in hammer to make it into a .bsp.


TODO: http://pythonhosted.org/PyInstaller/ create redistributable package. as a side note, we need to manually add every single prefab
.py, as pyinstaller cannot detect modules imported with the modification of sys.path
