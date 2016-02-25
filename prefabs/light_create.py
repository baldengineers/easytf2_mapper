#does the environment lighting
import os
def replacevalues(light_r,light_g,light_b,light_brightness,world_id_num):
    l = open('prefab_template\light_env_template.txt')
    lines = l.readlines()
    lines_str = "".join(lines)

    for i in range(lines_str.count("world_idnum")):
        lines_str = lines_str.replace('world_idnum', str(world_id_num))
        world_id_num += 1

    lines_str = lines_str.replace("light_r", str(light_r))
    lines_str = lines_str.replace("light_g", str(light_g))
    lines_str = lines_str.replace("light_b", str(light_b))
    lines_str = lines_str.replace("lightbrightness", str(light_brightness))
    return lines_str
