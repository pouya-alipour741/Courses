import os

path = r'E:\Downloads\movie\shameless\11'
mkv_lst = []
srt_lst = []
for file in os.listdir(path):
    if file.endswith('mkv'):
        name,ext = os.path.splitext(file)
        mkv_lst.append(name)
    if file.endswith('srt'):
        srt_lst.append(file)

            # os.rename(os.path.join(path,file),os.path.join(path,''.join([str(index), '.jpg'])))
print(mkv_lst[0])
print(srt_lst[0])

os.chdir(path)
for i in range(len(mkv_lst)):
    os.rename(srt_lst[i],f'{mkv_lst[i]}.srt')


