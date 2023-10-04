#ta vaghti adad begire tekrar,gheyr az addad gereft error va exit
##while True:
##    try:
##        g = int(input('addad aval: '))
##        b = int(input('addad dovom: '))
##        print('natijeh = {}'.format(g*b))
##    except:     
##        print('type only numbers')
##        break


##ta vaghti gheyr az adad gerefte tekrar,2ta addad gereft exit
##while True:
##    try:
##        g = int(input('addad aval: '))
##        b = int(input('addad dovom: '))
##        c = g * b
##        print('natijeh = {}'.format(c))
##        break
##    except:
##        pass


##ravesh behtar tamrin ghabl
##while True:
##    try:
##        g = int(input('addad aval: '))
##        break
##    except:
##        pass
##    
##while True:
##    try:
##        b = int(input('addad dovom: '))
##        print('natijeh = {}'.format(g*b))
##        break
##    except:
##        pass
   

#4ta morabae kenar ham

##from tkinter import *
##
##
##win = Tk()
##win .geometry('500x500')
##win.title('hi')

##lb1 = Label(win,
##            bg = 'lightblue',
####            relief = 'raised', 
##            width = 50,
##            height = 50,
##            )
##
##lb1.place(x = 0, y = 0)

##lb2 = Label(win,
##            bg = 'red',
####            relief = 'raised',
##            width = 50,
##            height = 50
##            )
##
##lb2.place(x = 250, y = 0)
##
##lb3 = Label(win,
##            bg = 'green',
####            relief = 'raised',
##            width = 50,
##            height = 50
##            )
##
##lb3.place(x = 0, y = 250)
##
##lb4 = Label(win,
##            bg = 'purple',
####            relief = 'raised',
##            width = 50,
##            height = 50
##            )
##
##lb4.place(x = 250, y = 250)
##
##
##win.mainloop()


#dars

##label

##from tkinter import *
##win = Tk()
##win.geometry('500x500+150+150')
##win.title('hello world')
##win.iconbitmap('coffee.ico')
##win.configure(bg='darkred')
##win.attributes('-alpha',.9) #transparent
##win.state('normal') #zoomed,iconic,normal,withdrawn,normal
##
##lb1 = Label(win,
##            text= 'click me !',
##            font= ('tahoma',12,'bold'),
####            width= 25,
####            height=4,
##            bg= 'green', #background 
##            fg= 'blue',  #font
##            relief= 'ridge', #flat,raised,sunken,groove,ridge
####            bd= 10,  
##            cursor= 'target',
##            underline= 0,  #index underline
##            padx= 25,
##            pady = 25,
##            )
##lb1.place(x=180,y=200)
##win.mainloop()




#ax

##from tkinter import *
##
##
##win = Tk()
##win.geometry('500x500')
##
##im = PhotoImage(file='work.png')
##
##lb1 = Label(win,
##            relief = 'sunken',
##            image = im,
##            )
##lb1.place(x=20,y=20)
##
##im2 = PhotoImage(file= 'plan.png')
##
##lb2 = Label(win,
##            image = im2,
##            relief= 'sunken',
##            )
##lb2.place(x=200,y=20)
##
##win.mainloop()
             




#frame

##from tkinter import *
##
##win = Tk()
##
##frm = LabelFrame(win,padx= 20,pady=20)
##frm.pack(padx=10,pady=10)
##
##
##im = PhotoImage(file='work.png')
##
##lb1 = Label(frm,
####            relief = 'sunken',
##            image = im,
##            )
##lb1.pack()
##
##im2 = PhotoImage(file= 'plan.png')
##
##lb2 = Label(frm,
##            image = im2,
####            relief= 'sunken',
##            )
##lb2.pack()
##
##im3 = PhotoImage(file='rent.png')
##
##lb3 = Label(frm,
##            image = im3,
##            )
##lb3.pack()
##
##im4 = PhotoImage(file='up.png')
##
##lb4 = Label(frm,
##            image = im4,
##            )
##            
##lb4.pack()
##
##win.mainloop()


             




