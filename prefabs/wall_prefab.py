import os
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
    f = open('prefab_template/wall_prefab.txt', 'r+')
    lines = f.readlines() #gathers each line of the prefab and puts numbers them

    if rotation == 0:

        x1 = posx*1*512
        y1 = posy*-1*512
        z1 = level*512 + 64
        x2 = posx*1*512 + (512)
        y2 = posy*-1*512
        z2 = level*512 + 64
        x3 = posx*1*512 + (512)
        y3 = posy*-1*512 + (-512)
        z3 = level*512 + 64
        x4 = posx*1*512
        y4 = posy*-1*512 + (-512)
        z4 = level*512 + 0
        x5 = posx*1*512 + (512)
        y5 = posy*-1*512 + (-512)
        z5 = level*512 + 0
        x6 = posx*1*512 + (512)
        y6 = posy*-1*512
        z6 = level*512 + 0
        x7 = posx*1*512
        y7 = posy*-1*512
        z7 = level*512 + 64
        x8 = posx*1*512
        y8 = posy*-1*512 + (-512)
        z8 = level*512 + 64
        x9 = posx*1*512
        y9 = posy*-1*512 + (-512)
        z9 = level*512 + 0
        x10 = posx*1*512 + (512)
        y10 = posy*-1*512
        z10 = level*512 + 0
        x11 = posx*1*512 + (512)
        y11 = posy*-1*512 + (-512)
        z11 = level*512 + 0
        x12 = posx*1*512 + (512)
        y12 = posy*-1*512 + (-512)
        z12 = level*512 + 64
        x13 = posx*1*512 + (512)
        y13 = posy*-1*512
        z13 = level*512 + 64
        x14 = posx*1*512
        y14 = posy*-1*512
        z14 = level*512 + 64
        x15 = posx*1*512
        y15 = posy*-1*512
        z15 = level*512 + 0
        x16 = posx*1*512 + (512)
        y16 = posy*-1*512 + (-512)
        z16 = level*512 + 0
        x17 = posx*1*512
        y17 = posy*-1*512 + (-512)
        z17 = level*512 + 0
        x18 = posx*1*512
        y18 = posy*-1*512 + (-512)
        z18 = level*512 + 64
        x19 = posx*1*512 + (448)
        y19 = posy*-1*512
        z19 = level*512 + 320
        x20 = posx*1*512 + (512)
        y20 = posy*-1*512
        z20 = level*512 + 320
        x21 = posx*1*512 + (512)
        y21 = posy*-1*512 + (-512)
        z21 = level*512 + 320
        x22 = posx*1*512 + (448)
        y22 = posy*-1*512 + (-512)
        z22 = level*512 + 64
        x23 = posx*1*512 + (512)
        y23 = posy*-1*512 + (-512)
        z23 = level*512 + 64
        x24 = posx*1*512 + (512)
        y24 = posy*-1*512
        z24 = level*512 + 64
        x25 = posx*1*512 + (448)
        y25 = posy*-1*512
        z25 = level*512 + 320
        x26 = posx*1*512 + (448)
        y26 = posy*-1*512 + (-512)
        z26 = level*512 + 320
        x27 = posx*1*512 + (448)
        y27 = posy*-1*512 + (-512)
        z27 = level*512 + 64
        x28 = posx*1*512 + (512)
        y28 = posy*-1*512
        z28 = level*512 + 64
        x29 = posx*1*512 + (512)
        y29 = posy*-1*512 + (-512)
        z29 = level*512 + 64
        x30 = posx*1*512 + (512)
        y30 = posy*-1*512 + (-512)
        z30 = level*512 + 320
        x31 = posx*1*512 + (512)
        y31 = posy*-1*512
        z31 = level*512 + 320
        x32 = posx*1*512 + (448)
        y32 = posy*-1*512
        z32 = level*512 + 320
        x33 = posx*1*512 + (448)
        y33 = posy*-1*512
        z33 = level*512 + 64
        x34 = posx*1*512 + (512)
        y34 = posy*-1*512 + (-512)
        z34 = level*512 + 64
        x35 = posx*1*512 + (448)
        y35 = posy*-1*512 + (-512)
        z35 = level*512 + 64
        x36 = posx*1*512 + (448)
        y36 = posy*-1*512 + (-512)
        z36 = level*512 + 320
