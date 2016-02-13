"""
This program takes a vmf file exported from hammer, then exports both a
prefab txt template (look in prefabs folder), and a .py containing the
algorithms to create the object
"""






file_list = []
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

  print("num_list: ", num_list)
  
  for item in num_list:
    if item == "SEPARATE":
      num_count += 1
      print(num_count)
    else:
      try:
        value_list[num_count] = value_list[num_count] + item
      except IndexError:
        value_list.append(item)

  print("value_list: ", value_list)
  value_list_history.append(value_list)
  print("value_list_history: ", value_list_history)
  xyz_list = ["x", "y", "z"]
  
  for var in xyz_list:
    
    value = int(value_list[xyz_list.index(var)])

    if var == "x":
      negative = ""
    elif var == "y":
      negative = "-"
        
    if var == "z":
      file_list.append("%s%d = %d" %(var, var_num, value))
      print(file_list)
    elif value == 0:
      file_list.append("%s%d = %s*%s512" %(var, var_num, var, negative))
      print(file_list)
    else:
      file_list.append("%s%d = %s*%s512 + (%d)" %(var, var_num, var, negative, value))
      print(file_list)
  

    #elif value == 0:
      #file_list.append("%s%d = %s*%s512" %(var, var_num, var, negative))
      #print(file_list)
    #elif value == 512:
      #file_list.append("%s%d = %s*%s512 + 512" %(var, var_num, var, negative))
      #print(file_list)
    #elif value == -512:
      #file_list.append("%s%d = %s*%s512 - 512" %(var, var_num, var, negative))
      #print(file_list)

def compileTXT():
  #This compiles the txt prefab template
  pass

def compilePY():
  #This compiles the py file containing the algorithms
  pass


#main loop
for line in openlines:
  if "(" in line:
    for letter in line:
      print(letter)
      try:
        number = int(letter)
        num_list.append(letter)
      except ValueError:
        if letter == " ":
          num_list.append("SEPARATE")
        elif letter == "-":
          num_list.append("-")
        elif letter == ")":
          write_var()
          var_num += 1
          num_list = []

      
        
