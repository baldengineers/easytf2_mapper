"""
This function takes a vmf file exported from hammer, then exports both a
prefab txt template (look in prefabs folder), and a .py containing the
algorithms to create the object
"""
def write_var(num_list, txt_list, py_list, var_num, value_list_history, in_solid_block, in_entity_block):
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

  if in_solid_block:
    xyz_list = ["x", "y", "z"]
  elif in_entity_block:
    xyz_list = ["px", "py", "pz"]
  
  for var in xyz_list:

    try:
      value = int(value_list[xyz_list.index(var)])
    except ValueError:
      value = float(value_list[xyz_list.index(var)])
      

    if var == "x" or var == "px":
      negative = ""
    elif var == "y" or var == "py":
      negative = "-"
        
    if var == "z" or var == "pz":
      py_list.append("%s%d = %d" %(var, var_num, value))
      #print(py_list)
    elif value == 0:
      py_list.append("%s%d = %s%s*%s512" %(var, var_num, "pos", var[-1] if var.startswith("p") else var, negative))
      #print(py_list)
    else:
      py_list.append("%s%d = %s%s*%s512 + (%d)" %(var, var_num, "pos", var[-1] if var.startswith("p") else var, negative, value))
      #print(py_list)

    txt_list[txt_list.index("INSERT_VAR")] = "%s%d" %(var, var_num)
  

def compileTXT(txt_path, txt_list, prefab_name, prefab_text, prefab_icon, ent_list, ent_path):
  #This compiles the txt prefab template
  file = open(txt_path, "w")
  
  for item in txt_list:
    file.write(item)
  file.close()

  file = open(ent_path, "w")

  for item in ent_list:
    file.write(item)
  file.close
    

  prefab_file = open("prefab_template\\prefab_list.txt", "a")
  prefab_text_file = open("prefab_template\\prefab_text_list.txt", "a")
  prefab_icon_file = open("prefab_template\\prefab_icon_list.txt", "a")

  prefab_file.write(prefab_name + "\n")
  prefab_text_file.write(prefab_text + "\n")
  prefab_icon_file.write(prefab_icon + "\n")

  for file in [prefab_file, prefab_text_file, prefab_icon_file]:
    file.close()

  return "File Exported as \"%s\"\n" %(txt_path)

  
  

def compilePY(py_path, py_list, txt_path, compile_list, contains_ent, ent_code, ent_path, ent_py_list):
  #This compiles the py file containing the algorithms
  
  for item in py_list:
    compile_list.insert(compile_list.index("#INSERT_PY_LIST"), "    " + item + "\n")

  compile_list[compile_list.index("#INSERT_OPEN_FILE")] = "    f = open('%s', 'r+')" %(txt_path)

  compile_list[compile_list.index("#INSERT_PY_LIST")] = ""

  var_count = (len(py_list) + 1)/3

  compile_list[compile_list.index("#INSERT_VAR_COUNT")] = "    var_count = %d" %(var_count)

  if contains_ent:
    ent_code[ent_code.index("#INSERT_ENT_OPEN_FILE")] = "\n    g = open('%s', 'r+')" %(ent_path)

    for item in ent_py_list:
      ent_code.insert(ent_code.index("#INSERT_ENT_PY_LIST"), "    " + item + "\n")

    ent_code[ent_code.index("#INSERT_ENT_PY_LIST")] = ""

    ent_var_count = (len(ent_py_list) + 1)/3

    ent_code[ent_code.index("#INSERT_ENT_VAR_COUNT")] = "    ent_var_count = %d" %(ent_var_count)

    for item in ent_code:
      compile_list.insert(compile_list.index("#INSERT_ENT_CODE"), item)

    compile_list[compile_list.index("#INSERT_ENT_CODE")] = ""

  file = open(py_path, "w")
  
  for item in compile_list:
    file.write(item)

  file.close()

  return "File Exported as \"%s\"\n" %(py_path)

  



