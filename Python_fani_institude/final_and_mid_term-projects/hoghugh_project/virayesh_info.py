from tkinter import messagebox
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


#function
def zakhireh_virayesh_karmand():
    if messagebox.askyesno(title='ذخیره اطلاعات',message='آیا از صحت اطلاعات مطمئن هستید؟'):
        personel_code = ent_v_personel.get()
        name = ent_v_name.get()
        family_name = ent_v_family.get()
        job = ent_v_job.get()
        meli_id = ent_v_meli.get()
        hoghugh_payeh = ent_v_bsal.get()
        degree = ent_v_degree.get()
        messagebox.showinfo(title='انجام شد',message='اطلاعات با موفقیت ذخیره شد')

def show_personel():
    with open('emp.txt') as f:
        for line in f:
            emp, info = line.split('=')
            emp = emp.strip(' ')
            info = info.strip(' ')
            if emp == ent_v_personel.get():
                ent_v_name.delete(0, END)
                ent_v_name.insert(0, info[0])
                ent_v_family.delete(0, END)
                ent_v_family.insert(0, info[1])
                ent_v_job.delete(0, END)
                ent_v_job.insert(0, info[2])
                ent_v_meli.delete(0, END)
                ent_v_meli.insert(0, info[3])
                ent_v_bsal.delete(0, END)
                ent_v_bsal.insert(0, info[4])
                ent_v_degree.delete(0, END)
                ent_v_degree.insert(0, info[5])
                ent_v_children.delete(0, END)
                ent_v_children.insert(0, info[6])

def close():
    if messagebox.askyesno(title='خروج',message='آیا از خروج مطمئن هستید؟',):
        top_virayesh.destroy()


#panel
top_virayesh = Toplevel()
top_virayesh.geometry('300x1000')
top_virayesh.title('ورود اطلاعات کاربر')
top_virayesh.iconbitmap('salary.ico')
top_virayesh.configure(background='cyan')

top_virayesh.protocol("WM_DELETE_WINDOW", close)


#lables
frm_v = Frame(top_virayesh)
frm_v.grid(row=1, column=1, columnspan=5)
img_v = PhotoImage(file='config.png')
lb_v_img = Label(frm_v,
                 image=img_v,
                 )
# lb1.grid(row=1,column=1)
lb_v_img.pack()

lb_v_titr = Label(frm_v,
                  text='برای ویرایش لطفا کد پرسنل را وارد کنید',
                  font=arial_bold_font,
                  bg='cyan')
# lb2.grid(row=2,column=1)
lb_v_titr.pack(fill=X)

lb_v_personel = Label(top_virayesh,
                      text=': کد پرسنل',
                      font=label_font,
                      relief='raised',
                      bg='grey',
                      )
lb_v_personel.grid(row=2, column=5, pady=30)

ent_v_personel = Entry(top_virayesh,
                       width=5,
                       relief='sunken',
                       bd=4,
                       justify='right',
                       )
ent_v_personel.grid(row=2, column=4, columnspan=2)



lb_v_name = Label(top_virayesh,
                  text=': نام',
                  font=label_font,
                  relief='raised',
                  bg='grey',
                  )
lb_v_name.grid(row=3, column=5)

ent_v_name = Entry(top_virayesh,
                   relief='sunken',
                   bd=4,
                   justify=RIGHT
                   )
ent_v_name.grid(row=3, column=4, pady=5)

lb_v_family = Label(top_virayesh,
                    text=': نام خانوادگی',
                    font=label_font,
                    relief='raised',
                    bg='grey',
                    )
lb_v_family.grid(row=4, column=5)

ent_v_family = Entry(top_virayesh,
                     relief='sunken',
                     bd=4,
                     justify=RIGHT
                     )
ent_v_family.grid(row=4, column=4, pady=5)

lb_v_job = Label(top_virayesh,
                 text=': شغل',
                 font=label_font,
                 relief='raised',
                 bg='grey',
                 padx=10
                 )
lb_v_job.grid(row=5, column=5)

ent_v_job = Entry(top_virayesh,
                  relief='sunken',
                  bd=4,
                  justify='right'
                  )
ent_v_job.grid(row=5, column=4, pady=5)

lb_v_id = Label(top_virayesh,
                text=': کد ملی',
                font=label_font,
                relief='raised',
                bg='grey',
                padx=10
                )
lb_v_id.grid(row=6, column=5)

ent_v_meli = Entry(top_virayesh,
                   relief='sunken',
                   bd=4,
                   justify='right'
                   )
ent_v_meli.grid(row=6, column=4, pady=5)

lb_v_bsal = Label(top_virayesh,
                  text=': حقوق پایه',
                  font=label_font,
                  relief='raised',
                  bg='grey',
                  padx=10
                  )
lb_v_bsal.grid(row=7, column=5)

ent_v_bsal = Entry(top_virayesh,
                   relief='sunken',
                   bd=4,
                   justify='right'
                   )
ent_v_bsal.grid(row=7, column=4, pady=5)


lb_v_degree = Label(top_virayesh,
                    text=': مدرک تحصیلی',
                    font=label_font,
                    relief='raised',
                    bg='grey',
                    padx=10
                    )
lb_v_degree.grid(row=9, column=5)

ent_v_degree = Entry(top_virayesh,
                     relief='sunken',
                     bd=4,
                     justify='right'
                     )
ent_v_degree.grid(row=9, column=4, pady=5)

img_v_ax = PhotoImage(file='lock.png')
lb_im_v = Label(top_virayesh,image=img_v_ax)
lb_im_v.grid(row=12,column=4,columnspan=2)

########buttons
btn_v_search = Button(top_virayesh,
                      text='جست و جو',
                      font=label_font,
                      command=show_personel
                      )
btn_v_search.grid(row=2, column=3, columnspan=2)

btn_v_save = Button(top_virayesh,
                    command=zakhireh_virayesh_karmand,
                    text='ذخیره اطلاعات',
                    font=label_font)
btn_v_save.grid(row=13, column=4, pady=10, columnspan=2)

btn_v_exit = Button(top_virayesh,
                    text='خروج',
                    font=label_font,
                    command=close)
btn_v_exit.grid(row=14, column=3, columnspan=2)


top_virayesh.mainloop()
