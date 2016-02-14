"""
This program takes a vmf file exported from hammer, then exports both a
prefab txt template (look in prefabs folder), and a .py containing the
algorithms to create the object
"""







py_list = []
txt_list = []
num_list = []
value_list = []

var_num = 1
value_list_history = []
name = "prefabs\godplsno.vmf" #name of the vmf file, will change to allow user to open a file
file = open(name, "r")

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
  name = "prefabs\output.txt" #TODO: make it so that you manually choose file
  file = open(name, "w")
  
  for item in txt_list:
    file.write(item)

  print("File Exported as \"output.txt\"")

def compilePY():
  #This compiles the py file containing the algorithms
  pass


#main loop
for line in openlines:
  if "mins" in line or "maxs" in line: #TODO: maybe make the strings that we don't want to include a list?
    txt_list.append(line)
  else:
    if "(" not in line:
      txt_list.append(line)
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

compileTXT()

      
        
