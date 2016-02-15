"""
This program takes a vmf file exported from hammer, then exports both a
prefab txt template (look in prefabs folder), and a .py containing the
algorithms to create the object
"""







py_list = []
txt_list = []
num_list = []
id_num_list = []
id_value_list = []
value_list = []
compile_list = [
"""
import os

def createTile(posx, posy, id_num, world_id_num):
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
    f = open('prefabs\prefab_blanktile.txt', 'r+')
    lines = f.readlines() #gathers each line of the prefab and puts numbers them
""",
"INSERT_PY_LIST",
"INSERT_VAR_COUNT",
"""
    values = "".join(lines)#converting list to string
    ogvalues = "".join(lines)
    values = values.replace('world_idnum', str(world_id_num))
    #world_id_num += 1
    
    for var in ["x", "y", "z"]:
        for count in range(1,var_count+1):
    
            values = values.replace(var + str(count),str(eval(var + str(count))))

    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        id_num = id_num+1
  
    return values
"""
]

var_num = 1
black_list_var = False #True means it IS on the blacklist, False otherwise
value_list_history = []
name = "prefabs\godplsno.vmf" #name of the vmf file, will change to allow user to open a file
file = open(name, "r")

black_list = ["editorversion",
              "editorbuild",
              "mapversion",
              "formatversion",
              "prefab",
              "bSnapToGrid",
              "bShowGrid",
              "bShowLogicalGrid",
              "nGridSpacing",
              "bShow3DGrid",
              "mapversion",
              "classname",
              "skyname",
              "maxpropscreenwidth",
              "detailvbsp",
              "detailmaterial",
              "activecamera",
              "mins",
              "maxs",
              "active"]

openlines = file.readlines()

def write_var():
  #TODO: Add a values list history, that keeps track of all the past value_lists
  #so we can see if there are duplicate value lists. 
  
  value_list = []
  #item count needs to be -1 so that the initial "SEPARATE" makes the var 0
  num_count = -1

  #print("num_list: ", num_list)
  
  for item in num_list:
    if item == "SEPARATE":
      num_count += 1
      #print(num_count)
    else:
      try:
        value_list[num_count] = value_list[num_count] + item
      except IndexError:
        value_list.append(item)

  #print("value_list: ", value_list)
  value_list_history.append(value_list)
  #print("value_list_history: ", value_list_history)

  item_count = 0
  for item in value_list:
    txt_list.insert(-1 - item_count, "INSERT_VAR")
    item_count += 2 
  
  xyz_list = ["x", "y", "z"]
  
  for var in xyz_list:
    
    value = int(value_list[xyz_list.index(var)])

    if var == "x":
      negative = ""
    elif var == "y":
      negative = "-"
        
    if var == "z":
      py_list.append("%s%d = %d" %(var, var_num, value))
      #print(py_list)
    elif value == 0:
      py_list.append("%s%d = %s*%s512" %(var, var_num, var, negative))
      #print(py_list)
    else:
      py_list.append("%s%d = %s*%s512 + (%d)" %(var, var_num, var, negative, value))
      #print(py_list)

    txt_list[txt_list.index("INSERT_VAR")] = "%s%d" %(var, var_num)

    #print("txt_list: ", txt_list)
  

def compileTXT():
  #This compiles the txt prefab template
  name = "prefabs\\" + prefab_name + ".txt"
  file = open(name, "w")
  
  for item in txt_list:
    file.write(item)

  print("File Exported as \"%s\"" %(name))

def compilePY():
  #This compiles the py file containing the algorithms
  for item in py_list:
    compile_list.insert(compile_list.index("INSERT_PY_LIST"), "    " + item + "\n")

  compile_list[compile_list.index("INSERT_PY_LIST")] = ""

  var_count = (len(py_list) + 1)/3

  compile_list[compile_list.index("INSERT_VAR_COUNT")] = "    var_count = %d" %(var_count)

  name = prefab_name + ".py"
  file = open(name, "w")
  
  for item in compile_list:
    file.write(item)

  print("File Exported as \"%s\"" %(name))











#main loop
prefab_name = input("Name of prefab? (eg. wall_prefab)\n")  

for line in openlines:
  
  for item in black_list:
    if item in line:
      black_list_var = True

  #Testing creating the black_list automatically
  #if "\t" not in line:
   # createBlackList(line)
  if not black_list_var:
    if "\t" in line:
      if "(" not in line:
        if "solid" in line or "side" in line: #need to add this because somehow, the solid/side
                                              #line does not make it past "if id not in line"
            txt_list.append(line)

        
        if "id" not in line:
          txt_list.append(line)
        elif "\t\t\"id\"" in line:
          for letter in line:
            try:
              number = int(letter)
            except ValueError:
              txt_list.append(letter)

          if "\t\t\t" in line:
            txt_list.insert(-2, "id_num") #need to insert because it creates a \n at the end of the line
          else: 
            txt_list.insert(-2, "world_idnum")

        #print(txt_list)

      elif "(" in line:
        for letter in line:
          #print(letter)
          try:
            number = int(letter)    
            num_list.append(letter)
          except ValueError:
            if letter != "-":
              txt_list.append(letter)
            if letter == " ":
              num_list.append("SEPARATE")
            elif letter == "-":
              num_list.append("-")
            elif letter == ")":
              write_var() 
              var_num += 1
              num_list = []

  black_list_var = False

  
compileTXT()
compilePY()

      
        
