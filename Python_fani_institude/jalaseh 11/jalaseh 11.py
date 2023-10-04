# from tkinter import *
#
#
# ###tamrin 1
# def func():
#    name = ent_user.get()
#    passw = ent_pass.get()
#
#    if name == 'admin' and passw == 'admin':
#        print('welcome')
#    else:
#        print('wrong user or pass')
#
#    ent_user.delete(0, END)
#    ent_pass.delete(0, END)
#    ent_user.focus()
#
#
# def func1 (event):
#
#    if ent_pass['show'] == '*':
#        ent_pass['show'] = ''
#    else:
#        ent_pass['show'] = '*'
#
#
#
#
#
#
#
# win=Tk()
# win.geometry('300x200')
#
# d = {'bd':2,'width':20,'font':('tahoma',11)}
#
# ent_user = Entry(win,**d,selectbackground='grey',selectforeground='blue')
# ent_user.grid(row=1,column=2)
# ent_user.focus()
# ent_user.insert(0,'Pouya')
# ent_user.select_range(0,END)
#
#
# btn=Button(win,
#           text='press',
#           width=5,
#           height=2,
#           command=func)
#
# ent_pass = Entry(win,**d, show= '*')
# ent_pass.grid(row=2,column=2)
#
#
# img = PhotoImage(file='eye.png')
# Label_eye = Label(win,image=img)
#
# lbl_user = Label(win,
#                 text='user',
#                 width=10,
#                 height=3,
#                 )
# lbl_pass = Label(win,
#                 text="pass",
#                 width=10,
#                 height=3,
#                 )
#
# Label_eye.grid(row=2,column=3)
# lbl_user.grid(row=1,column=1)
# lbl_pass.grid(row=2,column=1)
#
# Label_eye.bind('<Enter>',func1)
# Label_eye.bind('<Leave>',func1)
# ent_pass.bind('<Return>',lambda event: btn.focus())
# ent_user.bind('<Return>',lambda event: ent_pass.focus())
#
#
# btn.grid(row=3,column=3)
#
#
#
# win.mainloop()



#####tamrin 2
from tkinter import *
from tkinter import filedialog,messagebox
import os

def submit():
 name = ent_name.get()
 last = ent_last.get()
 lb['text'] = {'name':name,'last':last}
 
def open_img():
 res = filedialog.askopenfilename(initialdir=os.getcwd(), title='select a file:',
                              filetypes=(('png files', '*.png'), ('all files', '*.*')))
 ent_ax.delete(0,END)
 ent_ax.insert(0, res)

def save():
 global img
 img = PhotoImage(file=ent_ax.get())
 lb_ax = Label(win, image=img)
 lb_ax.grid(row=7, column=1, columnspan=2)

win = Tk()
win.geometry('300x300')

lb_name = Label(win,text='اسم')
lb_name.grid(row=1,column=2,padx=60,columnspan=2)

lb_last = Label(win,text='فامیل',)
lb_last.grid(row=2,column=2,padx=60,columnspan=2)

ent_name = Entry(win,justify = RIGHT)
ent_name.grid(row=1,column=1,padx=20)

ent_last = Entry(win,justify = RIGHT)
ent_last.grid(row=2,column=1,padx=20)

name = ent_name.get()
last = ent_last.get()
lst = [name,last]

bt = Button(win,text='submit',command=submit)
bt.grid(row=3,column=1,columnspan=3)

lb = Label(win,text='')
lb.grid(row=4,column=1,columnspan=3)

bt_ax = Button(win,text='انتخاب عکس',command=open_img)
bt_ax.grid(row=5,column=2)

bt_ax2 = Button(win,text='save image',command=save)
bt_ax2.grid(row=5,column=3,sticky='w')


ent_ax = Entry(win)
ent_ax.grid(row=5, column=1)


win.mainloop()



#dars##

#########1

