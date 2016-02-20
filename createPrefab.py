"""
This function takes a vmf file exported from hammer, then exports both a
prefab txt template (look in prefabs folder), and a .py containing the
algorithms to create the object
"""

def write_var(num_list, txt_list, py_list, var_num, value_list_history):
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
      py_list.append("%s%d = %s%s*%s512" %(var, var_num, "pos", var, negative))
      #print(py_list)
    else:
      py_list.append("%s%d = %s%s*%s512 + (%d)" %(var, var_num, "pos", var, negative, value))
      #print(py_list)

    txt_list[txt_list.index("INSERT_VAR")] = "%s%d" %(var, var_num)
  

def compileTXT(txt_path, txt_list, prefab_name, prefab_text, prefab_icon):
  #This compiles the txt prefab template
  file = open(txt_path, "w")
  
  for item in txt_list:
    file.write(item)

  prefab_file = open("prefab_template\\prefab_list.txt", "a")
  prefab_text_file = open("prefab_template\\prefab_text_list.txt", "a")
  prefab_icon_file = open("prefab_template\\prefab_icon_list.txt", "a")

  prefab_file.write(prefab_name + "\n")
  prefab_text_file.write(prefab_text + "\n")
  prefab_icon_file.write(prefab_icon + "\n")

  for file in [prefab_file, prefab_text_file, prefab_icon_file]:
    file.close()

  file.close()

  return "File Exported as \"%s\"\n" %(txt_path)

  
  

def compilePY(py_path, py_list, txt_path, compile_list, contains_ent, ent_code):
  #This compiles the py file containing the algorithms
  
  for item in py_list:
    compile_list.insert(compile_list.index("INSERT_PY_LIST"), "    " + item + "\n")

  compile_list[compile_list.index("INSERT_OPEN_FILE")] = "    f = open('%s', 'r+')" %(txt_path)

  compile_list[compile_list.index("INSERT_PY_LIST")] = ""

  var_count = (len(py_list) + 1)/3

  compile_list[compile_list.index("INSERT_VAR_COUNT")] = "    var_count = %d" %(var_count)

  if contains_ent:
    compile_list[compile_list.index("INSERT_ENT_CODE")] = ent_code

  file = open(py_path, "w")
  
  for item in compile_list:
    file.write(item)

  file.close()

  return "File Exported as \"%s\"\n" %(py_path)

  



def create(name, prefab_name, prefab_text, prefab_icon):

  py_list = []
  txt_list = []
  num_list = []
  id_num_list = []
  id_value_list = []
  value_list = []
  compile_list = [
  """import os

def createTile(posx, posy, id_num, world_id_num):
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
""",

  "INSERT_OPEN_FILE",

  """
    lines = f.readlines() #gathers each line of the prefab and puts numbers them
""",

  "INSERT_PY_LIST",

  "INSERT_VAR_COUNT",

  """
    values = "".join(lines)#converting list to string
    ogvalues = "".join(lines)
    
    for i in range(ogvalues.count("world_idnum")):
        values = values.replace('world_idnum', str(world_id_num), 1)
        world_id_num += 1
    
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
        id_num = id_num+1""",

  "INSERT_ENT_CODE",
  
  "    return values, id_num, world_id_num, entity_num"
  ]

  ent_code ="""    for i in range(ogvalues.count("entity_name")):
        values = values.replace("entity_name", "entity" + str(entity_num), 1) #NEED TO MAKE VAR CALLED ENTITY NUM PLZ
        entity_num += entity_num


"""

  var_num = 1
  contains_ent = False #True if there are entities in the vmf
  black_list_var = False #True means it IS on the blacklist, False otherwise
  value_list_history = []
  #name = "prefab_template\godplsno.vmf" #name of the vmf file, changed to allow user to open a file
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

  prefab_icon_list = prefab_icon.split("/")

  if "easytf2_mapper" in prefab_icon_list:
    del prefab_icon_list[ :prefab_icon_list.index("easytf2_mapper")+1]

    for index, item in enumerate(prefab_icon_list): #enumerate allows you to give 2 vars in the for loop
      if index != len(prefab_icon_list) - 1:
        #print(index, " is ", item, " in ", prefab_icon_list)
        prefab_icon_list[index] = item + "/" # add the "/" back into the filepath
    
    prefab_icon = "".join(prefab_icon_list)
    #print("prefab_icon: ",prefab_icon)

  #main loop
  #prefab_name = input("Name of prefab? (eg. wall_prefab)\n")
  txt_path = "prefab_template/" + prefab_name + ".txt"
  py_path = prefab_name + ".py"

  for line in openlines:
    
    for item in black_list:
      if item in line:
        black_list_var = True
        
    #if "\t" not in line:
     # createBlackList(line)
    if not black_list_var:
      if "\t" in line:
        if "solid" in line: #or "side" in line:# or "origin" in line: #need to add this because somehow, the solid/side
                                              #line does not make it past "if id not in line"
          txt_list.append(line)
          #go until "\t}"

          while "\t}" not in line:

            if "(" not in line:

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
                  elif letter == " ":
                    num_list.append("SEPARATE")
                  elif letter == "-":
                    num_list.append("-")
                  elif letter == ")":
                    write_var(num_list, txt_list, py_list, var_num, value_list_history) 
                    var_num += 1
                    num_list = []
		
          txt_list.append(line)
		
        elif "entity" in line:
          contains_ent = True
          txt_list.append(line)
          while "\"" in line:
            #do something
            if "id" in line:
                  for letter in line:
                    try:
                          number = int(letter)
                    except ValueError:
                          txt_list.append(letter)
                          
                  txt_list.insert(-2, "world_idnum")
                  
            elif "targetname" in line:
              for letter in line:
                for item in [t,a,r,g,e,t,n,a,m,e]:
                  if letter == "\"" or letter == item:
                    txt_list.append(letter)
                            
              txt_list.insert(-2, "entity_name")
                  
            elif "origin" in line:
              nums_yet = False #if True then numbers have been received
              for letter in line:
                
                #print(letter)
                try:
                  number = int(letter)    
                  num_list.append(letter)
                  nums_yet = True
                except ValueError:
                  if letter != "-":
                    txt_list.append(letter)
                  elif letter == " ":
                    num_list.append("SEPARATE")
                  elif letter == "-":
                    num_list.append("-")
                  elif letter == "\"" and nums_yet:
                    write_var(num_list, txt_list, py_list, var_num, value_list_history) 
                    var_num += 1
                    num_list = []                  
                
                          
				
				
		  

    black_list_var = False

  file.close()
  return compileTXT(txt_path, txt_list, prefab_name, prefab_text, prefab_icon) + compilePY(py_path, py_list, txt_path, compile_list, contains_ent, ent_code)

