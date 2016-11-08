''' после восстановления фото с флешкарты
    создалось много файлов
'''

import os
import imghdr
import shutil

directory = '/home/bo/out_dir/jpg/'
r_directory = '/home/bo/img/'
files = os.listdir(directory)

for file_item in files :
    abs_path = directory + file_item
    file_size = os.path.getsize(abs_path)
    if file_size < 60000:
        shutil.move(abs_path, r_directory + 'broken/')
        continue
    if imghdr.what(abs_path) == 'jpeg':
        if file_size < 200000 :
            shutil.move(abs_path, r_directory+ '200k/')
        else :
            if file_size < 400000:
                shutil.move(abs_path, r_directory + '300k/')
            else :
                if file_size < 600000 :
                    shutil.move(abs_path, r_directory + '400k/')
                else :
                    if file_size < 800000:
                        shutil.move(abs_path, r_directory + '600k/')
                    else:
                        if file_size < 1000000:
                            shutil.move(abs_path, r_directory + '800k/')
    else:
        shutil.move(abs_path, r_directory + 'broken/')

