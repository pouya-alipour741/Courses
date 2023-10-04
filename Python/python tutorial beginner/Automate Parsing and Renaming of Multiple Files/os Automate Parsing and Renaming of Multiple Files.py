import os
os.chdir(r'C:\Users\pouya\Desktop\python\music test')
# print(os.listdir())

for f in os.listdir():
    f_name,f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
    new_f = f'{f_num}-{f_title}-{f_course}{f_ext}'
    os.rename(f,new_f)

    # os.rename(f,os.path.join(r'C:\Users\pouya\Desktop\python\move here',new_f))
    # print(new_f)

