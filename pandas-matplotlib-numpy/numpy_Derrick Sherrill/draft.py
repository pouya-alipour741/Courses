import csv
import os
import pandas as pd

os.chdir(r'C:\Users\pouya\Desktop\python\csv')
html_output = ''
names = []
with open(r'unpopular_songs.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        # if line['track_name'] == 'Fangs': # won't read data past 3rd line
        #     break
        names.append(f"{line['track_name']} {line['track_artist']}")

data = pd.read_csv(r'unpopular_songs.csv')
print(data['danceability'])


# html_output += f'<p> there are currently {len(names)} public contributer.Thank you !<p>'
# html_output += '\n<ul>'
# for name in names:
#     html_output += f'\n\t<li>{name}<li>'
# html_output += '\n<ul>'
# print(html_output)
# with open(r'unpopular_songs_new.csv','w') as f:
#     for line in html_output:
#         f.write(line)

    # can use f.write(html_output) # but we might run out of memory with this method



#method2
# os.chdir(r'C:\Users\pouya\Desktop\python\csv')
# html_output = ''
# names = []
#
# with open('vgsales.csv','r') as csv_f:
#     csv_reader = csv.reader(csv_f)
#
#     for line in csv_reader:
#         if line[0] == '4':
#             break
#         names.append(f'{line[0]} {line[1]} {line[-1]}')
# for name in names:
#     print(name)


#method3
# os.chdir(r'C:\Users\pouya\Desktop\python\csv')
# html_output = ''
# names = []
#
# with open('vgsales.csv','r') as csv_f:
#     csv_reader = csv.DictReader(csv_f)
#
#     next(csv_reader)
#
#     for line in csv_reader:
#         if line['Rank'] == '4':
#             break
#         names.append(f"{line['Rank']} {line['Platform']} {line['Genre']}")
# for name in names:
#     print(name)

