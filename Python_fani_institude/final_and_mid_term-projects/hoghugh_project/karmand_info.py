from tkinter import messagebox
from tkinter import *
from tkinter import filedialog

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

#function
def choose_image():
    global ax_i
    ax_i = filedialog.askopenfilename(initialdir=r'C:\Users\pouya\Desktop\python\class',title='select an image')
    ent_i_ax.delete(0,END)
    ent_i_ax.insert(0,ax_i)


def zakhireh_karmand():
    global personel_code,name,family_name,job,meli_id,hoghugh_payeh,degree
    if messagebox.askyesno(title='ذخیره اطلاعات',message='آیا از صحت اطلاعات مطمئن هستید؟'):
        personel_code = ent_i_personel.get()
        name = ent_i_name.get()
        family_name = ent_i_family.get()
        job = ent_i_job.get()
        meli_id = ent_i_meli.get()
        hoghugh_payeh = ent_i_bsal.get()
        degree = ent_i_degree.get()
        image_link = ent_i_ax.get()
        messagebox.showinfo(title='انجام شد',message='اطلاعات با موفقیت ذخیره شد')


        with open('emp.txt','a') as f:
            f.write(f'{personel_code} = {[name,family_name,job,meli_id,hoghugh_payeh,degree,image_link]}\n')


def close():
    if messagebox.askyesno(title='خروج',message='آیا از خروج مطمئن هستید؟',):
        top_info.destroy()


#panel
top_info = Toplevel()
top_info.geometry('320x650')
top_info.title('ورود اطلاعات کاربر')
top_info.iconbitmap('salary.ico')
top_info.configure(background='cyan')

top_info.protocol("WM_DELETE_WINDOW", close)


#lables
frm = Frame(top_info)
frm.grid(row=1,column=1,columnspan=5)
img = PhotoImage(file='office.png')
lb_i_pic = Label(frm,
                 image=img,
                 )
# lb1.grid(row=1,column=1)
lb_i_pic.pack()

lb_i_titr = Label(frm,
                  text='لطفا اطلاعات لازم را با دقت وارد کنید',
                  font=arial_bold_font,
                  bg='cyan')
# lb2.grid(row=2,column=1)
lb_i_titr.pack(fill=X)

lb_i_personel = Label(top_info,
                      text=': کد پرسنل',
                      font=label_font,
                      relief='raised',
                      bg='grey',
                      )
lb_i_personel.grid(row=2, column=5, pady=30)

ent_i_personel = Entry(top_info,
                       width=10,
                       relief='sunken',
                       bd=4,
                       justify='right'
                       )
ent_i_personel.grid(row=2, column=4)

lb_i_name = Label(top_info,
                  text=': نام',
                  font=label_font,
                  relief='raised',
                  bg='grey',
                  )
lb_i_name.grid(row=3, column=5)

ent_i_name = Entry(top_info,
                   relief='sunken',
                   bd=4,
                   justify=RIGHT
                   )
ent_i_name.grid(row=3, column=4, pady=5)

lb_i_family = Label(top_info,
                    text=': نام خانوادگی',
                    font=label_font,
                    relief='raised',
                    bg='grey',
                    )
lb_i_family.grid(row=4, column=5)

ent_i_family = Entry(top_info,
                     relief='sunken',
                     bd=4,
                     justify=RIGHT
                     )
ent_i_family.grid(row=4, column=4, pady=5)

lb_i_job = Label(top_info,
                 text=': شغل',
                 font=label_font,
                 relief='raised',
                 bg='grey',
                 padx=10
                 )
lb_i_job.grid(row=5, column=5)

ent_i_job = Entry(top_info,
                  relief='sunken',
                  bd=4,
                  justify='right'
                  )
ent_i_job.grid(row=5, column=4, pady=5)

lb_i_meli = Label(top_info,
                  text=': کد ملی',
                  font=label_font,
                  relief='raised',
                  bg='grey',
                  padx=10
                  )
lb_i_meli.grid(row=6, column=5)

ent_i_meli = Entry(top_info,
                   relief='sunken',
                   bd=4,
                   justify='right'
                   )
ent_i_meli.grid(row=6, column=4, pady=5)

lb_i_bsal = Label(top_info,
                  text=': حقوق پایه',
                  font=label_font,
                  relief='raised',
                  bg='grey',
                  padx=10
                  )
lb_i_bsal.grid(row=7, column=5)

ent_i_bsal = Entry(top_info,
                   relief='sunken',
                   bd=4,
                   justify='right'
                   )
ent_i_bsal.grid(row=7, column=4, pady=5)

lb_i_degree = Label(top_info,
                    text=': مدرک تحصیلی',
                    font=label_font,
                    relief='raised',
                    bg='grey',
                    padx=10
                    )
lb_i_degree.grid(row=9, column=5)

ent_i_degree = Entry(top_info,
                     relief='sunken',
                     bd=4,
                     justify='right'
                     )
ent_i_degree.grid(row=9, column=4, pady=5)

lb_i_ax = Label(top_info,
                text=': عکس کارمند',
                font=label_font,
                relief='raised',
                bg='grey',
                padx=10
                )
lb_i_ax.grid(row=10, column=5, pady=10)

ent_i_ax = Entry(top_info,
                 relief='sunken',
                 bd=4,
                 justify='right', )
ent_i_ax.grid(row=10, column=4)


######buttons
btn_i_ax = Button(top_info,
                  text='انتخاب عکس',
                  font=bold_font,
                  height=1,
                  width=10,
                  command=choose_image
                  )
btn_i_ax.grid(row=11, column=4, pady=5)

btn_i_save = Button(top_info,
                    command=zakhireh_karmand,
                    text='ثبت کاربر',
                    font=label_font)
btn_i_save.grid(row=12, column=5)

btn_i_exit = Button(top_info,
                    text='خروج',
                    font=label_font,
                    command=close)
btn_i_exit.grid(row=12, column=4)

top_info.mainloop()
