import shutil
import os
os.chdir(r'C:\Users\pouya\Desktop\python\music test')
# print(os.getcwd())
# print(os.listdir())
for file in os.listdir():
    shutil.copy(file, r'C:\Users\pouya\Desktop\python\move here')
os.chdir(r'C:\Users\pouya\Desktop\python\move here')
for f in os.listdir():
    f_name,f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
    new_f = f'{f_num}-{f_title}-{f_course}{f_ext}'
    os.rename(f, new_f)


