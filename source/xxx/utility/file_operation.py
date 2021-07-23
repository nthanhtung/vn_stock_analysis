import os
import shutil
import glob

def create_dir(dirs):
    for dir in dirs:
        if os.path.isdir(dir):
            print(f"path {dir} already exists")
        else:
            os.mkdir(dir)
            print(f"created path {dir}")
    print("complete operation")
    return True

def copy_latest_file(source_dir, target_dir, new_file_name):
    '''
    scan the latest file in the dir download path
    rename that file with new_file_name
    if new_file_name already exist -> it will be overwrited with new content
    '''
    old_filename = max([source_dir + "\\" + f for f in os.listdir(source_dir)],key=os.path.getctime)
    file_extension = old_filename.split('.')[-1]
    shutil.copy(old_filename,os.path.join(target_dir,f"{new_file_name}.{file_extension}"))
    return True    

def clean_dir(dirs):
    for dir in dirs:    
        for CleanUp in glob.glob(f'{dir}\\*.*'):
            os.remove(CleanUp)
    return True        


