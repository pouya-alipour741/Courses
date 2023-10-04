import tkinter.messagebox
from tkinter import *

#colors

co0 = "#2e2d2b"  #black
co1 = "#feffff"  #white
co2 = "#4fa882"  #green
co3 = "#38576b"  #ash_blue
co4 = "#403d3d"  #ash
co5 = "#e06636"  #orange
co6 = "#038cfc"  #blue
co7 = "#3fbfb9"  #green
co8 = "#263238"  #black
co9 = "#e9edf5"  #white

#fonts
bold_font = ('tahoma', 12, 'bold')
regular_font = ('tahoma',12)
arial_bold_font = ('arial',12,'bold')
label_font = ('tahoma',11)


#panel
win = Tk()
win.geometry('700x600')
win.title('محاسبه حقوق')
win.iconbitmap('salary.ico')
win.configure(background=co9)

#salary functions and variables
hoghugh_payeh = 4179550
hagh_maskan = 650000
bon_kargari = 850000
payeh_sanavat = 210000
hagh_olad = 417975
def hoghugh():
     n = int(input('tedad farzand? '))
     return hoghugh_payeh + hagh_maskan + bon_kargari + (hagh_olad * n)

def ezafe():
    ezafe_kari = int(input('saat ezafe kari: '))
    return (hoghugh()) / 220 * (1.4 * ezafe_kari)

def tatil():
    tatil_kari = int(input('saat tatil kari: '))
    return (hoghugh_payeh) / 220 * (1.4 * tatil_kari)

def shab():
    shab_kari = int(input('saat shab kari: '))
    return hoghugh_payeh / 220 * (1.35 * shab_kari)

def sanavat():
    ruze_karkard = int(input('tedad ruze karkard: '))
    return hoghugh_payeh / 365 * ruze_karkard

def eidi():
    ruze_karkard = int(input('tedad ruze karkard: '))
    return ((hoghugh_payeh + bon_kargari + hagh_maskan) * ruze_karkard * 2) / 365

#labels
img = PhotoImage(file='rent.png')
lb1 = Label(win,
            padx=10,
            pady=10,
            # width=20,
            # height=2,
            text='name',
            font= regular_font,
            fg='red',
            bg= 'black',
            image= img
            )
# lb1.place(x=0,y=0)
lb1.pack(padx=20,pady=20)

textbox = Text(win, font=bold_font,height=1)
textbox.pack(padx=20,pady=10)


btn1 = Button(win,text='click me',font=regular_font)
btn1.pack(pady=10)

myentry = Entry(win)
myentry.pack(padx=60,pady=30)



btnframe = Frame(win)
btnframe.columnconfigure(0,weight=1)
btnframe.columnconfigure(1,weight=1)
btnframe.columnconfigure(2,weight=1)

btn1 = Button(btnframe,text='1',font=regular_font)
btn1.grid(row=0,column=0,sticky='ew')

btn2 = Button(btnframe,text='2',font=regular_font)
btn2.grid(row=0,column=1,sticky=W+E)

btn3 = Button(btnframe,text='3',font=regular_font)
btn3.grid(row=0,column=2,sticky=W+E)

btn4 = Button(btnframe,text='4',font=regular_font)
btn4.grid(row=1,column=0,sticky=W+E)

btn5 = Button(btnframe,text='5',font=regular_font)
btn5.grid(row=1,column=1,sticky=W+E)

btn6 = Button(btnframe,text='6',font=regular_font)
btn6.grid(row=1,column=2,sticky='ew')

btnframe.pack(fill='x')

calc = str()
def hi(symbol):
    global calc
    calc+= symbol
    textbox.delete('1.0',END)
    textbox.insert('1.0',calc)

anotherbtn = Button(win,text='insert hi',command=lambda: hi('hi '))
anotherbtn.place(x=100,y=220,height=20)


check_state = IntVar()
check = Checkbutton(win,text='show message box',font=regular_font,variable=check_state)
check.pack(side=RIGHT,padx=10,pady=10)

check_str = StringVar()
check2 = Checkbutton(win,text='would you like pizza or burger?',font=regular_font,variable=check_str,onvalue='pizza',offvalue='burger')
check2.deselect()
check2.pack(side=LEFT)

def ord_food():
    if check_str.get() == 'pizza':
        print('piz')
    else:
        print('burg')

food_btn = Button(win,text='food',font=regular_font,command=ord_food)
food_btn.pack()

from tkinter import messagebox

def show_message():
    if check_state.get() == 1:
        print(textbox.get('1.0',END))
    else:
        messagebox.showinfo(title='message',message=textbox.get('1.0',END))

msg_button = Button(win,font=regular_font,text='show message',command=show_message)
msg_button.pack(padx=10,pady=10)


def on_close():
    if messagebox.askyesno(title='quit?',message='do you want to quit'):
        win.destroy()

win.protocol("WM_DELETE_WINDOW",on_close)

def clear():
    textbox.delete('1.0',END)

clr_btn = Button(win,text = 'clear',font= regular_font,command=clear)
clr_btn.pack(padx=10,pady=10)



menu_bar = Menu(win)
file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label='close',command=on_close)
file_menu.add_separator()
file_menu.add_command(label='close without question',command=exit)
actionmenu = Menu(menu_bar,tearoff=0)
actionmenu.add_command(label='show message',command=show_message)


menu_bar.add_cascade(menu=file_menu,label='file')
menu_bar.add_cascade(menu=actionmenu,label='Action')


win.config(menu=menu_bar)

# anotherbtn = Button(win,text='hi',width=50,height=50)
# anotherbtn.pack(pady=50)



# print(f'{eidi():,.0f} toman')
#frame
# top_frame = Frame(window, width=1043, height=60, pady=5, bg=co1,  relief="flat",)
# top_frame.grid(row=0, column=0)
#
# bottom_frame = Frame(window,width=1043, height=400,bg=co1, pady=0, relief="flat")
# bottom_frame.grid(row=1, column=0,pady=0, padx=0, sticky=NSEW)

win.mainloop()