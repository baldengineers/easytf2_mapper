file_list = []
i = 1
name = "prefabs\godplsno.vmf"
file = open(name, "r")
openlines = file.readlines()
openlinesstr = "".join(openlines)

for line in openlinesstr:
  if "(" in line:
    for letter in line:
      try:
        number = int(letter)
      except ValueError:
        continue
      if number == 0:
        file_list.append("%s%d = %s*%s512", "x", i, "x", "")
        print(file_list)
      elif number == 512
        file_list.append("%s%d = %s*%s512 + 512", "x", i, "x", "")
      elif number == -512
        file_list.append("%s%d = %s*%s512 - 512", "y", i, "y", "-")
        
      i++
        
