import os
import shutil
import sys
dir_path = r'C:\\Users\\Кристина\Desktop\\Kurs\\Kurs1\\lesson6'


path_folders = [('dir_' + str(i + 1)) for i in range(9)]

def creat_folder(paths):
    folder_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(folder_path)
        print(folder_path + ' - Успешно создано')
    except:
        print(folder_path + '- Невозможно создать')    

#for i in path_folders:
#creat_folder(i)

path_folders = [('dir_' + str(i + 1)) for i in range(9)]

def delete_folder(folder):
    folder_path = os.path.join(os.getcwd(), folder)
    try:
        os.rmdir(folder_path)
        print(folder_path + ' - Успешно удалено')
    except:
        print(folder_path + ' - Невозможно удалить')    



#for i in path_folders: 
    #delete_folder(i)    




def list_folder(path1):
    for a in os.listdir(path1):
        print(a)

path1 = os.getcwd()


#list_folder(path1)




def copy_file(first_file,backup_file):
    shutil.copy(first_file,backup_file)
 
first_file = sys.argv[0]
backup_file = first_file + '.backup'
copy_file(first_file,backup_file)


def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - Успешно перешел')
    except:
        print(dir_path + ' - Невозможно перейти')