from pathlib import Path
import automate_module
import shutil

path = Path(r'C:\Users\pouya\Desktop\python\move here')
path_2 = Path(r'C:\Users\pouya\Desktop\python')

for file in path_2.glob('*.xlsx'):
    shutil.copy(file,r'C:\Users\pouya\Desktop\python\move here')
for file in path.glob('*.xlsx'):
    automate_module.process_workbook(file)
