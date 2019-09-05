from os import listdir
from os.path import isfile, join
import os
import shutil
def sort_files_in_a_folder(mypath):    
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    folder = {}
    folder['Dokumenty']=['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx']
    folder['Pliki']=['iso', 'dmg', 'zip', '7z']
    folder['Filmy']=['mkv', 'mp4', 'mpg', 'mpeg']

    for file in files:
        filetype=file.split('.')[1]
        if filetype in folder['Dokumenty']:
            new_folder_name=mypath+'/'+ 'Dokumenty'
            if os.path.isdir(new_folder_name)==True:  #folder exists
                continue
            else:
                os.mkdir(new_folder_name)
        elif filetype in folder['Pliki']:
            new_folder_name=mypath+'/'+ 'Pliki'
            if os.path.isdir(new_folder_name)==True:  #folder exists
                continue
            else:
                os.mkdir(new_folder_name)
        elif filetype in folder['Filmy']:
            new_folder_name=mypath+'/'+ 'Filmy'
            if os.path.isdir(new_folder_name)==True:  #folder exists
                continue
            else:
                os.mkdir(new_folder_name)
        src_path=mypath+'/'+file
        filetype=file.split('.')[1]
        if filetype in folder['Dokumenty']:
            dest_path='Dokumenty'
        elif filetype in folder['Pliki']:
            dest_path='Pliki'
        elif filetype in folder['Filmy']:
            dest_path='Filmy'
        else:
            dest_path='Inne'
            shutil.move(src_path,dest_path)
            print(src_path + '>>>' + dest_path)
if __name__=="__main__":
    mypath='/home/botul/Downloads'
    sort_files_in_a_folder(mypath)
