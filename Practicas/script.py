import os
import errno

items = ['dir1','dir2']


for item in items:
    try:
        os.mkdir(str(item))
        print("Directory " + str(item) + " created")
    except OSError as e:
        print("Directory " + str(item) + " not created")
        if e.errno != errno.EEXIST:
            raise
