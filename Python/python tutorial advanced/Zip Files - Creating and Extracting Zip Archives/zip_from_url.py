import requests
import shutil
import zipfile
from pathlib import Path

if Path("data.zip").is_file():
    print("file exist,extracting...")
    with zipfile.ZipFile('data.zip', 'r') as f_zip:
        print(f_zip.namelist())
        f_zip.extractall('csv_folder')
        # f_zip.extract("README_2022.txt",'csv_folder')
else:
    print("file does not exist,downloading and extracting...")
    r = requests.get(
        'https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2022.zip')

    with open('data.zip', 'wb') as f:
        f.write(r.content)
    with zipfile.ZipFile('data.zip','r') as f_zip:
        print(f_zip.namelist())
        f_zip.extractall('csv_folder')
        # f_zip.extract("README_2022.txt",'csv_folder')

# shutil.unpack_archive('data.zip','csv_folder')


