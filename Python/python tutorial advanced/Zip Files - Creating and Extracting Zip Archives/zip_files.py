import zipfile
import shutil

# my_zip = zipfile.ZipFile('files.zip','w')

# my_zip.write('test.txt')
# my_zip.write('thumbnail.png')

# my_zip.close()

# with zipfile.ZipFile('files_compressed.zip','w',compression=zipfile.ZIP_DEFLATED) as my_zip:   ###compression arguement to reduce size
#     my_zip.write('test.txt')
#     my_zip.write('thumbnail.png')


# with zipfile.ZipFile('files_compressed.zip','r') as my_zip:   ###compression arguement to reduce size
#     print(my_zip.namelist())
#     # my_zip.extractall('files')        ##into files directory or remain empty to extract to non folder
#     my_zip.extract('test.txt','test_folder')

# shutil.make_archive('another','zip','files')  #zip tar gztar bztar xztar

# shutil.unpack_archive('another.zip','another_folder')