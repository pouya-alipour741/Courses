from tkinter import *

# def func(event= None):
#     if img1['file'] == '1.png':
#         img1['file'] = '2.png'
#     else:
#         img1['file'] = '1.png'
#
#
# win = Tk()
# win.geometry('500x500')
#
# img1 = PhotoImage(file='1.png')
#
# lb1 = Label(win,
#             image=img1,
#             bg= 'red'
#             )
# lb1.grid(row=2,column=3)
#
# win.bind('<Enter>',func)
# win.bind('<Leave>',func)
#
# win.mainloop()


############dars

#############labelframe

win = Tk()
win.geometry('500x300')
frm = LabelFrame(win,
              text='gdfgd',
              font=('arial',13,'italic'),
              # pady=20,
              padx=20,
              bd=4,
              fg='red',
              labelanchor='ne',
              )
frm.place(x=150,y=100)

lb1 = Label(frm,
         text='gjndfjkhgdjfghdj',
         font=('arial',13,'italic'),
         relief='sunken')
lb1.pack()

lb2 = Label(frm,
         text='vjhbut',
         font=('arial',13,'italic'),
         relief='raised')
lb2.pack()

lb3 = Label(frm,
         text='bcvibudifu',
         font=('arial',13,'italic'),
         # relief='groove'
         )
lb3.pack()


win.mainloop()


############frame

# def func():
#     print('hi')
#
# win = Tk()
# win.geometry('500x300')
# frm = Frame(win,
#             pady=20,
#             padx=20,
#             bd=4,
#             )
# frm.place(x=150,y=100)
#
# lb1 = Label(frm,
#             text='gjndfjkhgdjfghdj',
#             font=('arial',13,'italic'),
#             relief='sunken')
# lb1.pack()
#
# lb2 = Label(frm,
#             text='vjhbut',
#             font=('arial',13,'italic'),
#             relief='raised')
# lb2.pack()
#
# lb3 = Label(frm,
#             text='bcvibudifu',
#             font=('arial',13,'italic'),
#             # relief='groove'
#             )
# lb3.pack()

# btn1 = Button(frm,
#               text='press',
#               width=15,
#               height=3,
#               cursor='target',
#               # padx=10,
#               # pady=10,
#               command=func
#               )
# btn1.pack()
# win.mainloop()


#########bind

# def func(event):
#     print('hi')
#
# def func2(event):
#     label_text['font'] = ('arial', 15, 'bold')
#     label_text['text'] = 'right click'
#
# def func3(event):
#     label_text['font'] = ('arial',13,'italic')
#     label_text['text'] = 'left click'


# win = Tk()
# win.geometry('500x300')
#
# frm = Frame(win)
# frm.place(x=150,y=50)
#
# label_text = Label(win,
#                    text='left click',
#                    font=('arial',13,'italic'),
#                    relief='sunken',
#                    padx=20,
#                    pady=20
#                    )
#
# label_text.grid(row=1, column=1)
#
# img = PhotoImage(file='1.png')
# label_image = Label(frm,
#                     image=img,
#                     )
# label_image.grid(row=2, column=1)
#
# label_info = Label(frm,
#                    text='hover mouse over button to print hi',
#                    relief='groove',
#                    bd=4,
#                    font=('arial',13,'italic'),
#                    width=30,
#                    height=2
#                    )
# label_info.grid(row=1, column=1)
#
# label_image.bind('<Enter>', func)
# label_text.bind('<Button-1>', func2)  #left click
# label_text.bind('<Button-3>',func3)  #right click
#
# win.mainloop()



##########bind('<Motion>')

# def func(event=None):
#     print('X = {},Y= {}'.format(event.x,event.y))
#
# def func2(event):
#     print('press')
#
# def func21(event):
#     print('release')
#
# def func3(event):
#     print('double click')
#
# win = Tk()
# win.geometry('300x300')
# lb1 = Label(win,
#             text='salam',
#             width=15,
#             height=2,
#             relief='raised')
# lb1.place(x=118,y=87)
#
# win.bind('<Motion>',func)    #baraye kole kadr
# lb1.bind('<ButtonPress-1>',func2)  #1-left click 2-middle mouse 3-right click
# lb1.bind('<ButtonRelease>',func21)    #har kodam az 3dokme mouse
# lb1.bind('<Double-1>',func3)   #double click
#
#
# win.mainloop()



#########pack()
# win = Tk()
# win.geometry('300x300')
# lb1 = Label(win,
#             text='salam',
#             width=15,
#             height=2,
#             relief='sunken',
#             anchor='nw')   #anchor text north west
# lb1.pack(side=RIGHT,fill=Y,padx=10,pady=10)
#
# win.mainloop()


########pack()
# win = Tk()
# win.geometry('300x300')
# lb1 = Label(win,
#             text='salam',
#             width=15,
#             height=2,
#             relief='sunken')
# lb1.pack(side=RIGHT,fill=BOTH,padx=10,pady=10,expand=1)   #vaghti fill = BOTH bayad >> expand=1
#
# win.mainloop()



###########status bar

##def func(event=None):
## lb1['text'] = 'X= {},Y= {}'.format(event.x,event.y)
##
##
##win = Tk()
##win.geometry('300x300')
##lb1 = Label(win,
##         width=15,
##         height=2,
##         relief='sunken',
##         anchor='nw')   #anchor text north west
##lb1.pack(side=BOTTOM,fill=X,padx=5,pady=5)
##
##win.bind('<Motion>',func)
##win.mainloop()



##########more pack()
# win = Tk()
# win.geometry('300x300')
# lb1 = Label(win,
#             text='gkjhfdskjghdf',
#             width=15,
#             height=2,
#             relief='sunken',
#             anchor='e')
# lb1.pack(side=BOTTOM,padx=5,pady=5)
#
#
# lb2 = Label(win,
#             text='hkjhbvjcvhb',
#             width=15,
#             height=2,
#             relief='sunken',
#             anchor='nw')   #anchor text north west
# lb2.pack(side=BOTTOM,padx=5,pady=5)
#
# win.mainloop()


############Entry and get(),columnspan and rowspan

def func():
    name = ent.get()
    print(name)

win = Tk()
win.geometry('500x300')

lb1 = Label(win,
            text='gkjhfdskjghdf',
            width=15,
            height=2,
            relief='sunken',
            anchor='e')

lb1.grid(row=1,column=1)

ent = Entry(win,
            width=15,
            relief='sunken',
            bd=4
            )

ent.grid(row=1,column=2,padx=5)

btn = Button(win,text='columspan',width=30,relief='raised',command=func)
btn.grid(row=2,column=1,columnspan=2)

lb2 = Label(win,text='rowspan',relief='sunken',bd=2,height=4)
lb2.grid(row=1,column=3,rowspan=2)

win.mainloop()


