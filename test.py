import os

def createTile(posx, posy, id_num, world_id_num, entity_num):
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
    f = open('prefab_template/test.txt', 'r+')
    lines = f.readlines() #gathers each line of the prefab and puts numbers them
    x1 = posx*512
    y1 = posy*-512
    z1 = 64
    x2 = posx*512 + (512)
    y2 = posy*-512
    z2 = 64
    x3 = posx*512 + (512)
    y3 = posy*-512 + (-512)
    z3 = 64
    x4 = posx*512
    y4 = posy*-512 + (-512)
    z4 = 0
    x5 = posx*512 + (512)
    y5 = posy*-512 + (-512)
    z5 = 0
    x6 = posx*512 + (512)
    y6 = posy*-512
    z6 = 0
    x7 = posx*512
    y7 = posy*-512
    z7 = 64
    x8 = posx*512
    y8 = posy*-512 + (-512)
    z8 = 64
    x9 = posx*512
    y9 = posy*-512 + (-512)
    z9 = 0
    x10 = posx*512 + (512)
    y10 = posy*-512
    z10 = 0
    x11 = posx*512 + (512)
    y11 = posy*-512 + (-512)
    z11 = 0
    x12 = posx*512 + (512)
    y12 = posy*-512 + (-512)
    z12 = 64
    x13 = posx*512 + (512)
    y13 = posy*-512
    z13 = 64
    x14 = posx*512
    y14 = posy*-512
    z14 = 64
    x15 = posx*512
    y15 = posy*-512
    z15 = 0
    x16 = posx*512 + (512)
    y16 = posy*-512 + (-512)
    z16 = 0
    x17 = posx*512
    y17 = posy*-512 + (-512)
    z17 = 0
    x18 = posx*512
    y18 = posy*-512 + (-512)
    z18 = 64
    x19 = posx*512
    y19 = posy*-512
    z19 = 320
    x20 = posx*512 + (512)
    y20 = posy*-512
    z20 = 320
    x21 = posx*512 + (512)
    y21 = posy*-512 + (-64)
    z21 = 320
    x22 = posx*512
    y22 = posy*-512 + (-64)
    z22 = 64
    x23 = posx*512 + (512)
    y23 = posy*-512 + (-64)
    z23 = 64
    x24 = posx*512 + (512)
    y24 = posy*-512
    z24 = 64
    x25 = posx*512
    y25 = posy*-512
    z25 = 320
    x26 = posx*512
    y26 = posy*-512 + (-64)
    z26 = 320
    x27 = posx*512
    y27 = posy*-512 + (-64)
    z27 = 64
    x28 = posx*512 + (512)
    y28 = posy*-512
    z28 = 64
    x29 = posx*512 + (512)
    y29 = posy*-512 + (-64)
    z29 = 64
    x30 = posx*512 + (512)
    y30 = posy*-512 + (-64)
    z30 = 320
    x31 = posx*512 + (512)
    y31 = posy*-512
    z31 = 320
    x32 = posx*512
    y32 = posy*-512
    z32 = 320
    x33 = posx*512
    y33 = posy*-512
    z33 = 64
    x34 = posx*512 + (512)
    y34 = posy*-512 + (-64)
    z34 = 64
    x35 = posx*512
    y35 = posy*-512 + (-64)
    z35 = 64
    x36 = posx*512
    y36 = posy*-512 + (-64)
    z36 = 320
    x37 = posx*512
    y37 = posy*-512 + (-64)
    z37 = 320
    x38 = posx*512 + (64)
    y38 = posy*-512 + (-64)
    z38 = 320
    x39 = posx*512 + (64)
    y39 = posy*-512 + (-448)
    z39 = 320
    x40 = posx*512
    y40 = posy*-512 + (-448)
    z40 = 64
    x41 = posx*512 + (64)
    y41 = posy*-512 + (-448)
    z41 = 64
    x42 = posx*512 + (64)
    y42 = posy*-512 + (-64)
    z42 = 64
    x43 = posx*512
    y43 = posy*-512 + (-64)
    z43 = 320
    x44 = posx*512
    y44 = posy*-512 + (-448)
    z44 = 320
    x45 = posx*512
    y45 = posy*-512 + (-448)
    z45 = 64
    x46 = posx*512 + (64)
    y46 = posy*-512 + (-64)
    z46 = 64
    x47 = posx*512 + (64)
    y47 = posy*-512 + (-448)
    z47 = 64
    x48 = posx*512 + (64)
    y48 = posy*-512 + (-448)
    z48 = 320
    x49 = posx*512 + (64)
    y49 = posy*-512 + (-64)
    z49 = 320
    x50 = posx*512
    y50 = posy*-512 + (-64)
    z50 = 320
    x51 = posx*512
    y51 = posy*-512 + (-64)
    z51 = 64
    x52 = posx*512 + (64)
    y52 = posy*-512 + (-448)
    z52 = 64
    x53 = posx*512
    y53 = posy*-512 + (-448)
    z53 = 64
    x54 = posx*512
    y54 = posy*-512 + (-448)
    z54 = 320
    x55 = posx*512
    y55 = posy*-512 + (-448)
    z55 = 320
    x56 = posx*512 + (512)
    y56 = posy*-512 + (-448)
    z56 = 320
    x57 = posx*512 + (512)
    y57 = posy*-512 + (-512)
    z57 = 320
    x58 = posx*512
    y58 = posy*-512 + (-512)
    z58 = 64
    x59 = posx*512 + (512)
    y59 = posy*-512 + (-512)
    z59 = 64
    x60 = posx*512 + (512)
    y60 = posy*-512 + (-448)
    z60 = 64
    x61 = posx*512
    y61 = posy*-512 + (-448)
    z61 = 320
    x62 = posx*512
    y62 = posy*-512 + (-512)
    z62 = 320
    x63 = posx*512
    y63 = posy*-512 + (-512)
    z63 = 64
    x64 = posx*512 + (512)
    y64 = posy*-512 + (-448)
    z64 = 64
    x65 = posx*512 + (512)
    y65 = posy*-512 + (-512)
    z65 = 64
    x66 = posx*512 + (512)
    y66 = posy*-512 + (-512)
    z66 = 320
    x67 = posx*512 + (512)
    y67 = posy*-512 + (-448)
    z67 = 320
    x68 = posx*512
    y68 = posy*-512 + (-448)
    z68 = 320
    x69 = posx*512
    y69 = posy*-512 + (-448)
    z69 = 64
    x70 = posx*512 + (512)
    y70 = posy*-512 + (-512)
    z70 = 64
    x71 = posx*512
    y71 = posy*-512 + (-512)
    z71 = 64
    x72 = posx*512
    y72 = posy*-512 + (-512)
    z72 = 320
    x73 = posx*512 + (64)
    y73 = posy*-512 + (-64)
    z73 = 320
    x74 = posx*512 + (512)
    y74 = posy*-512 + (-64)
    z74 = 320
    x75 = posx*512 + (512)
    y75 = posy*-512 + (-448)
    z75 = 320
    x76 = posx*512 + (64)
    y76 = posy*-512 + (-448)
    z76 = 256
    x77 = posx*512 + (512)
    y77 = posy*-512 + (-448)
    z77 = 256
    x78 = posx*512 + (512)
    y78 = posy*-512 + (-64)
    z78 = 256
    x79 = posx*512 + (64)
    y79 = posy*-512 + (-64)
    z79 = 320
    x80 = posx*512 + (64)
    y80 = posy*-512 + (-448)
    z80 = 320
    x81 = posx*512 + (64)
    y81 = posy*-512 + (-448)
    z81 = 256
    x82 = posx*512 + (512)
    y82 = posy*-512 + (-64)
    z82 = 256
    x83 = posx*512 + (512)
    y83 = posy*-512 + (-448)
    z83 = 256
    x84 = posx*512 + (512)
    y84 = posy*-512 + (-448)
    z84 = 320
    x85 = posx*512 + (512)
    y85 = posy*-512 + (-64)
    z85 = 320
    x86 = posx*512 + (64)
    y86 = posy*-512 + (-64)
    z86 = 320
    x87 = posx*512 + (64)
    y87 = posy*-512 + (-64)
    z87 = 256
    x88 = posx*512 + (512)
    y88 = posy*-512 + (-448)
    z88 = 256
    x89 = posx*512 + (64)
    y89 = posy*-512 + (-448)
    z89 = 256
    x90 = posx*512 + (64)
    y90 = posy*-512 + (-448)
    z90 = 320
    x91 = posx*512 + (448)
    y91 = posy*-512 + (-64)
    z91 = 64
    x92 = posx*512 + (448)
    y92 = posy*-512 + (-160)
    z92 = 64
    x93 = posx*512 + (512)
    y93 = posy*-512 + (-160)
    z93 = 64
    x94 = posx*512 + (448)
    y94 = posy*-512 + (-160)
    z94 = 64
    x95 = posx*512 + (448)
    y95 = posy*-512 + (-64)
    z95 = 64
    x96 = posx*512 + (448)
    y96 = posy*-512 + (-64)
    z96 = 192
    x97 = posx*512 + (512)
    y97 = posy*-512 + (-64)
    z97 = 192
    x98 = posx*512 + (512)
    y98 = posy*-512 + (-64)
    z98 = 64
    x99 = posx*512 + (512)
    y99 = posy*-512 + (-160)
    z99 = 64
    x100 = posx*512 + (448)
    y100 = posy*-512 + (-64)
    z100 = 192
    x101 = posx*512 + (448)
    y101 = posy*-512 + (-64)
    z101 = 64
    x102 = posx*512 + (512)
    y102 = posy*-512 + (-64)
    z102 = 64
    x103 = posx*512 + (448)
    y103 = posy*-512 + (-160)
    z103 = 192
    x104 = posx*512 + (448)
    y104 = posy*-512 + (-64)
    z104 = 192
    x105 = posx*512 + (512)
    y105 = posy*-512 + (-64)
    z105 = 192
    x106 = posx*512 + (512)
    y106 = posy*-512 + (-160)
    z106 = 192
    x107 = posx*512 + (512)
    y107 = posy*-512 + (-160)
    z107 = 64
    x108 = posx*512 + (448)
    y108 = posy*-512 + (-160)
    z108 = 64
    x109 = posx*512 + (448)
    y109 = posy*-512 + (-160)
    z109 = 256
    x110 = posx*512 + (448)
    y110 = posy*-512 + (-64)
    z110 = 256
    x111 = posx*512 + (512)
    y111 = posy*-512 + (-64)
    z111 = 256
    x112 = posx*512 + (448)
    y112 = posy*-512 + (-64)
    z112 = 192
    x113 = posx*512 + (448)
    y113 = posy*-512 + (-64)
    z113 = 256
    x114 = posx*512 + (448)
    y114 = posy*-512 + (-160)
    z114 = 256
    x115 = posx*512 + (512)
    y115 = posy*-512 + (-160)
    z115 = 256
    x116 = posx*512 + (512)
    y116 = posy*-512 + (-64)
    z116 = 256
    x117 = posx*512 + (512)
    y117 = posy*-512 + (-64)
    z117 = 192
    x118 = posx*512 + (512)
    y118 = posy*-512 + (-64)
    z118 = 192
    x119 = posx*512 + (512)
    y119 = posy*-512 + (-64)
    z119 = 256
    x120 = posx*512 + (448)
    y120 = posy*-512 + (-64)
    z120 = 256
    x121 = posx*512 + (448)
    y121 = posy*-512 + (-64)
    z121 = 192
    x122 = posx*512 + (448)
    y122 = posy*-512 + (-160)
    z122 = 192
    x123 = posx*512 + (512)
    y123 = posy*-512 + (-160)
    z123 = 192
    x124 = posx*512 + (448)
    y124 = posy*-512 + (-160)
    z124 = 192
    x125 = posx*512 + (448)
    y125 = posy*-512 + (-160)
    z125 = 256
    x126 = posx*512 + (512)
    y126 = posy*-512 + (-160)
    z126 = 256
    x127 = posx*512 + (448)
    y127 = posy*-512 + (-352)
    z127 = 256
    x128 = posx*512 + (448)
    y128 = posy*-512 + (-160)
    z128 = 256
    x129 = posx*512 + (512)
    y129 = posy*-512 + (-160)
    z129 = 256
    x130 = posx*512 + (448)
    y130 = posy*-512 + (-160)
    z130 = 256
    x131 = posx*512 + (448)
    y131 = posy*-512 + (-352)
    z131 = 256
    x132 = posx*512 + (448)
    y132 = posy*-512 + (-352)
    z132 = 192
    x133 = posx*512 + (512)
    y133 = posy*-512 + (-352)
    z133 = 192
    x134 = posx*512 + (512)
    y134 = posy*-512 + (-352)
    z134 = 256
    x135 = posx*512 + (512)
    y135 = posy*-512 + (-160)
    z135 = 256
    x136 = posx*512 + (448)
    y136 = posy*-512 + (-352)
    z136 = 192
    x137 = posx*512 + (448)
    y137 = posy*-512 + (-352)
    z137 = 256
    x138 = posx*512 + (512)
    y138 = posy*-512 + (-352)
    z138 = 256
    x139 = posx*512 + (448)
    y139 = posy*-512 + (-160)
    z139 = 192
    x140 = posx*512 + (448)
    y140 = posy*-512 + (-352)
    z140 = 192
    x141 = posx*512 + (512)
    y141 = posy*-512 + (-352)
    z141 = 192
    x142 = posx*512 + (512)
    y142 = posy*-512 + (-160)
    z142 = 192
    x143 = posx*512 + (512)
    y143 = posy*-512 + (-160)
    z143 = 256
    x144 = posx*512 + (448)
    y144 = posy*-512 + (-160)
    z144 = 256
    x145 = posx*512 + (448)
    y145 = posy*-512 + (-352)
    z145 = 64
    x146 = posx*512 + (448)
    y146 = posy*-512 + (-448)
    z146 = 64
    x147 = posx*512 + (512)
    y147 = posy*-512 + (-448)
    z147 = 64
    x148 = posx*512 + (448)
    y148 = posy*-512 + (-448)
    z148 = 64
    x149 = posx*512 + (448)
    y149 = posy*-512 + (-352)
    z149 = 64
    x150 = posx*512 + (448)
    y150 = posy*-512 + (-352)
    z150 = 192
    x151 = posx*512 + (512)
    y151 = posy*-512 + (-352)
    z151 = 64
    x152 = posx*512 + (512)
    y152 = posy*-512 + (-448)
    z152 = 64
    x153 = posx*512 + (512)
    y153 = posy*-512 + (-448)
    z153 = 192
    x154 = posx*512 + (512)
    y154 = posy*-512 + (-448)
    z154 = 64
    x155 = posx*512 + (448)
    y155 = posy*-512 + (-448)
    z155 = 64
    x156 = posx*512 + (448)
    y156 = posy*-512 + (-448)
    z156 = 192
    x157 = posx*512 + (448)
    y157 = posy*-512 + (-352)
    z157 = 64
    x158 = posx*512 + (512)
    y158 = posy*-512 + (-352)
    z158 = 64
    x159 = posx*512 + (512)
    y159 = posy*-512 + (-352)
    z159 = 192
    x160 = posx*512 + (448)
    y160 = posy*-512 + (-448)
    z160 = 192
    x161 = posx*512 + (448)
    y161 = posy*-512 + (-352)
    z161 = 192
    x162 = posx*512 + (512)
    y162 = posy*-512 + (-352)
    z162 = 192
    x163 = posx*512 + (448)
    y163 = posy*-512 + (-448)
    z163 = 256
    x164 = posx*512 + (448)
    y164 = posy*-512 + (-352)
    z164 = 256
    x165 = posx*512 + (512)
    y165 = posy*-512 + (-352)
    z165 = 256
    x166 = posx*512 + (448)
    y166 = posy*-512 + (-352)
    z166 = 192
    x167 = posx*512 + (448)
    y167 = posy*-512 + (-352)
    z167 = 256
    x168 = posx*512 + (448)
    y168 = posy*-512 + (-448)
    z168 = 256
    x169 = posx*512 + (512)
    y169 = posy*-512 + (-448)
    z169 = 192
    x170 = posx*512 + (512)
    y170 = posy*-512 + (-448)
    z170 = 256
    x171 = posx*512 + (512)
    y171 = posy*-512 + (-352)
    z171 = 256
    x172 = posx*512 + (448)
    y172 = posy*-512 + (-448)
    z172 = 192
    x173 = posx*512 + (448)
    y173 = posy*-512 + (-448)
    z173 = 256
    x174 = posx*512 + (512)
    y174 = posy*-512 + (-448)
    z174 = 256
    x175 = posx*512 + (512)
    y175 = posy*-512 + (-352)
    z175 = 192
    x176 = posx*512 + (512)
    y176 = posy*-512 + (-352)
    z176 = 256
    x177 = posx*512 + (448)
    y177 = posy*-512 + (-352)
    z177 = 256
    x178 = posx*512 + (448)
    y178 = posy*-512 + (-352)
    z178 = 192
    x179 = posx*512 + (448)
    y179 = posy*-512 + (-448)
    z179 = 192
    x180 = posx*512 + (512)
    y180 = posy*-512 + (-448)
    z180 = 192
    x181 = posx*512 + (448)
    y181 = posy*-512 + (-352)
    z181 = 184
    x182 = posx*512 + (448)
    y182 = posy*-512 + (-448)
    z182 = 184
    x183 = posx*512 + (352)
    y183 = posy*-512 + (-448)
    z183 = 184
    x184 = posx*512 + (448)
    y184 = posy*-512 + (-448)
    z184 = 56
    x185 = posx*512 + (448)
    y185 = posy*-512 + (-352)
    z185 = 56
    x186 = posx*512 + (352)
    y186 = posy*-512 + (-352)
    z186 = 56
    x187 = posx*512 + (448)
    y187 = posy*-512 + (-352)
    z187 = 56
    x188 = posx*512 + (448)
    y188 = posy*-512 + (-448)
    z188 = 56
    x189 = posx*512 + (448)
    y189 = posy*-512 + (-448)
    z189 = 184
    x190 = posx*512 + (352)
    y190 = posy*-512 + (-448)
    z190 = 56
    x191 = posx*512 + (352)
    y191 = posy*-512 + (-352)
    z191 = 56
    x192 = posx*512 + (352)
    y192 = posy*-512 + (-352)
    z192 = 184
    x193 = posx*512 + (448)
    y193 = posy*-512 + (-448)
    z193 = 56
    x194 = posx*512 + (352)
    y194 = posy*-512 + (-448)
    z194 = 56
    x195 = posx*512 + (352)
    y195 = posy*-512 + (-448)
    z195 = 184
    x196 = posx*512 + (352)
    y196 = posy*-512 + (-352)
    z196 = 56
    x197 = posx*512 + (448)
    y197 = posy*-512 + (-352)
    z197 = 56
    x198 = posx*512 + (448)
    y198 = posy*-512 + (-352)
    z198 = 184
    x199 = posx*512 + (352)
    y199 = posy*-512 + (-160)
    z199 = 184
    x200 = posx*512 + (352)
    y200 = posy*-512 + (-64)
    z200 = 184
    x201 = posx*512 + (448)
    y201 = posy*-512 + (-64)
    z201 = 184
    x202 = posx*512 + (352)
    y202 = posy*-512 + (-64)
    z202 = 56
    x203 = posx*512 + (352)
    y203 = posy*-512 + (-160)
    z203 = 56
    x204 = posx*512 + (448)
    y204 = posy*-512 + (-160)
    z204 = 56
    x205 = posx*512 + (352)
    y205 = posy*-512 + (-160)
    z205 = 56
    x206 = posx*512 + (352)
    y206 = posy*-512 + (-64)
    z206 = 56
    x207 = posx*512 + (352)
    y207 = posy*-512 + (-64)
    z207 = 184
    x208 = posx*512 + (448)
    y208 = posy*-512 + (-64)
    z208 = 56
    x209 = posx*512 + (448)
    y209 = posy*-512 + (-160)
    z209 = 56
    x210 = posx*512 + (448)
    y210 = posy*-512 + (-160)
    z210 = 184
    x211 = posx*512 + (352)
    y211 = posy*-512 + (-64)
    z211 = 56
    x212 = posx*512 + (448)
    y212 = posy*-512 + (-64)
    z212 = 56
    x213 = posx*512 + (448)
    y213 = posy*-512 + (-64)
    z213 = 184
    x214 = posx*512 + (448)
    y214 = posy*-512 + (-160)
    z214 = 56
    x215 = posx*512 + (352)
    y215 = posy*-512 + (-160)
    z215 = 56
    x216 = posx*512 + (352)
    y216 = posy*-512 + (-160)
    z216 = 184
    x217 = posx*512 + (448)
    y217 = posy*-512 + (-64)
    z217 = 256
    x218 = posx*512 + (448)
    y218 = posy*-512 + (-448)
    z218 = 256
    x219 = posx*512 + (64)
    y219 = posy*-512 + (-448)
    z219 = 256
    x220 = posx*512 + (448)
    y220 = posy*-512 + (-448)
    z220 = 64
    x221 = posx*512 + (448)
    y221 = posy*-512 + (-64)
    z221 = 64
    x222 = posx*512 + (64)
    y222 = posy*-512 + (-64)
    z222 = 64
    x223 = posx*512 + (448)
    y223 = posy*-512 + (-64)
    z223 = 64
    x224 = posx*512 + (448)
    y224 = posy*-512 + (-448)
    z224 = 64
    x225 = posx*512 + (448)
    y225 = posy*-512 + (-448)
    z225 = 256
    x226 = posx*512 + (64)
    y226 = posy*-512 + (-448)
    z226 = 64
    x227 = posx*512 + (64)
    y227 = posy*-512 + (-64)
    z227 = 64
    x228 = posx*512 + (64)
    y228 = posy*-512 + (-64)
    z228 = 256
    x229 = posx*512 + (448)
    y229 = posy*-512 + (-448)
    z229 = 64
    x230 = posx*512 + (64)
    y230 = posy*-512 + (-448)
    z230 = 64
    x231 = posx*512 + (64)
    y231 = posy*-512 + (-448)
    z231 = 256
    x232 = posx*512 + (64)
    y232 = posy*-512 + (-64)
    z232 = 64
    x233 = posx*512 + (448)
    y233 = posy*-512 + (-64)
    z233 = 64
    x234 = posx*512 + (448)
    y234 = posy*-512 + (-64)
    z234 = 256
    x235 = posx*512 + (512)
    y235 = posy*-512 + (-160)
    z235 = 176
    x236 = posx*512 + (512)
    y236 = posy*-512 + (-352)
    z236 = 176
    x237 = posx*512 + (496)
    y237 = posy*-512 + (-352)
    z237 = 176
    x238 = posx*512 + (512)
    y238 = posy*-512 + (-352)
    z238 = 64
    x239 = posx*512 + (512)
    y239 = posy*-512 + (-160)
    z239 = 64
    x240 = posx*512 + (496)
    y240 = posy*-512 + (-160)
    z240 = 64
    x241 = posx*512 + (496)
    y241 = posy*-512 + (-352)
    z241 = 64
    x242 = posx*512 + (496)
    y242 = posy*-512 + (-160)
    z242 = 64
    x243 = posx*512 + (496)
    y243 = posy*-512 + (-160)
    z243 = 176
    x244 = posx*512 + (512)
    y244 = posy*-512 + (-160)
    z244 = 64
    x245 = posx*512 + (512)
    y245 = posy*-512 + (-352)
    z245 = 64
    x246 = posx*512 + (512)
    y246 = posy*-512 + (-352)
    z246 = 176
    x247 = posx*512 + (496)
    y247 = posy*-512 + (-160)
    z247 = 64
    x248 = posx*512 + (512)
    y248 = posy*-512 + (-160)
    z248 = 64
    x249 = posx*512 + (512)
    y249 = posy*-512 + (-160)
    z249 = 176
    x250 = posx*512 + (512)
    y250 = posy*-512 + (-352)
    z250 = 64
    x251 = posx*512 + (496)
    y251 = posy*-512 + (-352)
    z251 = 64
    x252 = posx*512 + (496)
    y252 = posy*-512 + (-352)
    z252 = 176
    x253 = posx*512 + (368)
    y253 = posy*-512 + (-384)
    z253 = 208
    x254 = posx*512 + (368)
    y254 = posy*-512 + (-128)
    z254 = 208
    x255 = posx*512 + (624)
    y255 = posy*-512 + (-128)
    z255 = 208
    x256 = posx*512 + (368)
    y256 = posy*-512 + (-128)
    z256 = 48
    x257 = posx*512 + (368)
    y257 = posy*-512 + (-384)
    z257 = 48
    x258 = posx*512 + (624)
    y258 = posy*-512 + (-384)
    z258 = 48
    x259 = posx*512 + (368)
    y259 = posy*-512 + (-384)
    z259 = 48
    x260 = posx*512 + (368)
    y260 = posy*-512 + (-128)
    z260 = 48
    x261 = posx*512 + (368)
    y261 = posy*-512 + (-128)
    z261 = 208
    x262 = posx*512 + (624)
    y262 = posy*-512 + (-128)
    z262 = 48
    x263 = posx*512 + (624)
    y263 = posy*-512 + (-384)
    z263 = 48
    x264 = posx*512 + (624)
    y264 = posy*-512 + (-384)
    z264 = 208
    x265 = posx*512 + (368)
    y265 = posy*-512 + (-128)
    z265 = 48
    x266 = posx*512 + (624)
    y266 = posy*-512 + (-128)
    z266 = 48
    x267 = posx*512 + (624)
    y267 = posy*-512 + (-128)
    z267 = 208
    x268 = posx*512 + (624)
    y268 = posy*-512 + (-384)
    z268 = 48
    x269 = posx*512 + (368)
    y269 = posy*-512 + (-384)
    z269 = 48
    x270 = posx*512 + (368)
    y270 = posy*-512 + (-384)
    z270 = 208
    x271 = posx*512 + (497)
    y271 = posy*-512 + (-352)
    z271 = 181
    x272 = posx*512 + (497)
    y272 = posy*-512 + (-160)
    z272 = 181
    x273 = posx*512 + (499)
    y273 = posy*-512 + (-160)
    z273 = 181
    x274 = posx*512 + (497)
    y274 = posy*-512 + (-160)
    z274 = 64
    x275 = posx*512 + (497)
    y275 = posy*-512 + (-352)
    z275 = 64
    x276 = posx*512 + (499)
    y276 = posy*-512 + (-352)
    z276 = 64
    x277 = posx*512 + (497)
    y277 = posy*-512 + (-352)
    z277 = 64
    x278 = posx*512 + (497)
    y278 = posy*-512 + (-160)
    z278 = 64
    x279 = posx*512 + (497)
    y279 = posy*-512 + (-160)
    z279 = 181
    x280 = posx*512 + (499)
    y280 = posy*-512 + (-160)
    z280 = 64
    x281 = posx*512 + (499)
    y281 = posy*-512 + (-352)
    z281 = 64
    x282 = posx*512 + (499)
    y282 = posy*-512 + (-352)
    z282 = 181
    x283 = posx*512 + (497)
    y283 = posy*-512 + (-160)
    z283 = 64
    x284 = posx*512 + (499)
    y284 = posy*-512 + (-160)
    z284 = 64
    x285 = posx*512 + (499)
    y285 = posy*-512 + (-160)
    z285 = 181
    x286 = posx*512 + (499)
    y286 = posy*-512 + (-352)
    z286 = 64
    x287 = posx*512 + (497)
    y287 = posy*-512 + (-352)
    z287 = 64
    x288 = posx*512 + (497)
    y288 = posy*-512 + (-352)
    z288 = 181
    var_count = 288
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
    g = open('prefab_template/test_entities.txt', 'r+')
    lines_ent = g.readlines()
    px1 = posx*512 + (400)
    py1 = posy*-512 + (-431)
    pz1 = 56
    px2 = posx*512 + (400)
    py2 = posy*-512 + (-80)
    pz2 = 56
    px3 = posx*512 + (287)
    py3 = posy*-512 + (-351)
    pz3 = 73
    px4 = posx*512 + (287)
    py4 = posy*-512 + (-287)
    pz4 = 73
    px5 = posx*512 + (287)
    py5 = posy*-512 + (-223)
    pz5 = 73
    px6 = posx*512 + (287)
    py6 = posy*-512 + (-159)
    pz6 = 73
    px7 = posx*512 + (223)
    py7 = posy*-512 + (-351)
    pz7 = 73
    px8 = posx*512 + (223)
    py8 = posy*-512 + (-287)
    pz8 = 73
    px9 = posx*512 + (223)
    py9 = posy*-512 + (-223)
    pz9 = 73
    px10 = posx*512 + (223)
    py10 = posy*-512 + (-159)
    pz10 = 73
    px11 = posx*512 + (159)
    py11 = posy*-512 + (-351)
    pz11 = 73
    px12 = posx*512 + (159)
    py12 = posy*-512 + (-287)
    pz12 = 73
    px13 = posx*512 + (159)
    py13 = posy*-512 + (-223)
    pz13 = 73
    px14 = posx*512 + (159)
    py14 = posy*-512 + (-159)
    pz14 = 73
    px15 = posx*512 + (95)
    py15 = posy*-512 + (-159)
    pz15 = 73
    px16 = posx*512 + (95)
    py16 = posy*-512 + (-223)
    pz16 = 73
    px17 = posx*512 + (95)
    py17 = posy*-512 + (-287)
    pz17 = 73
    px18 = posx*512 + (95)
    py18 = posy*-512 + (-351)
    pz18 = 73
    px19 = posx*512 + (504)
    py19 = posy*-512 + (-256)
    pz19 = 120
    px20 = posx*512 + (496)
    py20 = posy*-512 + (-256)
    pz20 = 128
    px21 = posx*512 + (498)
    py21 = posy*-512 + (-256)
    pz21 = 128
    px22 = posx*512 + (497)
    py22 = posy*-512 + (-256)
    pz22 = 122
    px23 = posx*512 + (525)
    py23 = posy*-512 + (-256)
    pz23 = 128
    ent_var_count = 23
    ent_values = "".join(lines_ent)
    valcount = "".join(lines_ent)

    for i in range(valcount.count('world_idnum')):
        ent_values = ent_values.replace('world_idnum', str(world_id_num), 1)
        world_id_num += 1

    for var in ["px", "py", "pz"]:
        for count in range(1,ent_var_count+1):
            string = var + str(count)
            string_var = str(eval(var + str(count)))

            if var == "pz":
                ent_values = ent_values.replace(string + ")",string_var + ")") #we need to do this or else it will mess up on 2 digit numbers
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
        entity_num += 1

    return values, id_num, world_id_num, entity_num, ent_values