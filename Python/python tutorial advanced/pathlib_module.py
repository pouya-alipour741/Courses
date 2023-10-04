from pathlib import Path
import os

###1
# print(Path().resolve())   ###gives cwd
# Path().absolute()     ###gives cwd

####2
# filename = "draft.py"
#
# path1 = Path(filename).resolve()
# print(type(path1))
# print(path1.exists())
# print(path1.is_file())
# print(path1.is_dir())

####3
# filename = 'multipool_executor.py'
# f = Path() / 'Threading_Multiprocessing_modules' / 'Multiprocessing' / filename  ##similar to os.path.join()
# print(f.resolve())
# print(f.exists())
#
# print(Path(filename).suffix)       ###getting extension with pathlib
# print(f.stem)
# print(f.parent)
# print(f.parent.stem)   ##print parent folder of the filename
# print(Path(filename).name)       ###getting file name with pathlib
# print(Path(filename).resolve())
#
# print(os.path.splitext(filename)[-1])   ###getting extension with os


####4
# path = Path(r'C:\Users\pouya\Desktop\python')
# # print(path.exists())
# for file in path.glob("*.xlsx"):
#     print(file)
#     print(file.name)
#     print(file.suffix)
#     print()
#
# for file in path.glob("*.pdf"):
#     print(file)

###5
# for file in Path('logging_tutorial').glob("*.py"):
# # print(file.suffix)
#     print(file.name)
#     # print(file)
#     print()


###6
# print(os.listdir('Zip Files - Creating and Extracting Zip Archives'))
# for file in Path('Zip Files - Creating and Extracting Zip Archives').glob("*/*"):  ##all .py files in first subfolder
#     # print(file.suffix)
#     print(file.name)
#     # print(file)
#     print()
#

##7
# file_list = [file.name for file in Path('Zip Files - Creating and Extracting Zip Archives').glob("*/*")]
# print(file_list)

##8
# file_list = list(Path('Zip Files - Creating and Extracting Zip Archives').glob("*/*"))
# print(file_list)

###
# print(Path(__file__))   ##get the address of current file