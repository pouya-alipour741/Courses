import csv
from collections import defaultdict,Counter


###1
# with open('data/survey_results_public.csv') as f:
#     csv_reader = csv.DictReader(f)
#
#     yes_count = 0
#     no_count = 0
#     for line in csv_reader:
#         if line["Hobbyist"] == 'Yes':
#             yes_count += 1
#         elif line["Hobbyist"] == 'No':
#             no_count += 1
#
# total = yes_count + no_count
#
# yes_percentage = round((yes_count/total * 100),2)
# no_percentage = round((no_count/total * 100),2)
#
# print(f'yes: {yes_percentage}%')
# print(f'no: {no_percentage}%')

###2
# with open('data/survey_results_public.csv') as f:
#     csv_reader = csv.DictReader(f)
#
#     counts = {
#         'Yes': 0,
#         'No': 0
#     }
#     for line in csv_reader:
#         counts[line["Hobbyist"]] += 1
#
#
# total = counts['Yes'] + counts['No']
#
# yes_percentage = round((counts['Yes']/total * 100),2)
# no_percentage = round((counts['No']/total * 100),2)
#
# print(f'yes: {yes_percentage}%')
# print(f'no: {no_percentage}%')

###3
# with open('data/survey_results_public.csv') as f:
#     csv_reader = csv.DictReader(f)
#
#     counts = Counter()
#
#     for line in csv_reader:
#         counts[line['Hobbyist']] += 1
#
#
# total = counts['Yes'] + counts['No']
#
# yes_percentage = round((counts['Yes']/total * 100),2)
# no_percentage = round((counts['No']/total * 100),2)
#
# print(f'yes: {yes_percentage}%')
# print(f'no: {no_percentage}%')

###4
# with open('data/survey_results_public.csv') as f:
#     csv_reader = csv.DictReader(f)
#
#     counts = defaultdict(int)
#
#     for line in csv_reader:
#         counts[line['Hobbyist']] += 1
#
#
# total = counts['Yes'] + counts['No']
#
# yes_percentage = round((counts['Yes']/total * 100),2)
# no_percentage = round((counts['No']/total * 100),2)
#
# print(f'yes: {yes_percentage}%')
# print(f'no: {no_percentage}%')
