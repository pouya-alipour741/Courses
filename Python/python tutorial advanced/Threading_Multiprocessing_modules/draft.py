from PIL import Image,ImageFilter
import concurrent.futures
import time
from contextlib import contextmanager
import os

# @contextmanager
# def change_dir(cur):
#     try:
#         cur = os.getcwd()
#         os.chdir(r'E:\Pictures\Sport')
#         yield
#     finally:
#         os.chdir(cur)
#
img_names = []
path = 'E:\Pictures\Sport'
for f in os.listdir(path):
    if f.endswith('jpg'):
        img_names.append(f)
print(img_names)

# img_names = ['1.jpg','2.jpg','3.jpg','4.jpg']
# t1 = time.perf_counter()

# @change_dir
# def edit_pictures(img_name):
#     img = Image.open(img_name)
#     img = img.filter(ImageFilter.GaussianBlur(13))
#     img.thumbnail(size)
#     img.save(f'processed/{img_name}')
#     print(f'{img_name} was processed...')
#     print(os.getcwd())

size = (1200,1200)
os.chdir(r'E:\Pictures\Sport')
for img_name in img_names:
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(13))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')
    print(os.getcwd())

# if __name__ == "__main__":
#
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         executor.map(edit_pictures,img_names)
#
#
#     t2 = time.perf_counter()
#     print(f'finished in {t2-t1} seconds')
