import matplotlib.pyplot as plt
import requests
from pathlib import Path
import os
from contextlib import contextmanager

@contextmanager
def change_WDirectory(path):
    try:
        cur_wdirectory = Path.cwd()  ##same as os.getcwd()
        os.chdir(path)
        yield
    finally:
        os.chdir(cur_wdirectory)


github_link = input("enter github link: ")
wdirectory = input("enter working directory adress: ")
path = Path(input("enter course title: "))
path_name = f"{input('enter file name: ')}"
path_loc = path / path_name


def corey_github_downloader(path,path_name,github_link,WDirectory='C:/Users/pouya/vsCodeProjects/matplotlib-course'):
    with change_WDirectory(WDirectory):
        path.mkdir(parents=True, exist_ok=True)

        Matplotlib_01 = github_link
        response = requests.get(Matplotlib_01)

        with open(path_loc,'wb') as f:
            f.write(response.content)
    

course = corey_github_downloader(path,path_name,github_link)
course