def create(name, prefab_name, prefab_text, prefab_icon):

  py_list = []
  ent_py_list = []
  txt_list = []
  ent_list = []
  num_list = []
  id_num_list = []
  id_value_list = []
  value_list = []
  compile_list = [
  """import os

def createTile(posx, posy, id_num, world_id_num, entity_num, placeholder_list):
    
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
""",

  "#INSERT_OPEN_FILE",

  """
    lines = f.readlines() #gathers each line of the prefab and puts numbers them
""",

  "#INSERT_PY_LIST",

  "#INSERT_VAR_COUNT",

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

  "#INSERT_ENT_CODE",
  
  "    return values, id_num, world_id_num, entity_num, ent_values, placeholder_list"
  ]

  ent_code =["#INSERT_ENT_OPEN_FILE",

             """
    lines_ent = g.readlines()
""",

             "#INSERT_ENT_PY_LIST",

             "#INSERT_ENT_VAR_COUNT",

"""
    ent_values = "".join(lines_ent)
    ent_values_split = ent_values.split("\\"")
    valcount = "".join(lines_ent)

    for item in ent_values_split:
        if "entity_name" in item or "parent_name" in item or "door_large" in item:
            placeholder_list.append(item)

    for i in range(valcount.count('world_idnum')):
        ent_values = ent_values.replace('world_idnum', str(world_id_num), 1)
        world_id_num += 1

    for var in ["px", "py", "pz"]:
        for count in range(1,ent_var_count+1):
            string = var + str(count)
            string_var = str(eval(var + str(count)))

            if var == "pz":
                ent_values = ent_values.replace(string + "\\"",string_var + "\\"") #we need to do this or else it will mess up on 2 digit numbers
            else:
                ent_values = ent_values.replace(string + " ",string_var + " ")
                
    for var in ["x", "y", "z"]:
        for count in range(1,var_count+1):
            try:
                string = var + str(count)
                string_var = str(eval(var + str(count)))
                if var == "z":
                    ent_values = ent_values.replace(string + ")",string_var + ")") #we need to do this or else it will mess up on 2 digit numbers
                else:
                    ent_values = ent_values.replace(string + " ",string_var + " ")
            except:
                pass

    for i in range(valcount.count('id_num')):
        ent_values = ent_values.replace('id_num', str(id_num), 1)
        id_num = id_num+1

    for i in range(valcount.count("entity_name")):
        ent_values = ent_values.replace("entity_name", "entity" + str(entity_num), 1)
        ent_values = ent_values.replace("entity_same", "entity" + str(entity_num), 1)
        if "parent_name" in placeholder_list[entity_num]:
            ent_values = ent_values.replace("parent_name", "entity" + str(entity_num), 1)
            placeholder_list.remove(placeholder_list[entity_num])
        if "door_large" in placeholder_list[entity_num]:
            ent_values = ent_values.replace("door_large", "door_large" + str(entity_num), 1)
        if "respawn_name" in placeholder_list[entity_num]:
            ent_values = ent_values.replace("respawn_name", "respawn_name" + str(entity_num), 1)
        entity_num += 1

"""]

  var_num = 1
  ent_var_num = 1
  contains_ent = False #True if there are entities in the vmf
  in_solid_block = False #True if in a solid code block
  in_entity_block = False #True if in an entity code block
  in_editor_block = False #True if in an editor cod (best game omg so good 8)))) block
  in_connections_block = False #True if in a connections code block
  solid_to_ent = False #True if you want to put the solid block into ent_list
  black_list_var = False #True means it IS on the blacklist, False otherwise
  value_list_history = []
  #name = "prefab_template\godplsno.vmf" #name of the vmf file, changed to allow user to open a file
  file = open(name, "r")

  #black_list = ["editorversion",
  #              "editorbuild",
  #              "mapversion",
  #              "formatversion",
  #              "prefab",
  #              "bSnapToGrid",
  #              "bShowGrid",
  #              "bShowLogicalGrid",
  #              "nGridSpacing",
  #              "bShow3DGrid",
  #              "mapversion",
  #              "classname",
  #              "skyname",
  #              "maxpropscreenwidth",
  #              "detailvbsp",
  #              "detailmaterial",
  #              "activecamera",
  #              "mins",
  #              "maxs",
  #              "active"]

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
  ent_path = "prefab_template/" + prefab_name + "_entities.txt"
  py_path = prefab_name + ".py"
  loopernum = 0
  for line in openlines:
    
    #for item in black_list:
    #  if item in line:
    #    black_list_var = True
        
    #if "\t" not in line:
     # createBlackList(line)

    

     
    #if not black_list_var:

    which_list = "txt_list" if not solid_to_ent else "ent_list"
      
    if "\t" in line or "entity" in line:
      
      if in_solid_block and "\t}" not in line or in_solid_block and "\t\t" in line:
        #print(line)
        if "(" not in line:

          if "\"id\"" not in line:
            eval(which_list).append(line)
          elif "\t\t\"id\"" in line:
            for letter in line:
              try:
                number = int(letter)
              except ValueError:
                eval(which_list).append(letter)

            if "\t\t\t" in line:
              eval(which_list).insert(-2, "id_num") #need to insert because it creates a \n at the end of the line
            else: 
              eval(which_list).insert(-2, "world_idnum")

          #print(txt_list)

        elif "(" in line:
          for letter in line:
            #print(letter)
            try:
              number = int(letter)    
              num_list.append(letter)
            except ValueError:
              if letter != "-" and letter != ".":
                eval(which_list).append(letter)
              if letter == " ":
                num_list.append("SEPARATE")
              elif letter == ".":
                num_list.append(".")
              elif letter == "-":
                num_list.append("-")
              elif letter == ")":
                #print(num_list)
                write_var(num_list, eval(which_list), py_list, var_num, value_list_history, in_solid_block, in_entity_block) 
                var_num += 1
                num_list = []
      elif in_solid_block and "\t}" in line and "\t\t" not in line:
        in_solid_block = False
        #print(line)
        eval(which_list).append(line)
        if solid_to_ent:
          ent_list.append("}\n")
        solid_to_ent = False
        #import sys
        #sys.exit()

      elif in_entity_block and "\"" in line:
        #print(line)
        
        if "\"id\"" not in line and "\t\"targetname\"" not in line and "\t\"origin\"" not in line and "\t\"associatedmodel\"" not in line and "\t\"parentname\"" not in line:
          ent_list.append(line)
        elif "\"id\"" in line:
          for letter in line:
            try:
              number = int(letter)
            except ValueError:
              ent_list.append(letter)
                  
          ent_list.insert(-2, "world_idnum")
              
        elif "\t\"targetname\"" in line and "respawn_trigger" not in line:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "entity_name")
        elif "\t\"targetname\"" in line and "respawn_trigger" in line:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "respawn_name")

        elif "\t\"associatedmodel\"" in line:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "entity_same")

        elif "\t\"parentname\"" in line and "\"func_door\"" not in openlines[loopernum-19]: 
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "parent_name")

        elif "\t\"parentname\"" in line and "\"func_door\"" in openlines[loopernum-19]:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
          ent_list.insert(-2, "door_large")
            
        elif "\t\"origin\"" in line:
          nums_yet = False #if True then numbers have been received
          for letter in line:
            
            #print(letter)
            try:
              number = int(letter)    
              num_list.append(letter)
              nums_yet = True
            except ValueError:
              if letter != "-" and letter != ".":
                ent_list.append(letter)
              if letter == " ":
                num_list.append("SEPARATE")
              elif letter == ".":
                num_list.append(".")
              elif letter == "-":
                num_list.append("-")
              elif letter == "\"" and nums_yet:
                write_var(num_list, ent_list, ent_py_list, ent_var_num, value_list_history, in_solid_block, in_entity_block) 
                ent_var_num += 1
                num_list = []
          

      elif in_entity_block and "\"" not in line:
        in_entity_block = False
        if "editor" in line:
          #print(line)
          ent_list.append(line)
          in_editor_block = True
        elif "connections" in line:
          ent_list.append(line)
          in_connections_block = True
        elif "solid" in line:
          solid_to_ent = True

      elif in_editor_block and "\t}" not in line:
        #print(line)
        ent_list.append(line)

      elif in_editor_block and "\t}" in line:
        in_editor_block = False
        ent_list.append(line)
        ent_list.append("}\n")

      elif in_connections_block and "\t}" not in line:
        ent_list.append(line)

      elif in_connections_block and "\t}" in line:
        in_connections_block = False
        ent_list.append(line)
        solid_to_ent = True #IMPORTANT: Might need to change because solid might not always follow connections

      which_list = "txt_list" if not solid_to_ent else "ent_list"
        
                  
      if "solid" in line and "\"" not in line: #or "side" in line:# or "origin" in line: #need to add this because somehow, the solid/side
                        
        eval(which_list).append(line)
        #go until "\t}"
        in_solid_block = True
              
      elif "entity" in line:
        contains_ent = True
        in_entity_block = True
        ent_list.append(line)
        ent_list.append("{\n")

      #elif "editor" in line:
       # in_editor_block = True
        #txt_list.append(line)
                        
                              
    loopernum += 1            
          

    #black_list_var = False

  file.close()
  return compileTXT(txt_path, txt_list, prefab_name, prefab_text, prefab_icon, ent_list, ent_path) + compilePY(py_path, py_list, txt_path, compile_list, contains_ent, ent_code, ent_path, ent_py_list)

#create("vmf_prefabs/spawn_room_blu.vmf", "lol", "lol", "icons/spawn_blue.jpg") 