#INSERT_ROT_0_PY_LIST

    elif rotation == 1:
        x1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[0])
        y1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[1])
        z1 = level*512 + level*512 + 64
        x2 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[0])
        y2 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[1])
        z2 = level*512 + level*512 + 64
        x3 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y3 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z3 = level*512 + level*512 + 64
        x4 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[0])
        y4 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[1])
        z4 = level*512 + level*512 + 0
        x5 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y5 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z5 = level*512 + level*512 + 0
        x6 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[0])
        y6 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[1])
        z6 = level*512 + level*512 + 0
        x7 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[0])
        y7 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[1])
        z7 = level*512 + level*512 + 64
        x8 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[0])
        y8 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[1])
        z8 = level*512 + level*512 + 64
        x9 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[0])
        y9 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[1])
        z9 = level*512 + level*512 + 0
        x10 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[0])
        y10 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[1])
        z10 = level*512 + level*512 + 0
        x11 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y11 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z11 = level*512 + level*512 + 0
        x12 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y12 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z12 = level*512 + level*512 + 64
        x13 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[0])
        y13 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[1])
        z13 = level*512 + level*512 + 64
        x14 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[0])
        y14 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[1])
        z14 = level*512 + level*512 + 64
        x15 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[0])
        y15 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[1])
        z15 = level*512 + level*512 + 0
        x16 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y16 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z16 = level*512 + level*512 + 0
        x17 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[0])
        y17 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[1])
        z17 = level*512 + level*512 + 0
        x18 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[0])
        y18 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[1])
        z18 = level*512 + level*512 + 64
        x19 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 270)[0])
        y19 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 270)[1])
        z19 = level*512 + level*512 + 320
        x20 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[0])
        y20 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[1])
        z20 = level*512 + level*512 + 320
        x21 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y21 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z21 = level*512 + level*512 + 320
        x22 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 270)[0])
        y22 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 270)[1])
        z22 = level*512 + level*512 + 64
        x23 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y23 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z23 = level*512 + level*512 + 64
        x24 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[0])
        y24 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[1])
        z24 = level*512 + level*512 + 64
        x25 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 270)[0])
        y25 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 270)[1])
        z25 = level*512 + level*512 + 320
        x26 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 270)[0])
        y26 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 270)[1])
        z26 = level*512 + level*512 + 320
        x27 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 270)[0])
        y27 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 270)[1])
        z27 = level*512 + level*512 + 64
        x28 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[0])
        y28 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[1])
        z28 = level*512 + level*512 + 64
        x29 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y29 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z29 = level*512 + level*512 + 64
        x30 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y30 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z30 = level*512 + level*512 + 320
        x31 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[0])
        y31 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[1])
        z31 = level*512 + level*512 + 320
        x32 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 270)[0])
        y32 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 270)[1])
        z32 = level*512 + level*512 + 320
        x33 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 270)[0])
        y33 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 270)[1])
        z33 = level*512 + level*512 + 64
        x34 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y34 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z34 = level*512 + level*512 + 64
        x35 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 270)[0])
        y35 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 270)[1])
        z35 = level*512 + level*512 + 64
        x36 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 270)[0])
        y36 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 270)[1])
        z36 = level*512 + level*512 + 320
#INSERT_ROT_1_PY_LIST

    elif rotation == 2:
        x1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[0])
        y1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[1])
        z1 = level*512 + level*512 + 64
        x2 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[0])
        y2 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[1])
        z2 = level*512 + level*512 + 64
        x3 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y3 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z3 = level*512 + level*512 + 64
        x4 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[0])
        y4 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[1])
        z4 = level*512 + level*512 + 0
        x5 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y5 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z5 = level*512 + level*512 + 0
        x6 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[0])
        y6 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[1])
        z6 = level*512 + level*512 + 0
        x7 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[0])
        y7 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[1])
        z7 = level*512 + level*512 + 64
        x8 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[0])
        y8 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[1])
        z8 = level*512 + level*512 + 64
        x9 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[0])
        y9 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[1])
        z9 = level*512 + level*512 + 0
        x10 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[0])
        y10 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[1])
        z10 = level*512 + level*512 + 0
        x11 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y11 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z11 = level*512 + level*512 + 0
        x12 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y12 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z12 = level*512 + level*512 + 64
        x13 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[0])
        y13 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[1])
        z13 = level*512 + level*512 + 64
        x14 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[0])
        y14 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[1])
        z14 = level*512 + level*512 + 64
        x15 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[0])
        y15 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[1])
        z15 = level*512 + level*512 + 0
        x16 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y16 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z16 = level*512 + level*512 + 0
        x17 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[0])
        y17 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[1])
        z17 = level*512 + level*512 + 0
        x18 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[0])
        y18 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[1])
        z18 = level*512 + level*512 + 64
        x19 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 180)[0])
        y19 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 180)[1])
        z19 = level*512 + level*512 + 320
        x20 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[0])
        y20 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[1])
        z20 = level*512 + level*512 + 320
        x21 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y21 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z21 = level*512 + level*512 + 320
        x22 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 180)[0])
        y22 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 180)[1])
        z22 = level*512 + level*512 + 64
        x23 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y23 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z23 = level*512 + level*512 + 64
        x24 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[0])
        y24 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[1])
        z24 = level*512 + level*512 + 64
        x25 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 180)[0])
        y25 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 180)[1])
        z25 = level*512 + level*512 + 320
        x26 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 180)[0])
        y26 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 180)[1])
        z26 = level*512 + level*512 + 320
        x27 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 180)[0])
        y27 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 180)[1])
        z27 = level*512 + level*512 + 64
        x28 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[0])
        y28 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[1])
        z28 = level*512 + level*512 + 64
        x29 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y29 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z29 = level*512 + level*512 + 64
        x30 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y30 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z30 = level*512 + level*512 + 320
        x31 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[0])
        y31 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[1])
        z31 = level*512 + level*512 + 320
        x32 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 180)[0])
        y32 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 180)[1])
        z32 = level*512 + level*512 + 320
        x33 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 180)[0])
        y33 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 180)[1])
        z33 = level*512 + level*512 + 64
        x34 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y34 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z34 = level*512 + level*512 + 64
        x35 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 180)[0])
        y35 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 180)[1])
        z35 = level*512 + level*512 + 64
        x36 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 180)[0])
        y36 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 180)[1])
        z36 = level*512 + level*512 + 320
