def reset(num):
    text_list = ['prefab_template/prefab_text_list.txt','prefab_template/rot_prefab_list.txt',
                 'prefab_template/prefab_list.txt', 'prefab_template/prefab_icon_list.txt']

    for cur in text_list:
        #print(cur)
        file = open(cur, 'r+')
        cur_list = file.readlines()
        length = len(cur_list)-1
        file.seek(0)
        file.truncate()
        #print(length)
        for i in range(num):
            del cur_list[length-i]
        cur_str = "".join(cur_list)
        file.write(cur_str)
        file.close()
