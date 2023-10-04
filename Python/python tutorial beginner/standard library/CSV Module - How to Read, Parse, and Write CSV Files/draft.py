import csv

lst = [chr(i) for i in range(82,87)]
print(lst)
str1 = ''.join(lst)
print(str1)

field_names = ['first','second','third','fourth','fifth']
str2 = {key:value for key,value in zip(field_names,str1)}
print(str2)

# my_dict = {}
# for key, value in zip(field_names,str1):
#     my_dict[key] = value
# print(my_dict)


with open("sample1.csv",mode='w') as csv_file:
    csv_writer = csv.DictWriter(csv_file,fieldnames=field_names)

    csv_writer.writeheader()
    csv_writer.writerow(str2)



# with open(r"C:\Users\pouya\Desktop\python\csv\vgsales.csv",mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     lst_csv = list(csv_reader)[:5]
#     for item in lst_csv:
#         print(item)
#     with open(r"vgsales_copy.csv", mode='w') as csv_copy:
#         field_names = ['Platform','Year']
#         csv_writer = csv.DictWriter(csv_copy,fieldnames=field_names,delimiter='\t')
#
#         csv_writer.writeheader()
#         for line in csv_reader:
#             line = {
#                 'Platform': line['Platform'],
#                 'Year': line['Year'],
#             }
#             csv_writer.writerow(line)