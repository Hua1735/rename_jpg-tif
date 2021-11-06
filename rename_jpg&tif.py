import os

all_dir = os.walk('.')

for dirPath, dirNames, fileNames in all_dir:
    for f in fileNames:
        if '.JPG' in f or '.TIF' in f:
        	abspath_ori = os.path.join(os.path.abspath(dirPath),f)

        	new_name = dirPath[2:] + "_" + f
        	abspath_new = os.path.join(os.path.abspath(dirPath),new_name)

        	print('修改前:', abspath_ori)
        	os.rename(abspath_ori, abspath_new)
        	print('修改後:',abspath_new)