from PIL import Image ,ImageFilter
import os

###open and show image
# img1 = Image.open('image/4.jpg')
# img1.show()
# img1.save('image/4.png')


###save image
# for f in os.listdir('.'):
#
#     if f.endswith('.jpg'):
#         # print(f)
#     #
#         name,ext = os.path.splitext(f)
#         # print(name,ext)
#         img = Image.open(f)
#         img.save(f'png/{name}.png')


####resize
# for f in os.listdir('.'):
#     size_300 = (300,300)
#     size_700 = (700,700)
#
#     if f.endswith('.jpg'):
#         name,ext = os.path.splitext(f)
#         img = Image.open(f)
#
#         img.thumbnail(size_700)           ##higher resolution should run first
#         img.save(f'700/{name}_700{ext}')
#
#         img.thumbnail(size_300)
#         img.save(f'300/{name}_300{ext}')


##modding
# for f in os.listdir('.'):
#
#     if f.endswith('.jpg'):
#         name,ext = os.path.splitext(f)
#         img = Image.open(f)
#
#         img.rotate(270).save(f'mod/{name}_270{ext}')
#         img.convert(mode='L').save(f'mod/{name}_grey{ext}')
#         img.filter(ImageFilter.GaussianBlur(15)).save(f'mod/{name}_blur{ext}')



