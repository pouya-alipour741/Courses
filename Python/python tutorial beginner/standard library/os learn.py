import os
# print(os.getcwd())
# os.chdir(r'C:\Users\pouya\desktop')
# print(os.getcwd())
# print(dir(os))
# print(os.__file__)

# print(os.listdir())
# print(list(os.scandir()))
# print([entry.name for entry in list(os.scandir())])   ##same as os.listdir


# os.mkdir('module 3\sub module2')
# os.makedirs('module 3\sub module2')  #make all folders even if they don't exist
# os.rmdir('module 3\sub module2')
# os.removedirs('module 2')
# print(os.rename('draft_calc.py','webbrowser lib.py'))


# os.chdir('C:/Users/pouya/Desktop/python')
# print(os.stat('search.jpg'))
#
# mod_size = os.stat('search.jpg').st_size        ###shows size in bytes
# print(mod_size)
#
# mod_time = os.stat('search.jpg').st_mtime
# print(mod_time)
#
# import datetime
# print(datetime.datetime.fromtimestamp(mod_time))


# for x,y,z in os.walk(r'C:\Users\pouya\PycharmProjects\tutorial\Zip Files - Creating and Extracting Zip Archives'):
#     print(f"there are {len(y)} directories and {len(z)} files in {z}")
#     # print('current path:',x)
#     # print('directories:',y)
#     # print('files:',z)

# print(os.environ.get('ProgramData'))
# new_path = os.environ.get('ProgramData')
# new_path_combined = os.path.join(new_path,'folder1','one more folder','text.txt')  ###can concatanate as many argumnets as we want
# print(new_path_combined)
# print(os.path.exists(new_path_combined))        ###check if path exist

# print(os.environ)

# print(os.path.basename(r'C:\Users\pouya\Desktop\python\csv\ds_salaries.csv'))
# print(os.path.dirname(r'C:\Users\pouya\Desktop\python\csv\ds_salaries.csv'))
# print(os.path.splitext(r'C:\Users\pouya\Desktop\python\csv\ds_salaries.csv'))
# print(os.path.isdir(r'C:\Users\pouya\Desktop\python\csv\ds_salaries.csv'))
# print(os.path.isfile(r'C:\Users\pouya\Desktop\python\csv\ds_salaries.csv'))
# print(os.path.split(r'C:\Users\pouya\Desktop\python\csv\ds_salaries.csv'))

print(os.cpu_count())