#INSERT_ROT_2_PY_LIST

    elif rotation == 3:
        x1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[0])
        y1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[1])
        z1 = level*512 + level*512 + 64
        x2 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[0])
        y2 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[1])
        z2 = level*512 + level*512 + 64
        x3 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y3 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z3 = level*512 + level*512 + 64
        x4 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[0])
        y4 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[1])
        z4 = level*512 + level*512 + 0
        x5 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y5 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z5 = level*512 + level*512 + 0
        x6 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[0])
        y6 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[1])
        z6 = level*512 + level*512 + 0
        x7 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[0])
        y7 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[1])
        z7 = level*512 + level*512 + 64
        x8 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[0])
        y8 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[1])
        z8 = level*512 + level*512 + 64
        x9 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[0])
        y9 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[1])
        z9 = level*512 + level*512 + 0
        x10 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[0])
        y10 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[1])
        z10 = level*512 + level*512 + 0
        x11 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y11 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z11 = level*512 + level*512 + 0
        x12 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y12 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z12 = level*512 + level*512 + 64
        x13 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[0])
        y13 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[1])
        z13 = level*512 + level*512 + 64
        x14 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[0])
        y14 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[1])
        z14 = level*512 + level*512 + 64
        x15 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[0])
        y15 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[1])
        z15 = level*512 + level*512 + 0
        x16 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y16 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z16 = level*512 + level*512 + 0
        x17 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[0])
        y17 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[1])
        z17 = level*512 + level*512 + 0
        x18 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[0])
        y18 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[1])
        z18 = level*512 + level*512 + 64
        x19 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 90)[0])
        y19 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 90)[1])
        z19 = level*512 + level*512 + 320
        x20 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[0])
        y20 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[1])
        z20 = level*512 + level*512 + 320
        x21 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y21 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z21 = level*512 + level*512 + 320
        x22 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 90)[0])
        y22 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 90)[1])
        z22 = level*512 + level*512 + 64
        x23 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y23 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z23 = level*512 + level*512 + 64
        x24 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[0])
        y24 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[1])
        z24 = level*512 + level*512 + 64
        x25 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 90)[0])
        y25 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 90)[1])
        z25 = level*512 + level*512 + 320
        x26 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 90)[0])
        y26 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 90)[1])
        z26 = level*512 + level*512 + 320
        x27 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 90)[0])
        y27 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 90)[1])
        z27 = level*512 + level*512 + 64
        x28 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[0])
        y28 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[1])
        z28 = level*512 + level*512 + 64
        x29 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y29 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z29 = level*512 + level*512 + 64
        x30 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y30 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z30 = level*512 + level*512 + 320
        x31 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[0])
        y31 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[1])
        z31 = level*512 + level*512 + 320
        x32 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 90)[0])
        y32 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 90)[1])
        z32 = level*512 + level*512 + 320
        x33 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 90)[0])
        y33 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512), 90)[1])
        z33 = level*512 + level*512 + 64
        x34 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y34 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z34 = level*512 + level*512 + 64
        x35 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 90)[0])
        y35 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 90)[1])
        z35 = level*512 + level*512 + 64
        x36 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 90)[0])
        y36 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (448), posy*-1*512 + (-512)), 90)[1])
        z36 = level*512 + level*512 + 320
#INSERT_ROT_3_PY_LIST

    var_count = 36
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
        
#INSERT_ENT_CODE

    return values, id_num, world_id_num