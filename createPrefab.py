"""
This function takes a vmf file exported from hammer, then exports both a
prefab txt template (look in prefab_template folder), and a .py containing the
algorithms to create the object (look in the prefabs folder)
"""

from PIL import Image
import zipfile
import os



def write_var(num_list, txt_list, py_list, var_num, value_list_history, in_solid_block, in_entity_block, rot_py_list, rot_enabled): 
  value_list = []
  #item count needs to be -1 so that the initial "SEPARATE" makes the var 0
  num_count = -1

  for item in num_list:
    if item == "SEPARATE":
      num_count += 1
    else:
      try:
        value_list[num_count] = value_list[num_count] + item
      except IndexError:
        value_list.append(item)

  value_list_history.append(value_list)

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
    
  
    
    py_list_text = ""

    if var == "x" or var == "px":
      negative = 1
    elif var == "y" or var == "py" or var == "neg_y":
      negative = -1
      
    if var == "z" or var == "pz":
      py_list_text = "%s%d = level*448 + %d" %(var, var_num, value)
      py_list.append(py_list_text)
    elif value == 0:
      py_list_text = "%s%d = pos%s*%d*512" %(var, var_num, var[-1] if var.startswith("p") else var, negative)
      py_list.append(py_list_text)
    else:
      py_list_text = "%s%d = pos%s*%d*512 + (%d)" %(var, var_num, var[-1] if var.startswith("p") else var, negative, value)
      py_list.append(py_list_text)

    txt_list[txt_list.index("INSERT_VAR")] = "%s%d" %(var, var_num)

  rot_list = ["#ROT1", "#ROT2", "#ROT3"]

  for item in rot_list:
    if item == "#ROT1":
      degrees = 270
    elif item == "#ROT2":
      degrees = 180
    elif item == "#ROT3":
      degrees = 90
    else:
      degrees = 0
    
    for var in xyz_list:
      if var == "z" or var == "pz":
        rot_py_list_text = "%s%s%d = level*448 + %d" %(item, var, var_num, value)
        rot_py_list.append(rot_py_list_text)
      elif value == 0:
        rot_py_list_text = "%s%s%d = int(rotatePoint((posx*512+256,posy*-1*512-256), (%s, %s), %d)[%d])" %(item, var, var_num, py_list[-3][py_list[-1].index("=") + 2:], py_list[-2][py_list[-1].index("=") + 2:], degrees, 0 if var == "x" or var == "px" else 1)
        rot_py_list.append(rot_py_list_text)
      else:
        rot_py_list_text = "%s%s%d = int(rotatePoint((posx*512+256,posy*-1*512-256), (%s, %s), %d)[%d])" %(item, var, var_num, py_list[-3][py_list[-1].index("=") + 2:], py_list[-2][py_list[-1].index("=") + 2:], degrees, 0 if var == "x" or var == "px" else 1)
        rot_py_list.append(rot_py_list_text)


def compileTXT(txt_path, txt_list, prefab_name, prefab_text, prefab_icon, ent_list, ent_path,indexLine):
  file = open(txt_path, "w")
  global insertBool
  for item in txt_list:
    file.write(item)
  file.close()

  file = open(ent_path, "w")

  for item in ent_list:
    file.write(item)
  file.close
  if insertBool:  
    prefab_file = open("prefab_template/prefab_list.txt", "r")
    prefab_text_file = open("prefab_template/prefab_text_list.txt", "r")
    prefab_icon_file = open("prefab_template/prefab_icon_list.txt", "r")
    prefab_file_contents,prefab_text_file_contents,prefab_icon_file_contents = prefab_file.readlines(),prefab_text_file.readlines(),prefab_icon_file.readlines()
    
    for file in [prefab_file, prefab_text_file, prefab_icon_file]:
      file.close()

    prefab_file_contents.insert(indexLine,prefab_name + "\n")
    prefab_text_file_contents.insert(indexLine,prefab_text + "\n")
    prefab_icon_file_contents.insert(indexLine,prefab_icon + "\n")

    prefab_file_contents = "".join(prefab_file_contents)
    prefab_text_file_contents = "".join(prefab_text_file_contents)
    prefab_icon_file_contents = "".join(prefab_icon_file_contents)
    
    prefab_file = open("prefab_template/prefab_list.txt", "w")
    prefab_text_file = open("prefab_template/prefab_text_list.txt", "w")
    prefab_icon_file = open("prefab_template/prefab_icon_list.txt", "w")
    
    prefab_file.write(prefab_file_contents)
    prefab_text_file.write(prefab_text_file_contents)
    prefab_icon_file.write(prefab_icon_file_contents)
  else:
    prefab_file = open("prefab_template/prefab_list.txt", "a")
    prefab_text_file = open("prefab_template/prefab_text_list.txt", "a")
    prefab_icon_file = open("prefab_template/prefab_icon_list.txt", "a")

    prefab_file.write(prefab_name + "\n")
    prefab_text_file.write(prefab_text + "\n")
    prefab_icon_file.write(prefab_icon + "\n")    

  for file in [prefab_file, prefab_text_file, prefab_icon_file]:
    file.close()

  return "File Exported as \"%s\"\n" %(txt_path)

  
  