# from tkinter import *
# from tkinter import messagebox,filedialog
#
# def func():
#     if win.state() == 'zoomed':
#         win.state('normal')
#     else:
#         win.state('withdrawn')
#
# def func2():
#     print(win.state())
#
# def func3():
#     if win.state() == 'withdrawn':
#         win.state('normal')
#     else:
#         win.state('withdrawn')
#
# win = Tk()
# win.title('main')
# win2 = Toplevel()
# win2.title('slave')
# win2.geometry('300x300+500+200')
# win.state('zoomed')
#
# win2.lift(win)
#
# btn1 = Button(win2,command=func,text='change main window aspect')
# btn1.pack(side=TOP)
#
# btn2 = Button(win2,command=func2,text='main window state')
# btn2.pack(side=TOP)
#
# btn3 = Button(win2,command=func3,text='minimize on off')
# btn3.pack(side=TOP)
#
# btn4 = Button(win2,command=func3,text='minimize on off')
# btn4.pack(side=TOP)
#
# btn4.pack_forget()  #delete button 4
#
#
# win.mainloop()




########2
# from tkinter import *
# from tkinter import messagebox,filedialog
#
# def func():
#     win2.state('normal')
#     if win.state() == 'withdrawn':
#         win.state('normal')
#     else:
#         win.state('withdrawn')
#
# def func2():
#     win2.state('normal')
#     win2.lift(win)
#
# def func3():
#     win2.state('withdrawn')
#     print(win2.state())
#
# def func4():
#     win2.state('normal')
#
#
# win = Tk()
# win.geometry('300x300')
# win.title('main')
# win2 = Toplevel()
# win2.title('slave')
# win2.geometry('300x300+500+200')
# win.state('zoomed')
# win2.protocol('WM_DELETE_WINDOW',func3)
#
# win2.lift(win)
#
# btn1 = Button(win2,command=func,text='change main window aspect')
# btn1.pack(side=TOP)
#
# btn2 = Button(win2,command=func2,text='lift main win')
# btn2.pack(side=TOP)
#
# btn3 = Button(win,command=func4,text='bring slave back')
# btn3.pack(side=TOP)
#
# btn4 = Button(win2,command=func3,text='minimize on off')
# btn4.pack(side=TOP)
#
# btn4.pack_forget()  #delete button 4
#
#
# win.mainloop()



#########extra
# import tkinter as tk #import Tkinter as tk #change to commented for python2
#
# root = tk.Tk()
#
# for i in range(4):
#     #make a window with a label
#     window = tk.Toplevel(root)
#     label = tk.Label(window,text="window {}".format(i))
#     label.pack()
#     #add a button to root to lift that window
#     button = tk.Button(root, text = "lift window {}".format(i), command=window.lift)
#     button.grid(row=i)
#
# root.mainloop()



#########
# from tkinter import *
#
# def func():
#     print(txt.get(0.0,END))
# win = Tk()
# win.geometry('300x300')
#
# txt = Text(win,relief='sunken',width=20,height=3)
# txt.pack(side=TOP,fill=X)
#
# btn = Button(win,relief='sunken',text='press',command=func)
# btn.pack(side=TOP)
#
# txt.focus()
# txt.insert('end','salam')
# txt.insert(0.0,'bye')
#
#
# win.mainloop()



####
# #Import tkinter library
# from tkinter import *
# #Create an instance of tkinter frame
# win = Tk()
# #Set the geometry
# win.geometry("750x400")
# def select_text():
#    text.tag_add("start", "1.0","end")
#    text.tag_configure("start",background="black", foreground= "white")
# #Create a Text Widget
# text= Text(win)
# text.insert(INSERT, """Python is an interpreted, high-level and generalpurpose
# programming language. Python's design philosophy emphasizes
# code readability with its notable use of significant indentation""")
# text.pack()
# #Create a button to select all the text in the text widget
# button= Button(win, text= "Select", background= "gray71", command=select_text)
# button.pack(side= TOP)
# win.mainloop()



########## be 2 ax roju shavad
# from tkinter import *
# from tkinter import filedialog,messagebox
# win = Tk()
# win.geometry('300x300')
#
# # res = messagebox.showinfo('test','salam')
# res = filedialog.asksaveasfilename(parent=win,initialdir='/',title='select a file')
# print(res)
#
# win.mainloop()



# from tkinter import *
# from tkinter import colorchooser
# win = Tk()
#
# rgb,web = colorchooser.askcolor(parent=win,initialcolor=(255,0,0))
# print(rgb,web)
#
# win.mainloop()
