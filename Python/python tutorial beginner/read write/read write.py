# f = open('test.txt','r')
# print(f.name)
# f_content = f.read()
# print(f_content)
# f.close()

# better way
# with open('test.txt','r') as f:
#     f_content = f.read()
#     print(f_content,end='')


# better for reading larger files so we don't run out of memory
# with open('test.txt','r') as f:
#     for line in f:
#         print(line,end='')# end='' to remove space between lines

#more option
# with open('test.txt','r') as f:
#     f_content = f.read(3)
#     while len(f_content) > 0:
#         print(f_content, end='')
#         f_content = f.read(3)
#
#     print('\n',f.tell())

# with open('test.txt','r') as f:
#     f_content = f.read(9)
#     print(f_content,end='')
#     f.seek(15) #it start next part from index 15
#     f_content = f.read(9)
#     print(f_content, end='')

# write
# with open('test3.txt','w') as f: #use 'a' instead to appened to current file
#     f.write(' hello world')
#     # f.seek(1)
#     f.write(' hello world')

#read then write
# with open('test.txt','r') as rf:
#     with open('test_copy.txt','w') as wf:
#         for line in rf:
#             wf.write(line)

#copy picture
# with open('657567.PNG','rb') as shit:
#     with open('657567_copy.PNG','wb') as shit_copy:
#         for line in shit:
#             shit_copy.write(line)

# with open('657567.PNG', 'rb') as shit:
#     with open('657567_copy2.PNG', 'wb') as shit_copy:
#         good_shit = shit.read(4096)
#         while len(good_shit) > 0:
#             shit_copy.write(good_shit)
#             good_shit = shit.read(4096)

# with open("text2.txt", "r") as f:
#     f_content = f.readlines()
#     # print(f_content)
#     with open("writelines_learn.txt", "w") as f:
#         f.writelines(f_content)

# f_cont = ["1st line\t","2nd line"]
# with open("writelines_learn2.txt", "w") as f:
#     f.writelines(f_cont)


# with open("writelines_learn.txt", "r") as f:
#     f_cont = f.read(10)
#     while len(f_cont) > 0:
#         print(f_cont,end="")
#         f_cont = f.read(1)