def compilePY(py_path, py_list, txt_path, compile_list, contains_ent, ent_code, ent_path, ent_py_list, rot_code, rot_py_list, rot_ent_py_list, rot_enabled):
  if rot_enabled:
    rot_indent = "    "
  else:
    rot_indent = ""
    
  for item in py_list:
    compile_list.insert(compile_list.index("#INSERT_PY_LIST\n"), rot_indent + "    " + item + "\n")

  compile_list[compile_list.index("#INSERT_OPEN_FILE\n")] = "    f = open('%s', 'r+')" %(txt_path)

  compile_list[compile_list.index("#INSERT_PY_LIST\n")] = ""

  var_count = (len(py_list) + 1)

  compile_list[compile_list.index("#INSERT_VAR_COUNT\n")] = "\n    var_count = %d" %(var_count/3)
  
  if rot_enabled:
  
    compile_list.insert(compile_list.index("#INSERT_ROT_IF\n"), rot_code[0][0] + "\n")
    compile_list[compile_list.index("#INSERT_ROT_IF\n")] = ""
    
    ent_code.insert(ent_code.index("#INSERT_ROT_IF\n"), rot_code[1][0] + "\n")
    ent_code[ent_code.index("#INSERT_ROT_IF\n")] = ""

    for item in rot_py_list:
      if "#ROT0" in item:
        rot_code[0].insert(rot_code[0].index("#INSERT_ROT_0_PY_LIST\n"), "        " + item[5:] + "\n")
      elif "#ROT1" in item:
        rot_code[0].insert(rot_code[0].index("#INSERT_ROT_1_PY_LIST\n"), "        " + item[5:] + "\n")
      elif "#ROT2" in item:
        rot_code[0].insert(rot_code[0].index("#INSERT_ROT_2_PY_LIST\n"), "        " + item[5:] + "\n")
      elif "#ROT3" in item:
        rot_code[0].insert(rot_code[0].index("#INSERT_ROT_3_PY_LIST\n"), "        " + item[5:] + "\n")
        
    for index, item in enumerate(rot_code[0]):
      if not index == 0:
        compile_list.insert(compile_list.index("#INSERT_ROT_CODE\n"), item)
        
    compile_list[compile_list.index("#INSERT_ROT_CODE\n")] = ""

      
    for item in rot_ent_py_list:
      if "#ROT0" in item:
        rot_code[1].insert(rot_code[1].index("#INSERT_ROT_0_PY_LIST\n"), "        " + item[5:] + "\n")
      elif "#ROT1" in item:
        rot_code[1].insert(rot_code[1].index("#INSERT_ROT_1_PY_LIST\n"), "        " + item[5:] + "\n")
      elif "#ROT2" in item:
        rot_code[1].insert(rot_code[1].index("#INSERT_ROT_2_PY_LIST\n"), "        " + item[5:] + "\n")
      elif "#ROT3" in item:
        rot_code[1].insert(rot_code[1].index("#INSERT_ROT_3_PY_LIST\n"), "        " + item[5:] + "\n")
        
    for index, item in enumerate(rot_code[1]):
      if not index == 0:
        ent_code.insert(ent_code.index("#INSERT_ROT_ENT_CODE\n"), item)
        
    ent_code[ent_code.index("#INSERT_ROT_ENT_CODE\n")] = ""
    
  
  if contains_ent:
    ent_code[ent_code.index("#INSERT_ENT_OPEN_FILE\n")] = "\n    g = open('%s', 'r+')" %(ent_path)

    for item in ent_py_list:
      ent_code.insert(ent_code.index("#INSERT_ENT_PY_LIST\n"), rot_indent + "    " + item + "\n")

    ent_code[ent_code.index("#INSERT_ENT_PY_LIST\n")] = ""

    ent_var_count = (len(ent_py_list) + 1)

    ent_code[ent_code.index("#INSERT_ENT_VAR_COUNT\n")] = "    ent_var_count = %d" %(ent_var_count/3)

    for item in ent_code:
      compile_list.insert(compile_list.index("#INSERT_ENT_CODE\n"), item)

    compile_list[compile_list.index("#INSERT_ENT_CODE\n")] = ""

  compile_list.append("\n    return values, id_num, world_id_num, entity_num, ent_values, placeholder_list" if contains_ent else "\n    return values, id_num, world_id_num")

  file = open(py_path, "w")
  
  for item in compile_list:
    file.write(item)

  file.close()

  return "File Exported as \"%s\"\n" %(py_path)

  



