import glob
import os

name_of_dir = 'dir_path/'
list_of_files = filter( os.path.isfile,
                        glob.glob(name_of_dir + '*') )

list_of_files = sorted( list_of_files,
                        key =  lambda x: os.stat(x).st_size)
