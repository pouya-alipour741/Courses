from contextlib import contextmanager
import os

#how to simulate with open with class
# class open_file():
#     def __init__(self,file_name,mode):
#         self.file_name = file_name
#         self.mode = mode
#     def __enter__(self):
#         self.file = open(self.file_name,self.mode)
#         return self.file
#     def __exit__(self,exe_type,exc_eval,traceback):
#         self.file = self.file.close()
#
#
# with open_file('test_sample.txt','a') as f:
#     f.write('hi this is a test st\n')
#
# print(f.closed)


#using generators
# @contextmanager
# def open_file(file,mode):
#     try:
#         f = open(file,mode)
#         yield f                    ####everything before yield is equivalent to enter statement ins class
#     finally:
#         f.close()                     everything after yield is equivalent to exit statement in class
#
# with open_file('tst.txt','w') as f:
#     f.write('hiiii')
# print(f.closed)


#changing directories function
@contextmanager
def change_dir(directory):
    try:
        cwd = os.getcwd()
        os.chdir(directory)
        yield
    finally:
        os.chdir(cwd)

# with change_dir(r'C:\Users\pouya\Desktop\music\serhat durmus'):
#     a = os.listdir()
#     print(a)
#     with open('show all.txt', 'w') as f:
#         for file in a:
#             if file != '1.txt':
#                 f.write(f'{file}\n')
#
# with change_dir(r'C:\Users\pouya\Desktop\music\town - day'):
#     b = os.listdir()
#     with open('show all.txt', 'w') as f:
#         for file in b:
#             if file != '2.txt':
#               f.write(f'{file}\n')


#only showing a certain format in directory
# @contextmanager
# def change_dir(directory):
#     try:
#         cwd = os.getcwd()
#         os.chdir(directory)
#         yield
#     finally:
#         os.chdir(cwd)

# with change_dir(r'C:\Users\pouya\Desktop\music\serhat durmus'):
#     with open('show mp3 only.txt', 'w') as f:
#         for i in os.listdir():
#             name,ext = os.path.splitext(i)
#             # print(ext)
#             if ext == '.mp3':
#                 f.write(f'{name}\n')
#                 print(name,ext,sep='')