def create(name, prefab_name, prefab_text, prefab_icon, rot_enabled, workshop_export,indexLine,index):
  if indexLine == 'END':
    insertBool = False
  else:
    insertBool = True

  py_list = []
  ent_py_list = []
  rot_py_list = []
  rot_ent_py_list = []
  txt_list = []
  ent_list = []
  num_list = []
  id_num_list = []
  id_value_list = []
  value_list = []
  compile_list = [
  """import os
import math

def rotatePoint(centerPoint,point,angle):
    angle = math.radians(angle)
    temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
    return temp_point

def createTile(posx, posy, id_num, world_id_num, entity_num, placeholder_list, rotation, level):
    
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
""",

  "#INSERT_OPEN_FILE\n",

  """
    lines = f.readlines() #gathers each line of the prefab and puts numbers them
""",

  "#INSERT_ROT_IF\n",

  "#INSERT_PY_LIST\n",
  
  "#INSERT_ROT_CODE\n",

  "#INSERT_VAR_COUNT\n",

  """
    values = "".join(lines)#converting list to string
    ogvalues = "".join(lines)

    normal_list,axislist,negaxislist,vaxis,uaxis=[],['1 0 0 1','0 1 0 1','0 0 1 1'],['-1 0 0 1','0 -1 0 1','0 0 -1 1'],0,0
    def evaluate(coords):
        dist_x,dist_y,dist_z = abs(coords[0]),abs(coords[1]),abs(coords[2]),
        if dist_x >= dist_y and dist_x >= dist_z:
            return axislist[0]
        if dist_y >= dist_z:
            return axislist[1]
        return axislist[2]

    def get_normal(coord_list):
        vector_a = (coord_list[1][0]-coord_list[0][0],coord_list[1][1]-coord_list[0][1],coord_list[1][2]-coord_list[0][2])
        vector_b = (coord_list[2][0]-coord_list[0][0],coord_list[2][1]-coord_list[0][1],coord_list[2][2]-coord_list[0][2])
        
        normal = (vector_a[1]*vector_b[2]-vector_a[2]*vector_b[1],vector_a[2]*vector_b[0]-vector_a[0]*vector_b[2],vector_a[0]*vector_b[1]-vector_a[1]*vector_b[0])
        return normal
    
    for normal_num in range(1,var_count+1,3):
        normal_list=[]
        for i in range(3):
            normal_list.append([])
            for var in ["x", "y", "z"]:
                normal_list[i].append(eval(var+str(normal_num+i)))
        coords = get_normal(normal_list)  
        response = evaluate(coords)
        if response == axislist[0]:
            uaxis = axislist[1]
        else:
            uaxis = axislist[0]
        if response == axislist[2]:
            vaxis = negaxislist[1]
        else:
            vaxis = negaxislist[2]
        values = values.replace('AXIS_REPLACE_U',uaxis,1)
        values = values.replace('AXIS_REPLACE_V',vaxis,1)
    
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
        id_num = id_num+1
        if "ROTATION_RIGHT" in values:
            if rotation == 0:
                values = values.replace("ROTATION_RIGHT","0 0 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_RIGHT","0 270 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_RIGHT","0 180 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_RIGHT","0 90 0",1)
        if "ROTATION_UP" in values:
            if rotation == 0:
                values = values.replace("ROTATION_UP","0 90 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_UP","0 0 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_UP","0 270 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_UP","0 180 0",1)
        if "ROTATION_LEFT" in values:
            if rotation == 0:
                values = values.replace("ROTATION_LEFT","0 180 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_LEFT","0 90 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_LEFT","0 0 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_LEFT","0 270 0",1)
        if "ROTATION_DOWN" in values:
            if rotation == 0:
                values = values.replace("ROTATION_DOWN","0 270 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_DOWN","0 180 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_DOWN","0 90 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_DOWN","0 0 0",1)

    values = values.replace('"[0 0 0 1] 0.25"','"[1 1 1 1] 0.25"')
    values = values.replace('"[0 0 1 0] 0.25"','"[1 1 1 1] 0.25"')
    values = values.replace('"[0 1 0 0] 0.25"','"[1 1 1 1] 0.25"')       
    values = values.replace('"[1 0 0 0] 0.25"','"[1 1 1 1] 0.25"')
        
""",

  "#INSERT_ENT_CODE\n",
  
  ]

  ent_code =["#INSERT_ENT_OPEN_FILE\n",

             """
    lines_ent = g.readlines()
""",

             "#INSERT_ROT_IF\n",

             "#INSERT_ENT_PY_LIST\n",

             "#INSERT_ROT_ENT_CODE\n",
             
             "#INSERT_ENT_VAR_COUNT\n",

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

    for i in range(int(valcount.count('laser_target')/2)):
        if "laser_target_plac" in ent_values:
            ent_values = ent_values.replace("laser_target_plac", "laser_target" + str(entity_num), 2)
            entity_num += 1

    for i in range(int(valcount.count('sound'))):
        if "sound_plac" in ent_values:
            ent_values = ent_values.replace("sound_plac", "AmbSound"+str(entity_num), 2)
            ent_values = ent_values.replace("relay_plac", "LogicRelay"+str(entity_num),2)
            entity_num += 1

    for i in range(valcount.count("entity_name")):
        try:
            ent_values = ent_values.replace("entity_name", "entity" + str(entity_num), 1)
            ent_values = ent_values.replace("entity_same", "entity" + str(entity_num), 1)
            if "parent_name" in placeholder_list[entity_num]:
                ent_values = ent_values.replace("parent_name", "entity" + str(entity_num), 1)
                placeholder_list.remove(placeholder_list[entity_num])
            
            if "door_large" in ent_values:
                ent_values = ent_values.replace("door_large", "door_large" + str(entity_num), 4)
            if "\\"respawn_name\\"" in ent_values:
                ent_values = ent_values.replace("\\"respawn_name\\"", "\\"respawn_name" + str(entity_num) + "\\"", 2)
            entity_num += 1
        except Exception as e:
            print(str(e))

    for i in range(valcount.count("ROTATION")):
        if "ROTATION_RIGHT" in ent_values:
            if rotation == 0:
                ent_values = ent_values.replace("ROTATION_RIGHT","0 0 0",1)
            elif rotation == 1:
                ent_values = ent_values.replace("ROTATION_RIGHT","0 270 0",1)
            elif rotation == 2:
                ent_values = ent_values.replace("ROTATION_RIGHT","0 180 0 ",1)
            elif rotation == 3:
                ent_values = ent_values.replace("ROTATION_RIGHT","0 90 0",1)
        if "ROTATION_LEFT" in ent_values:
            if rotation == 0:
                ent_values = ent_values.replace("ROTATION_LEFT","0 180 0",1)
            elif rotation == 1:
                ent_values = ent_values.replace("ROTATION_LEFT","0 90 0",1)
            elif rotation == 2:
                ent_values = ent_values.replace("ROTATION_LEFT","0 0 0",1)
            elif rotation == 3:
                ent_values = ent_values.replace("ROTATION_LEFT","0 270 0",1)
        if "ROTATION_DOWN" in ent_values:
            if rotation == 0:
                ent_values = ent_values.replace("ROTATION_DOWN","0 270 0",1)
            elif rotation == 1:
                ent_values = ent_values.replace("ROTATION_DOWN","0 180 0",1)
            elif rotation == 2:
                ent_values = ent_values.replace("ROTATION_DOWN","0 90 0",1)
            elif rotation == 3:
                ent_values = ent_values.replace("ROTATION_DOWN","0 0 0",1)
        if "ROTATION_UP" in ent_values:
            if rotation == 0:
                ent_values = ent_values.replace("ROTATION_UP","0 90 0",1)
            elif rotation == 1:
                ent_values = ent_values.replace("ROTATION_UP","0 0 0",1)
            elif rotation == 2:
                ent_values = ent_values.replace("ROTATION_UP","0 270 0",1)
            elif rotation == 3:
                ent_values = ent_values.replace("ROTATION_UP","0 180 0",1)

        entity_num += 1
"""]

  rot_code = [["""
    if rotation == 0:
""",
    "#INSERT_ROT_0_PY_LIST\n",
"""
    elif rotation == 1:
""",
    "#INSERT_ROT_1_PY_LIST\n",
"""
    elif rotation == 2:
""",
    "#INSERT_ROT_2_PY_LIST\n",
"""
    elif rotation == 3:
""",
    "#INSERT_ROT_3_PY_LIST\n"],

["""
    if rotation == 0:
""",
    "#INSERT_ROT_0_PY_LIST\n",
"""
    elif rotation == 1:
""",
    "#INSERT_ROT_1_PY_LIST\n",
"""
    elif rotation == 2:
""",
    "#INSERT_ROT_2_PY_LIST\n",
"""
    elif rotation == 3:
""",
    "#INSERT_ROT_3_PY_LIST\n"]]

  var_num = 1
  ent_var_num = 1
  contains_ent = False #True if there are entities in the vmf
  in_solid_block = False #True if in a solid code block
  in_entity_block = False #True if in an entity code block
  in_editor_block = False #True if in an editor cod (i luv dat gme) block
  in_connections_block = False #True if in a connections code block
  solid_to_ent = False #True if you want to put the solid block into ent_list
  black_list_var = False #True means it IS on the blacklist, False otherwise
  value_list_history = []
  #name = "prefab_template\godplsno.vmf" #name of the vmf file, changed to allow user to open a file
  file = open(name, "r")

  openlines = file.readlines()

  prefab_icon_list = prefab_icon.split("/")

  if "easytf2_mapper" in prefab_icon_list:
    del prefab_icon_list[ :prefab_icon_list.index("easytf2_mapper")+1]

    for index, item in enumerate(prefab_icon_list): #enumerate allows you to give 2 vars in the for loop
      if index != len(prefab_icon_list) - 1:
       prefab_icon_list[index] = item + "/" # add the "/" back into the filepath
        
  txt_path = "prefab_template/" + prefab_name + ".txt"
  ent_path = "prefab_template/" + prefab_name + "_entities.txt"
  py_path = "prefabs/" + prefab_name + ".py"
  loopernum = 0
  for line in openlines:

    which_list = "txt_list" if not solid_to_ent else "ent_list"
      
    if "\t" in line or "entity" in line:
      
      if in_solid_block and "\t}" not in line or in_solid_block and "\t\t" in line:
        if "(" not in line:

          if "\"id\"" not in line:
            if "\"uaxis\"" in line:
              quote_num = 0
              for letter in line:
                  if letter == "\"":
                    quote_num += 1
                  if quote_num != 3:
                    eval(which_list).append(letter)
                  elif letter == "\"":
                    eval(which_list).append(letter)
                              
              eval(which_list).insert(-2, "[AXIS_REPLACE_U] 0.25")
            elif "\"vaxis\"" in line:
              quote_num = 0
              for letter in line:
                  if letter == "\"":
                    quote_num += 1
                  if quote_num != 3:
                    eval(which_list).append(letter)
                  elif letter == "\"":
                    eval(which_list).append(letter)
                              
              eval(which_list).insert(-2, "[AXIS_REPLACE_V] 0.25")

            else:
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
        
        elif "(" in line:
          for letter in line:
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
                write_var(num_list, eval(which_list), py_list, var_num, value_list_history, in_solid_block, in_entity_block, rot_py_list, rot_enabled) 
                var_num += 1
                num_list = []

      elif in_solid_block and "\t}" in line and "\t\t" not in line:
        in_solid_block = False

        eval(which_list).append(line)
        if solid_to_ent:
          ent_list.append("}\n")
        solid_to_ent = False


      elif in_entity_block and "\"" in line:

        if "\"id\"" not in line and "\t\"targetname\"" not in line and "\t\"origin\"" not in line and "\t\"associatedmodel\"" not in line and "\t\"parentname\"" not in line and "\t\"respawnroomname\"" not in line and "\"angles\"" not in line and "LaserTarget" not in line:
          ent_list.append(line)
        elif "\"id\"" in line:
          for letter in line:
            try:
              number = int(letter)
            except ValueError:
              ent_list.append(letter)
                  
          ent_list.insert(-2, "world_idnum")

        elif "\"angles\" \"0 0 0\"" in line:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "ROTATION_RIGHT")
        elif '"angles" "0 90 0"' in line:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "ROTATION_UP")
        elif '"angles" "0 180 0"' in line:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "ROTATION_LEFT")
        elif '"angles" "0 270 0"' in line:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "ROTATION_DOWN")
        elif "\t\"targetname\"" in line and "relay" not in line and "ambient_generic" not in openlines[loopernum-17] and "respawn_trigger" not in line and "\"func_door\"" not in openlines[loopernum-19] and "filter_activator_tfteam" not in openlines[loopernum-2] and "info_target" not in openlines[loopernum-3]:
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
        elif "\t\"targetname\"" in line and "filter_blu" in line:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "filter_blu")
        elif "\t\"targetname\"" in line and "relay" in line:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "relay_plac")
        elif "\t\"targetname\"" in line and "ambient_generic" in openlines[loopernum-17]:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "sound_plac")
        elif "\t\"targetname\"" in line and "filter_red" in line:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "filter_red")
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

        elif "\t\"parentname\"" in line and "\"func_door\"" not in openlines[loopernum-19] and "door" not in openlines[loopernum-2]: 
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "parent_name")
        elif "LaserTarget" in line:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "laser_target_plac")

        elif "targetname" in line and "info_target" in openlines[loopernum-3]:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "laser_target_plac")
          
        elif "\t\"parentname\"" in line and "door" in openlines[loopernum-2]: 
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "door_large")
        elif "\t\"targetname\"" in line and "\"func_door\"" in openlines[loopernum-19]:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "door_large")
        elif "\t\"parentname\"" in line and "connections" in openlines[loopernum-3]: 
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "door_large")
        elif "\t\"parentname\"" in line and "connections" in openlines[loopernum-2]: 
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
                        
          ent_list.insert(-2, "door_large")

        elif "\t\"respawnroomname\"" in line:
          quote_num = 0
          for letter in line:
              if letter == "\"":
                quote_num += 1
              if quote_num != 3:
                ent_list.append(letter)
              elif letter == "\"":
                ent_list.append(letter)
          ent_list.insert(-2, "respawn_name")
                
        elif "\t\"origin\"" in line:
          nums_yet = False #if True then numbers have been received
          for letter in line:
            
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
                write_var(num_list, ent_list, ent_py_list, ent_var_num, value_list_history, in_solid_block, in_entity_block, rot_ent_py_list, rot_enabled) 
                ent_var_num += 1
                num_list = []
          

      elif in_entity_block and "\"" not in line:
        in_entity_block = False
        if "editor" in line:
          ent_list.append(line)
          in_editor_block = True
        elif "connections" in line:
          ent_list.append(line)
          in_connections_block = True
        elif "solid" in line:
          solid_to_ent = True

      elif in_editor_block and "\t}" not in line:
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

        
    loopernum += 1            
          


  file.close()
  global insertBool
  if rot_enabled:
    print(prefab_icon)
    ext_list = ["_right.jpg","_down.jpg","_left.jpg","_up.jpg"]
    icondir = str(prefab_name)
    if not insertBool:
        with open("prefab_template/rot_prefab_list.txt", "a") as f:
          f.write(icondir+"_icon_list.txt\n")
          f.close()
    else:
        tempApp = open("prefab_template/rot_prefab_list.txt", "r")
        tempLines = tempApp.readlines()
        tempApp.close()
        tempLines.insert(indexLine,icondir+"_icon_list.txt\n")
        tempLines = "".join(tempLines)
        tempWrite = open("prefab_template/rot_prefab_list.txt", "w")
        tempWrite.write(tempLines)
        tempWrite.close()

    imageRot = Image.open(prefab_icon)
    imageRot.save("icons/"+ icondir+"_right.jpg")
    imageRot2 = Image.open(prefab_icon)
    imageRot2 = imageRot2.rotate(270)
    imageRot2.save("icons/"+ icondir+"_down.jpg")
    imageRot3 = Image.open(prefab_icon)
    imageRot3 = imageRot3.rotate(180)
    imageRot3.save("icons/"+ icondir+"_left.jpg")
    imageRot4 = Image.open(prefab_icon)
    imageRot4 = imageRot4.rotate(90)
    imageRot4.save("icons/"+ icondir+"_up.jpg")
    f = open("prefab_template/iconlists/"+ icondir+"_icon_list.txt","w+")
    for i in ext_list:
      f.write("icons/"+ icondir+i+"\n")
    f.close()

  else:
    icondir = str(prefab_name)
    if not insertBool:
        with open("prefab_template/rot_prefab_list.txt", "a") as f:
          f.write("NO_ROTATION\n")
          f.close()
    else:
        tempApp = open("prefab_template/rot_prefab_list.txt", "r")
        tempLines = tempApp.readlines()
        tempApp.close()
        tempLines.insert(indexLine,"NO_ROTATION\n")
        tempLines = "".join(tempLines)
        tempWrite = open("prefab_template/rot_prefab_list.txt", "w")
        tempWrite.write(tempLines)
        tempWrite.close()
    f = open("prefab_template/iconlists/"+ icondir+"_icon_list.txt","w+")
    for i in range(4):
      f.write("icons/"+icondir+"\n")
    f.close()


  txtReturn = compileTXT(txt_path, txt_list, prefab_name, prefab_text, prefab_icon, ent_list, ent_path,indexLine)
  pyReturn = compilePY(py_path, py_list, txt_path, compile_list, contains_ent, ent_code, ent_path, ent_py_list, rot_code, rot_py_list, rot_ent_py_list, rot_enabled)

  if workshop_export:
    d = open("info.txt","w")
    d.write(icondir+"\n"+prefab_name+"\n"+prefab_text+"\n"+str(index)+"\n")
    d.close()
    with zipfile.ZipFile(prefab_name + '.zip', 'w') as f:
      f.write(txt_path)
      f.write(py_path)

      if rot_enabled:
        f.write("icons/"+ icondir+"_right.jpg")
        f.write("icons/"+ icondir+"_down.jpg")
        f.write("icons/"+ icondir+"_left.jpg")
        f.write("icons/"+ icondir+"_up.jpg")
      else:
        f.write("icons/"+ icondir+".jpg")
      
      if contains_ent:
        f.write(ent_path)

      f.write("prefab_template/iconlists/"+icondir+"_icon_list.txt")
      f.write("info.txt")
      os.remove("info.txt")

  return txtReturn + pyReturn

insertBool = False
