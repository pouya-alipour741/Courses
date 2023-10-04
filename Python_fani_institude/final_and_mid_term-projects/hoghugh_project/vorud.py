from tkinter import *
from tkinter import messagebox

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

###font
bold_font = ('tahoma', 12, 'bold')
regular_font = ('tahoma',12)
arial_bold_font = ('arial',12,'bold')
label_font = ('tahoma',11)

#####panel
win = Tk()
win.geometry('520x300+500+200')
win.title('صفحه ورود')
win.resizable(0,0)

####function
def enter_samaneh():
    if ent_user.get() != 'admin':
        messagebox.showerror(title='نام اشتباه',message='نام وارد شده اشتباه هست')
    elif ent_pass.get() != 'admin':
        messagebox.showerror(title='رمز اشتباه', message='رمز وارد شده اشتباه هست')

# def show_pass():
#     if checkbox_status.get() == 1:
#         ent_pass['show'] = ''
#     else:
#         ent_pass['show'] = '*'

def show_pass(event=None):
    if ent_pass['show'] == '*':
        ent_pass['show'] = ''
    else:
        ent_pass['show'] = '*'


#######label
lb_user = Label(win,
                text=': نام کاربر',
                font=label_font,
                relief=SUNKEN,
                bg = co3
                )
lb_user.grid(row=1,column=2,pady=50)

lb_pass = Label(win,
                text=': رمز عبور',
                font=label_font,
                relief=SUNKEN,
                bg = co3,
                )
lb_pass.grid(row=2,column=2,sticky='n')

ent_user = Entry(win,bd=2,width=30)
ent_user.grid(row=1,column=1)

ent_pass = Entry(win,bd=2,width=30,show='*')
ent_pass.grid(row=2,column=1,sticky='n')

img = PhotoImage(file='lock.png')
lb_image = Label(win,
                 image=img)
lb_image.grid(row=1,column=0,rowspan=6)

btn_enter = Button(win,text='ورود',font=label_font,width=10,height=2,command=enter_samaneh)
btn_enter.grid(row=3,column=1)

# checkbox_status = IntVar()
#
# check_pass = Checkbutton(win, text='نشان دادن رمز عبور', font=label_font, variable=checkbox_status)
# check_pass.grid(row=4, column=1)

frm_eye = LabelFrame(win,text='نشان دادن رمز',font=label_font,fg='black')
frm_eye.grid(row=3,column=2,sticky='w')

img_eye = PhotoImage(file='eye.png')
pass_eye = Label(frm_eye,image=img_eye)
pass_eye.pack()

# pass_btn = Button(win,text='نشان/مخفی کردن رمز عبور',font=label_font,command=show_pass)
# pass_btn.grid(row=5,column=1)


#####binds
pass_eye.bind('<Enter>',show_pass)
pass_eye.bind('<Leave>',show_pass)
ent_user.bind('<Return>',lambda event: ent_pass.focus())
ent_pass.bind('<Return>',lambda event:btn_enter.focus())



win.mainloop()