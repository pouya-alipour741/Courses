from tkinter import *


##def func():
####    lst = [code,name,last]
####    str1 = '{},{},{}\n'.format(ent_name.get(),ent_last.get(),ent_code.get())
##    lst = '{},{},{}\n'.format(ent_name.get(),ent_last.get(),ent_code.get())
##    f= open('01.txt',mode='a')
####    f.write(str1)
##    f.writelines(lst)
##    f.close()
##    
##win = Tk()
##win.geometry('500x500')
##
##frm = LabelFrame(win,bg='orange',text='info',labelanchor='s',padx=100,pady=100)
##frm.place(x=40,y=60)
##
##lb_name = Label(frm,text=':name',padx=20,bg='orange')
##
##lb_name.grid(row=1,column=2)
##ent_name = Entry(frm)
##
##ent_name.grid(row=1,column=1)
##
##lb_last = Label(frm,text=':last name',padx=20,bg='orange')
##lb_last.grid(row=2,column=2)
##ent_last = Entry(frm)
##ent_last.grid(row=2,column=1)
##
##lb_code = Label(frm,text=':code',padx=20,bg='orange')
##lb_code.grid(row=3,column=2)
##ent_code = Entry(frm)
##ent_code.grid(row=3,column=1)
##
##
##btn = Button(frm,text='press',command=func,width=20)
##btn.grid(row=4,column=1,columnspan=2,pady=20)
##
##
##
##
##win.mainloop()



###dars

f = open('emp.txt',mode='r')
lst = f.readlines()  #return a list of strings from lines
f.close()
##print(lst)

temp = []
for item in lst:
    temp.append(item.strip('\n').split(','))

print(temp)
    
