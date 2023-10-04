from tkinter import *
from tkinter import messagebox,filedialog,colorchooser
import datetime as dt

#colors

# rgb,web = colorchooser.askcolor((255,0,0))
# print(rgb,web)
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
co10 = "#82ffff" #light blue

#fonts
bold_font = ('tahoma', 12, 'bold')
regular_font = ('tahoma',12)
arial_bold_font = ('arial',12,'bold')
label_font = ('tahoma',11)

#salary functions and variables
hagh_maskan = 650000
bon_kargari = 850000
payeh_sanavat = 210000
hagh_olad = 417975


# def hoghugh():
#      hoghugh_payeh = mozd_saati * ent_f_workday.get()
#      return hoghugh_payeh + hagh_maskan + bon_kargari + (hagh_olad * n)
#
# def ezafe():
#     ezafe_kari = int(input('saat ezafe kari: '))
#     return (hoghugh()) / 220 * (1.4 * ezafe_kari)
#
# def tatil():
#     tatil_kari = int(input('saat tatil kari: '))
#     return (hoghugh_payeh) / 220 * (1.4 * tatil_kari)
#
# def shab():
#     shab_kari = int(input('saat shab kari: '))
#     return hoghugh_payeh / 220 * (1.35 * shab_kari)
#
# def sanavat():
#     ruze_karkard = int(input('tedad ruze karkard: '))
#     return hoghugh_payeh / 365 * ruze_karkard
#
# def eidi():
#     ruze_karkard = int(input('tedad ruze karkard: '))
#     return ((hoghugh_payeh + bon_kargari + hagh_maskan) * ruze_karkard * 2) / 365


########open samaneh hoghugh
def enter_samaneh():
    ent_user.focus()
    if ent_user.get() != 'admin':
        messagebox.showerror(title='نام اشتباه',message='نام وارد شده اشتباه هست')
    elif ent_pass.get() != 'admin':
        messagebox.showerror(title='رمز اشتباه', message='رمز وارد شده اشتباه هست')
    else:
        win.state('withdrawn')
        ent_user.delete(0,END)
        ent_pass.delete(0,END)

        def back():
            win.state('normal')
            top_samaneh.state('withdrawn')

        #### panel
        top_samaneh = Toplevel()
        top_samaneh.resizable(0, 0)
        top_samaneh.geometry('700x460')
        top_samaneh.title('سامانه صدور فیش حقوقی')
        top_samaneh.iconbitmap('salary.ico')
        # top_samaneh.configure(background='orange')

        ########labels
        date = dt.datetime.now()
        welcome_time = date.strftime('%A %B,%Y زمان ورود ساعت  %H:%M   در تاریخ')


        lb_welcome = Label(top_samaneh,text=welcome_time,font=bold_font)
        lb_welcome.place(x=10,y=10)

        frm_bg = Frame(top_samaneh, padx=45)
        # frm_bg.place(x=40)
        frm_bg.grid(row=1, column=1, sticky='news')


        global img_ax_bg
        img_ax_bg = PhotoImage(file='bg.png')
        lb_ax = Label(top_samaneh, image=img_ax_bg)
        lb_ax.place(x=0,y=50)

        ##########buttons
        btn_back = Button(top_samaneh,
                               text='بازگشت به صفحه ورود',
                               font=('tahoma',10,'italic'),
                               relief='groove',
                               # width=20,
                               height=1,
                               bd=4,
                               bg=co4,
                                fg=co1,
                               command=back)
        btn_back.place(x=20,y=60)

        btn_sabt_user = Button(top_samaneh,
                               text='ثبت اطلاعات کاربر',
                               font=bold_font,
                               relief='groove',
                               width=20,
                               height=3,
                               bd=4,
                               bg=co3,
                               command=user_reg
                               )

        btn_sabt_user.place(x=450, y=280)

        btn_virayesh = Button(top_samaneh,
                              text='ویرایش اطلاعات کاربر',
                              font=bold_font,
                              relief='groove',
                              width=20,
                              height=3,
                              bd=4,
                              bg=co3,
                              command=edit,
                              )

        btn_virayesh.place(x=50, y=280)

        btn_sabt_fish = Button(top_samaneh,
                               text='محاسبه فیش حقوقی',
                               font=bold_font,
                               relief='groove',
                               width=20,
                               height=3,
                               bd=4,
                               bg=co3,
                               command=fish_hoghugh_calc,
                               )

        btn_sabt_fish.place(x=250, y=380)



#########open sabt user
def user_reg():
    # function
    def choose_image():
        global ax_i
        ax_i = filedialog.askopenfilename(initialdir=r'C:\Users\pouya\Desktop\python\class', title='select an image')
        ent_i_ax.delete(0, END)
        ent_i_ax.insert(0, ax_i)

    def zakhireh_karmand():
        # if messagebox.askyesno(title='ذخیره اطلاعات', message='آیا از صحت اطلاعات مطمئن هستید؟'):
            personel_code = ent_i_personel.get()
            name = ent_i_name.get()
            family_name = ent_i_family.get()
            job = ent_i_job.get()
            meli_id = ent_i_meli.get()
            hoghugh_payeh = ent_i_bsal.get()
            degree = ent_i_degree.get()
            children = ent_i_children.get()
            image_link = ent_i_ax.get()

            if not hoghugh_payeh.isdigit():
                messagebox.showwarning('خطا','حقوق باید عدد باشد')

            if name == '':
                messagebox.showwarning('خطا','لطفا یک اسم انتخاب کنید ')

            elif family_name == '':
                messagebox.showwarning('خطا','لطفا یک نام خانوادگی انتخاب کنید ')

            elif job == '':
                messagebox.showwarning('خطا','لطفا شغل را وارد نمایید ')

            elif meli_id == '':
                messagebox.showwarning('خطا','لطفا  کد ملی را وارد نمایید ')

            elif hoghugh_payeh == '':
                messagebox.showwarning('خطا','لطفا دستمزد ساعتی را وارد کنید ')

            elif degree == '':
                messagebox.showwarning('خطا','لطفا مدرک تحصیلی را وارد نمایید ')

            elif children == '':
                messagebox.showwarning('خطا','لطفا تعداد فرزند وارد شود ')

            elif image_link == '':
                messagebox.showwarning('خطا','لطفا یک عکس بارگذاری کنید ')

            else:
                lst = [f'{personel_code},{name},{family_name},{job},{meli_id},{hoghugh_payeh},{degree},{children},{image_link}\n']
                f = open('emp.txt','a')
                f.writelines(lst)
                f.close()

                # with open('emp.txt', 'a') as fa:
                #     fa.write(f'{personel_code},{name}, {family_name}, {job}, {meli_id}, {hoghugh_payeh}, {degree}, {children}, {image_link}\n')
                #     messagebox.showinfo('عملیات موفق','مشخصات پرسنل با موفقیت ثبت شد')


    def close():
        if messagebox.askyesno(title='خروج', message='آیا از خروج مطمئن هستید؟', ):
            top_info.destroy()


    # panel
    global top_info
    top_info = Toplevel()
    top_info.geometry('320x650+1000+100')
    top_info.title('ورود اطلاعات کاربر')
    top_info.iconbitmap('salary.ico')
    top_info.configure(background='cyan')



    # top_info.protocol("WM_DELETE_WINDOW", close)

    # lables
    frm = Frame(top_info)
    frm.grid(row=1, column=1, columnspan=5)
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
                          bg='cyan',
                          )
    lb_i_personel.grid(row=2, column=5, pady=30)

    ent_i_personel = Entry(top_info,
                           width=10,
                           relief='sunken',
                           bd=4,
                           justify='right'
                           )
    ent_i_personel.grid(row=2, column=4)
    ent_i_personel.focus()

    lb_i_name = Label(top_info,
                      text=': نام',
                      font=label_font,
                      relief='raised',
                      bg='cyan',
                      width=12,
                      padx=10,
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
                        bg='cyan',
                        padx=10,
                        width=12,
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
                     bg='cyan',
                     padx=10,
                     width=12,
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
                      bg='cyan',
                      padx=10,
                      width=12,
                      )
    lb_i_meli.grid(row=6, column=5)

    ent_i_meli = Entry(top_info,
                       relief='sunken',
                       bd=4,
                       justify='right'
                       )
    ent_i_meli.grid(row=6, column=4, pady=5)

    lb_i_bsal = Label(top_info,
                      text=': دستمزد ساعتی',
                      font=label_font,
                      relief='raised',
                      bg='cyan',
                      padx=10,
                      width=12,
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
                        bg='cyan',
                        padx=10,
                        width=12,
                        )
    lb_i_degree.grid(row=9, column=5)

    ent_i_degree = Entry(top_info,
                         relief='sunken',
                         bd=4,
                         justify='right'
                         )
    ent_i_degree.grid(row=9, column=4, pady=5)

    lb_i_children = Label(top_info, text=': تعداد فرزند',font=label_font,relief='raised',bg='cyan',padx=10,width=12,)
    lb_i_children.grid(row=10, column=5, pady=10)

    ent_i_children = Entry(top_info, justify=RIGHT, relief='sunken', bd=4)
    ent_i_children.grid(row=10, column=4, pady=10)

    lb_i_ax = Label(top_info,
                    text=': عکس کارمند',
                    font=label_font,
                    relief='raised',
                    bg='cyan',
                    padx=10,
                    width=12,
                    )
    lb_i_ax.grid(row=11, column=5, pady=10)

    ent_i_ax = Entry(top_info,
                     relief='sunken',
                     bd=4,
                     justify='right', )
    ent_i_ax.grid(row=11, column=4)

    ######buttons
    btn_i_ax = Button(top_info,
                      text='انتخاب عکس',
                      font=bold_font,
                      height=1,
                      width=10,
                      command=choose_image
                      )
    btn_i_ax.grid(row=12, column=4, pady=5)

    btn_i_save = Button(top_info,
                        command=zakhireh_karmand,
                        text='ثبت کاربر',
                        font=label_font)
    btn_i_save.grid(row=13, column=5)

    btn_i_exit = Button(top_info,
                        text='خروج',
                        font=label_font,
                        command=close)
    btn_i_exit.grid(row=13, column=4)

    top_info.mainloop()


#########open virayesh info
def edit():


    # function
    def zakhireh_virayesh_karmand():
        if messagebox.askyesno(title='ذخیره اطلاعات', message='آیا از صحت اطلاعات مطمئن هستید؟'):
            personel_code = ent_v_personel.get()
            name = ent_v_name.get()
            family_name = ent_v_family.get()
            job = ent_v_job.get()
            meli_id = ent_v_meli.get()
            hoghugh_payeh = ent_v_bsal.get()
            degree = ent_v_degree.get()
            children = ent_v_children.get()
            image_link = img_v_ax['file']

            if not hoghugh_payeh.isdigit():
                messagebox.showwarning('خطا','حقوق باید عدد باشد')

            elif name == '':
                messagebox.showwarning('خطا','لطفا یک اسم انتخاب کنید ')

            elif family_name == '':
                messagebox.showwarning('خطا','لطفا یک نام خانوادگی انتخاب کنید ')

            elif job == '':
                messagebox.showwarning('خطا','لطفا شغل را وارد نمایید ')

            elif meli_id == '':
                messagebox.showwarning('خطا','لطفا  کد ملی را وارد نمایید ')

            elif hoghugh_payeh == '':
                messagebox.showwarning('خطا','لطفا حقوق پایه را وارد کنید ')

            elif degree == '':
                messagebox.showwarning('خطا','لطفا مدرک تحصیلی را وارد نمایید ')

            elif children == '':
                messagebox.showwarning('خطا','لطفا تعداد فرزند وارد شود ')

            # elif image_link == '':
            #     messagebox.showwarning('خطا','لطفا یک عکس بارگذاری کنید ')

            else:
                f = open('emp.txt',mode='r')
                lst = f.readlines()

                temp = []
                for item in lst:
                    temp.append(item.strip('\n').split(','))

                for i in range(len(temp)):
                    if temp[i][0] == ent_v_personel.get():
                        temp[i] = [personel_code,name,family_name,job,meli_id,hoghugh_payeh,degree,children,image_link]
                    print(temp[i][0])

                new_lst = []
                for i in temp:
                    str1 = f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]},{i[8]}\n'
                    new_lst.append(str1)

                f = open('emp.txt', mode='w')
                f.writelines(new_lst)
                f.close()


            # lst2 = []
            # with open('emp.txt') as f:
            #     for line in f:
            #         personel, *lst = line.split(',')
            #         # emp = emp.strip(' ')
            #         # info = info.strip(' ')
            #         lst2.append(personel)
            # if ent_v_personel.get() not in lst2:
            #     messagebox.showwarning('خطا', 'پرسنل مورد نظر یافت نشد')
            #
            #
            # with open('emp.txt') as f:
            #     for line in f:
            #         personel, *lst = line.split(',')
            #         # emp = emp.strip(' ')
            #         # info = info.strip(' ')
            #         if personel == ent_v_personel.get():
            #             with open('emp.txt', 'a') as fw:
            #                 fw.write(f'{personel_code},{name},{family_name},{job},{meli_id},{hoghugh_payeh},{degree},{children},{image_link}\n')
            #
            #                 messagebox.showinfo(title='انجام شد', message='اطلاعات با موفقیت ذخیره شد')


    def show_personel():
        f = open('emp.txt', mode='r')
        lst = f.readlines()

        temp = []
        for item in lst:
            temp.append(item.strip('\n').split(','))
        # f = open('emp1.txt', mode='w')
        # f.writelines(f'{temp}')

        lst_error = list()
        for j in range(len(temp)):
            lst_error.append(temp[j][0])

        if ent_v_personel.get() not in lst_error:
            messagebox.showwarning('اخطار', 'پرسنل مورد نظر یافت نشد!')


        for i in temp:
            if f'{i[0]}' == ent_v_personel.get():
                ent_v_name.delete(0,END)
                ent_v_name.insert(0,i[1])
                ent_v_family.delete(0,END)
                ent_v_family.insert(0,f'{i[2]}')
                ent_v_job.delete(0,END)
                ent_v_job.insert(0,f'{i[3]}')
                ent_v_meli.delete(0, END)
                ent_v_meli.insert(0,f'{i[4]}')
                ent_v_bsal.delete(0,END)
                ent_v_bsal.insert(0,f'{i[5]}')
                ent_v_degree.delete(0,END)
                ent_v_degree.insert(0,f'{i[6]}')
                ent_v_children.delete(0,END)
                ent_v_children.insert(0,f'{i[7]}')

                img_v_ax['file'] = i[8]



        f.close()


        # lst2 = []
        # with open('emp.txt') as f:
        #     for line in f:
        #         personel, *lst = line.split(',')
        #         # emp = emp.strip(' ')
        #         # info = info.strip(' ')
        #         lst2.append(personel)
        # if ent_v_personel.get() not in lst2:
        #     messagebox.showwarning('خطا', 'پرسنل مورد نظر یافت نشد')
        #
        # with open('emp.txt') as f:
        #     for line in f:
        #         emp, *lst = line.split(',')
        #         # emp = emp.strip(' ')
        #         # info = info.strip(' ')
        #         if emp == ent_v_personel.get():
        #             ent_v_name.delete(0,END)
        #             ent_v_name.insert(0,lst[0])
        #             ent_v_family.delete(0,END)
        #             ent_v_family.insert(0,lst[1])
        #             ent_v_job.delete(0,END)
        #             ent_v_job.insert(0,lst[2])
        #             ent_v_meli.delete(0, END)
        #             ent_v_meli.insert(0,lst[3])
        #             ent_v_bsal.delete(0,END)
        #             ent_v_bsal.insert(0,lst[4])
        #             ent_v_degree.delete(0,END)
        #             ent_v_degree.insert(0,lst[5])
        #             ent_v_children.delete(0,END)
        #             ent_v_children.insert(0,lst[6])
        #
        #             img_v_ax['file'] = lst[7]


    def close():
        if messagebox.askyesno(title='خروج', message='آیا از خروج مطمئن هستید؟', ):
            top_virayesh.destroy()

    ##### panel
    global top_virayesh
    top_virayesh = Toplevel()
    top_virayesh.geometry('300x670+1000+100')
    top_virayesh.title('ورود اطلاعات کاربر')
    top_virayesh.iconbitmap('salary.ico')
    top_virayesh.configure(background='cyan')


    #window state
    # if top_info.state() == 'normal':
    #     top_info.state('withdrawn')
    #
    # else:
    #     top_info.state('withdrawn')
    #     top_virayesh.state('normal')
    #
    # if top_hoghugh_calc.state() == 'normal':
    #     top_hoghugh_calc.state('withdrawn')
    #
    # else:
    #     top_hoghugh_calc.state('withdrawn')


    # top_virayesh.protocol("WM_DELETE_WINDOW", close)

    # lables
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
                          bg='cyan',
                          )
    lb_v_personel.grid(row=2, column=5, pady=30)

    ent_v_personel = Entry(top_virayesh,
                           width=5,
                           relief='sunken',
                           bd=4,
                           justify='right',
                           )
    ent_v_personel.grid(row=2, column=4, columnspan=2)
    ent_v_personel.focus()

    lb_v_name = Label(top_virayesh,
                      text=': نام',
                      font=label_font,
                      relief='raised',
                      bg='cyan',
                      width=12,
                      padx=10
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
                        bg='cyan',
                        width=12,
                        padx=10

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
                     bg='cyan',
                     width=12,
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
                    bg='cyan',
                    width=12,
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
                      text=': دستمزد ساعتی',
                      font=label_font,
                      relief='raised',
                      bg='cyan',
                      width=12,
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
                        bg='cyan',
                        width=12,
                        padx=10
                        )
    lb_v_degree.grid(row=9, column=5)

    ent_v_degree = Entry(top_virayesh,
                         relief='sunken',
                         bd=4,
                         justify='right'
                         )
    ent_v_degree.grid(row=9, column=4, pady=5)

    lb_v_children = Label(top_virayesh, text=': تعداد فرزند', font=label_font, relief='raised', bg='cyan',width=12, padx=10)
    lb_v_children.grid(row=10, column=5, pady=10)

    ent_v_children = Entry(top_virayesh, justify=RIGHT, relief='sunken', bd=4)
    ent_v_children.grid(row=10, column=4, pady=10,)

    img_v_ax = PhotoImage(file='')
    lb_im_v = Label(top_virayesh, image=img_v_ax)
    lb_im_v.grid(row=12, column=4, columnspan=2)


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



####open fish hoghughi_calc
def fish_hoghugh_calc():
    ##########open fish_hoghughi
    def fish_hoghugh():
        #########functions
        try:
            def tax():
                if int(hoghugh) < 5600000:
                    tax = 0
                elif int(hoghugh) >= 5600000 and int(hoghugh) < 15000000:
                    tax = 0.1
                elif int(hoghugh) >= 15000000 and int(hoghugh) < 25000000:
                    tax = 0.15
                elif int(hoghugh) >= 25000000 and int(hoghugh) < 30000000:
                    tax = 0.2
                else:
                    tax = 0.3
                return tax


            #######variables
            hagh_maskan = 650000
            bon_kargari = 850000
            payeh_sanavat = 210000


            personel = ent_f_personel.get()
            name = ent_f_name.get()
            last = ent_f_family.get()
            job = ent_f_job.get()
            id = ent_f_meli.get()
            degree = ent_f_degree.get()
            children = ent_f_children.get()
            work_hours = ent_f_workday.get()
            hoghugh = int(work_hours) * int(ent_f_sal.get())
            shift = ent_f_shift.get()
            off_shift = ent_f_off_shift.get()
            hagh_olad = 417975 * int(children)

            if personel == '':
                messagebox.showwarning('خطا', 'لطفا یک پرسنل انتخاب کنید ')

            elif work_hours == '':
                messagebox.showwarning('خطا', 'لطفا ساعت کارکرد را وارد نمایید ')

            elif shift == '':
                messagebox.showwarning('خطا', 'لطفا ساعت اضافه کاری را وارد نمایید ')

            elif off_shift == '':
                messagebox.showwarning('خطا', 'لطفا ساعت تعطیل کاری را وارد نمایید ')

            else:
                sum_pay = int(hoghugh) + int(hagh_olad) + int(hagh_maskan) + hagh_olad + bon_kargari + (int(hoghugh) / 220 * 1.4 * int(shift)) + (int(hoghugh) / 220 * 1.4 * int(off_shift))
                sub_pay = (tax() * int(hoghugh)) + (0.07 * int(hoghugh)) + (0.03 * int(hoghugh))
                net_pay = sum_pay - sub_pay

                # lst = [f'{name},{last},{job},{id},{hoghugh},{degree},{children},{work_hours}, {shift}, {off_shift}']
                # f = open('fish_hoghughi_calc.txt', mode='w')
                # f.writelines(lst)
                # f.close()

                #####panel
                top_hoghugh_calc.state('withdrawn')
                top_fish_hoghughi = Toplevel()
                top_fish_hoghughi.geometry('1350x470+100+200')
                top_fish_hoghughi.title('فیش حقوقی')
                top_fish_hoghughi.configure(bg=co7)
                top_fish_hoghughi.resizable(0,0)
                top_fish_hoghughi.iconbitmap('salary.ico')


                ########labels
                #####frame 1
                frm_h_top = LabelFrame(top_fish_hoghughi)
                frm_h_top.grid(row=0, column=1, columnspan=6, padx=5, sticky='we')

                global img_hoghugh
                img_hoghugh = PhotoImage(file='payday.png')
                lb_h_img = Label(frm_h_top, image=img_hoghugh)
                lb_h_img.grid(row=1, column=1, rowspan=2, sticky='w')

                lb_h_name = Label(frm_h_top, text=': نام و نام خانوادگی', font=regular_font)
                lb_h_name.grid(row=1, column=7)

                ent_h_name = Label(frm_h_top, width=30, text=f'{name} {last}', font=label_font, anchor='e')
                ent_h_name.grid(row=1, column=6)

                lb_h_meli = Label(frm_h_top, text=': کد ملی', font=regular_font)
                lb_h_meli.grid(row=1, column=5)

                ent_h_meli = Label(frm_h_top, width=30, text=f'{id}', font=label_font, anchor='e')
                ent_h_meli.grid(row=1, column=4)

                lb_h_personel = Label(frm_h_top, text=': شماره پرسنلی', font=regular_font)
                lb_h_personel.grid(row=1, column=3)

                ent_h_personel = Label(frm_h_top, width=30, text=f'{personel}', font=label_font, anchor='e')
                ent_h_personel.grid(row=1, column=2)
                ent_h_personel.focus()

                lb_h_acc = Label(frm_h_top, text=': شماره حساب بانکی', font=regular_font)
                lb_h_acc.grid(row=2, column=7)

                ent_h_acc = Label(frm_h_top, width=30, text='---', font=label_font, anchor='e')
                ent_h_acc.grid(row=2, column=6)

                lb_h_work = Label(frm_h_top, text=': محل کار', font=regular_font)
                lb_h_work.grid(row=2, column=5)

                ent_h_work = Label(frm_h_top, width=30, text='---', font=label_font, anchor='e')
                ent_h_work.grid(row=2, column=4)


                ##########frame 2
                frm_h_header = Frame(top_fish_hoghughi, bg=co2, pady=15)
                frm_h_header.grid(row=1, column=1, columnspan=6, sticky='we', padx=5)

                lb_h_bonus = Label(frm_h_header, text='مزایا', font=bold_font, bg=co2, width=30)
                lb_h_bonus.grid(row=1, column=3)

                lb_h_subs = Label(frm_h_header, text='کسور', font=bold_font, bg=co2, width=30)
                lb_h_subs.grid(row=1, column=2)

                lb_h_others = Label(frm_h_header, text='سایر اطلاعات', font=bold_font, bg=co2, width=30)
                lb_h_others.grid(row=1, column=1)

                lb_h_loan = Label(frm_h_header, text='وام', font=bold_font, bg=co2, width=30)
                lb_h_loan.grid(row=1, column=0)

                #####frame 3
                frm_h_main_1 = LabelFrame(top_fish_hoghughi, bd=2)
                frm_h_main_1.grid(row=3, column=4, sticky='nswe', padx=5, pady=5)

                lb_h_hoghugh1 = Label(frm_h_main_1, text=': حقوق پایه', font=regular_font, padx=40)
                lb_h_hoghugh1.grid(row=1, column=2, pady=5)
                ent_h_hoghugh2 = Label(frm_h_main_1, text=f'{int(hoghugh):,} T', font=regular_font, padx=10)
                ent_h_hoghugh2.grid(row=1, column=1, sticky='w')

                lb_h_olad = Label(frm_h_main_1, text=': حق اولاد', font=regular_font, padx=65, anchor='e')
                lb_h_olad.grid(row=2, column=2, pady=5, sticky='e')
                ent_h_olad = Label(frm_h_main_1, text=f'{int(hagh_olad):,} T', font=regular_font, anchor='e', padx=40)
                ent_h_olad.grid(row=2, column=1, sticky='w')

                lb_h_prop = Label(frm_h_main_1, text=': حق مسکن', font=regular_font, padx=65, anchor='e')
                lb_h_prop.grid(row=3, column=2, pady=5, sticky='e')
                ent_h_prop = Label(frm_h_main_1, text=f'{int(hagh_maskan):,} T', font=regular_font, anchor='e', padx=40)
                ent_h_prop.grid(row=3, column=1)

                # lb_h_san = Label(frm_h_main_1, text=': سنوات', font=regular_font, padx=65, anchor='e')
                # lb_h_san.grid(row=4, column=2, pady=5, sticky='e')
                # ent_h_san = Label(frm_h_main_1, text=f'{(int(hoghugh) * 2 / 3 + int(payeh_sanavat)):,.0f} T', font=regular_font, anchor='e', padx=40)
                # ent_h_san.grid(row=4, column=1)

                lb_h_coup = Label(frm_h_main_1, text=': بن غذا', font=regular_font, padx=65, anchor='e')
                lb_h_coup.grid(row=5, column=2, pady=5, sticky='e')
                ent_h_coup = Label(frm_h_main_1, text=f'{int(bon_kargari):,} T', font=regular_font, anchor='e', padx=40)
                ent_h_coup.grid(row=5, column=1, )

                lb_h_off = Label(frm_h_main_1, text=': اضافه کاری', font=regular_font, padx=40, anchor='e')
                lb_h_off.grid(row=6, column=2, pady=5, sticky='e')
                ent_h_off = Label(frm_h_main_1, text=f'{int(hoghugh)/220 * 1.4 * int(shift):,.0f} T', font=regular_font, anchor='e', padx=10)
                ent_h_off.grid(row=6, column=1)

                lb_h_off = Label(frm_h_main_1, text=': تعطیل کاری', font=regular_font, padx=40, anchor='e')
                lb_h_off.grid(row=7, column=2, pady=5, sticky='e')
                ent_h_off = Label(frm_h_main_1, text=f'{int(hoghugh) / 220 * 1.4 * int(off_shift):,.0f} T', font=regular_font, anchor='e', padx=10)
                ent_h_off.grid(row=7, column=1)

                frm_h_main_2 = LabelFrame(top_fish_hoghughi, bd=2)
                frm_h_main_2.grid(row=3, column=3, sticky='ns', pady=5)

                lb_h_tax = Label(frm_h_main_2, text='مالیات', font=regular_font, padx=40)
                lb_h_tax.grid(row=1, column=2, pady=5, sticky='e')

                ent_h_tax = Label(frm_h_main_2, text=f'{tax() * int(hoghugh):,.0f} T', font=regular_font, padx=40)
                ent_h_tax.grid(row=1, column=1)

                lb_h_ins = Label(frm_h_main_2, text='بیمه سهم کارمند', font=regular_font, padx=40)
                lb_h_ins.grid(row=2, column=2, pady=5)

                ent_h_ins = Label(frm_h_main_2, text=f'{0.07 * int(hoghugh):,.0f} T', font=regular_font, padx=40)
                ent_h_ins.grid(row=2, column=1)

                lb_h_saving = Label(frm_h_main_2, text='پس انداز', font=regular_font, padx=40)
                lb_h_saving.grid(row=3, column=2, pady=5, sticky='e')

                ent_h_saving = Label(frm_h_main_2, text=f'{0.03 * int(hoghugh):,.0f} T', font=regular_font, padx=40)
                ent_h_saving.grid(row=3, column=1)

                frm_h_main_3 = LabelFrame(top_fish_hoghughi, bd=2, pady=5)
                frm_h_main_3.grid(row=3, column=2, sticky='nsew', pady=5)

                lb_h_san = Label(frm_h_main_3, text=': سنوات', font=regular_font, padx=40, anchor='e')
                lb_h_san.grid(row=3, column=2, pady=5, sticky='e')
                ent_h_san = Label(frm_h_main_3, text=f'{((int(hoghugh) * 2 / 3 + int(payeh_sanavat))/12):,.0f} T',
                                  font=regular_font, anchor='e')
                ent_h_san.grid(row=3, column=1,pady=5,sticky='e')

                lb_h_shifthr = Label(frm_h_main_3, text='کارکرد اضافه کاری', font=regular_font, padx=40)
                lb_h_shifthr.grid(row=1, column=2, pady=5)

                ent_h_shifthr = Label(frm_h_main_3, text=f'{shift} h', font=regular_font, anchor='n', padx=40)
                ent_h_shifthr.grid(row=1, column=1, sticky='e')

                lb_h_offhr = Label(frm_h_main_3, text='کارکرد تعطیل کاری', font=regular_font, padx=40)
                lb_h_offhr.grid(row=2, column=2, pady=5)

                ent_h_offhr = Label(frm_h_main_3, text=f'{off_shift} h', font=regular_font, anchor='n', padx=40)
                ent_h_offhr.grid(row=2, column=1, sticky='e')

                frm_h_main_4 = LabelFrame(top_fish_hoghughi, bd=2)
                frm_h_main_4.grid(row=3, column=1, pady=5, sticky='nsew', padx=5)

                lb_h_loan = Label(frm_h_main_4, text='', font=regular_font, padx=60, anchor='e')
                lb_h_loan.grid(row=6, column=2, pady=5)
                ent_h_loan = Label(frm_h_main_4, text='', font=regular_font, anchor='e', padx=60)
                ent_h_loan.grid(row=6, column=1)

                ########frame 4
                frm_h_footer = LabelFrame(top_fish_hoghughi, bd=2, bg=co2, pady=10)
                frm_h_footer.grid(row=4, column=1, columnspan=6, sticky='we', padx=5)

                lb_h_sum = Label(frm_h_footer, text=': جمع مزایا', font=regular_font, anchor='e', bg=co2, width=15)
                lb_h_sum.grid(row=1, column=6,sticky='e')

                lb_h_sumn = Label(frm_h_footer, text=f'{sum_pay:,.0f} T', font=regular_font, anchor='e', bg=co2, width=25)
                lb_h_sumn.grid(row=1, column=5,sticky='e')

                lb_h_sub = Label(frm_h_footer, text=': جمع کسور', font=regular_font, anchor='e', bg=co2, width=15)
                lb_h_sub.grid(row=1, column=4,sticky='e')

                lb_h_subn = Label(frm_h_footer, text=f'{sub_pay:,.0f} T', font=regular_font, anchor='e', bg=co2, width=25)
                lb_h_subn.grid(row=1, column=3,sticky='e')

                lb_h_net = Label(frm_h_footer, text=': خالص پرداختی', font=regular_font, anchor='e', bg=co2, width=15)
                lb_h_net.grid(row=1, column=2,sticky='e')

                lb_h_netn = Label(frm_h_footer, text=f'{net_pay:,.0f} T', font=regular_font, bg=co2, width=25, anchor='e')
                lb_h_netn.grid(row=1, column=1,sticky='e')

                lb_h_net = Label(frm_h_footer, text='   ', font=regular_font, anchor='e', bg=co2, width=15)
                lb_h_net.grid(row=1, column=0, sticky='e')

                # lb_h_netn = Label(frm_h_footer, text=f'{net_pay:,.0f} T', font=regular_font, bg=co2, width=25, anchor='e')
                # lb_h_netn.grid(row=1, column=1, sticky='e')
        except ValueError:
            messagebox.showwarning('خطا','لطفا تمام مقادیر خواسته شده را وارد نمایید')


    ######functions
    def search():
        # name = ent_f_name.get()
        # last = ent_f_family.get()
        # job = ent_f_job.get()
        # id = ent_f_meli.get()
        # hoghugh = ent_f_sal.get()
        # degree = ent_f_degree.get()
        # children = ent_f_children.get()
        # work_day = ent_f_workday.get()
        # shift = ent_f_shift.get()
        # off_shift = ent_f_off_shift.get()


        f = open('emp.txt',mode='r')
        lst = f.readlines()

        temp = []
        for item in lst:
            temp.append(item.strip('\n').split(','))

        for i in range(len(temp)):
            if temp[i][0] == ent_f_personel.get():
                ent_f_name.delete(0,END)
                ent_f_name.insert(0,temp[i][1])
                ent_f_family.delete(0,END)
                ent_f_family.insert(0,temp[i][2])
                ent_f_job.delete(0,END)
                ent_f_job.insert(0,temp[i][3])
                ent_f_meli.delete(0,END)
                ent_f_meli.insert(0,temp[i][4])
                ent_f_sal.delete(0,END)
                ent_f_sal.insert(0,temp[i][5])
                ent_f_degree.delete(0,END)
                ent_f_degree.insert(0,temp[i][6])
                ent_f_children.delete(0,END)
                ent_f_children.insert(0,temp[i][7])

                for i in temp:
                    if f'{i[0]}' == ent_f_personel.get():
                        for k in range(len(temp)):
                            if ent_f_personel.get() == f'{temp[k][0]}':
                                ent_f_name['state'] = 'disabled'
                                ent_f_family['state'] = 'disabled'
                                ent_f_job['state'] = 'disabled'
                                ent_f_meli['state'] = 'disabled'
                                ent_f_sal['state'] = 'disabled'
                                ent_f_degree['state'] = 'disabled'
                                ent_f_children['state'] = 'disabled'
                            else:
                                ent_f_name['state'] = 'normal'
                                ent_f_family['state'] = 'normal'
                                ent_f_job['state'] = 'normal'
                                ent_f_meli['state'] = 'normal'
                                ent_f_sal['state'] = 'normal'
                                ent_f_degree['state'] = 'normal'
                                ent_f_children['state'] = 'normal'

                                ent_f_name.delete(0, END)
                                ent_f_name.insert(0, f'{i[1]}')
                                ent_f_family.delete(0, END)
                                ent_f_family.insert(0, f'{i[2]}')
                                ent_f_job.delete(0, END)
                                ent_f_job.insert(0, f'{i[3]}')
                                ent_f_meli.delete(0, END)
                                ent_f_meli.insert(0, f'{i[4]}')
                                ent_f_sal.delete(0, END)
                                ent_f_sal.insert(0, f'{i[5]}')
                                ent_f_degree.delete(0, END)
                                ent_f_degree.insert(0, f'{i[6]}')
                                ent_f_children.delete(0, END)
                                ent_f_children.insert(0, f'{i[7]}')

                                # img_f_ax['file'] = i[8]

                                ent_f_name['state'] = 'disabled'
                                ent_f_family['state'] = 'disabled'
                                ent_f_job['state'] = 'disabled'
                                ent_f_meli['state'] = 'disabled'
                                ent_f_sal['state'] = 'disabled'
                                ent_f_degree['state'] = 'disabled'
                                ent_f_children['state'] = 'disabled'

        f.close()


        # with open('emp.txt') as f:
        #     lst2 = []
        #     for line in f:
        #         personel, lst = line.split('=')
        #         personel = personel.strip(' ')
        #         lst = lst.strip(' ')
        #         personel = (personel)
        #         lst = lst.strip(' ')
        #         lst2.append(personel)
        #
        #     if ent_f_personel.get() not in lst2:
        #         messagebox.showwarning('اخطار', 'پرسنل مورد نظر یافت نشد!')
        #
        # with open('emp.txt') as f:
        #     for line in f:
        #         personel, lst = line.split('=')
        #         personel = personel.strip(' ')
        #         lst = lst.strip(' ')
        #         if personel == ent_f_personel.get():
        #             ent_f_name.delete(0, END)
        #             ent_f_name.insert(0, lst[0])
        #             # ent_f_name['state'] = DISABLED
        #             ent_f_family.delete(0, END)
        #             ent_f_family.insert(0, lst)
        #             # ent_f_family['state'] = DISABLED
        #             ent_f_job.delete(0, END)
        #             ent_f_job.insert(0, lst)
        #             # ent_f_job['state'] = DISABLED
        #             ent_f_meli.delete(0, END)
        #             ent_f_meli.insert(0, lst)
        #             # ent_f_meli['state'] = DISABLED
        #             ent_b_sal.delete(0, END)
        #             ent_b_sal.insert(0, lst)
        #             # ent_b_sal['state'] = DISABLED
        #             ent_f_degree.delete(0, END)
        #             ent_f_degree.insert(0, lst)
        #             # ent_f_degree['state'] = DISABLED


    #####panel
    global top_hoghugh_calc
    top_hoghugh_calc = Toplevel()
    top_hoghugh_calc.geometry('1210x515+100+200')
    top_hoghugh_calc.title('محاسبه فیش حقوقی')
    top_hoghugh_calc.configure(bg='cyan')
    top_hoghugh_calc.iconbitmap('salary.ico')


    #######labels
    global img_invoice
    img_invoice = PhotoImage(file='invoice.png')
    lb_invoice = Label(top_hoghugh_calc, image=img_invoice)
    lb_invoice.grid(row=1, column=1, rowspan=10)

    frm_f_right = LabelFrame(top_hoghugh_calc,bd=4,padx=70,pady=10,bg=co8)
    frm_f_right.grid(row=1,column=3,rowspan=10,sticky='ns')

    frm_f_middle = LabelFrame(top_hoghugh_calc, bd=4, padx=10, pady=10, bg=co8)
    frm_f_middle.grid(row=1, column=2,rowspan=10,sticky='ns')

    lb_titr2 = Label(frm_f_middle, text='پس از وارد کردن مقادیر دکمه فیش حقوقی را بزنید', font=bold_font,bg=co8,fg=co1,pady=30)
    lb_titr2.grid(row=1, column=3, columnspan=2)

    d= {'font' : regular_font, 'bg' : co8, 'fg' : co1}

    lb_f_workday = Label(frm_f_middle, text=': ساعات کار کرد', **d)
    lb_f_workday.grid(row=2, column=4, sticky='s', pady=10)

    ent_f_workday = Entry(frm_f_middle, justify=RIGHT, relief='sunken', bd=4)
    ent_f_workday.grid(row=2, column=3, sticky='es', pady=10)

    lb_f_shift = Label(frm_f_middle, text=': ساعات اضافه کاری', **d)
    lb_f_shift.grid(row=3, column=4, pady=10)

    ent_f_shift = Entry(frm_f_middle, justify=RIGHT, relief='sunken', bd=4)
    ent_f_shift.grid(row=3, column=3, sticky='e', pady=10)

    lb_f_off_shift = Label(frm_f_middle, text=': ساعات تعطیل کاری', **d)
    lb_f_off_shift.grid(row=4, column=4, pady=10)

    ent_f_off_shift = Entry(frm_f_middle, justify=RIGHT, relief='sunken', bd=4)
    ent_f_off_shift.grid(row=4, column=3, sticky='e', pady=10)



    lb_titr = Label(frm_f_right, text='''برای محاسبه حقوق پرسنل مورد
     نظر،کد آن را جست و جو کنید''', font=bold_font,
                    bg=co8,fg=co1)
    lb_titr.grid(row=1, column=5, pady=20, padx=20, columnspan=2)

    lb_f_personel = Label(frm_f_right,
                          text=': کد پرسنل',
                          **d
                          )
    lb_f_personel.grid(row=2, column=6, pady=30)

    ent_f_personel = Entry(frm_f_right,
                           width=5,
                           relief='sunken',
                           bd=4,
                           justify='right',
                           )
    ent_f_personel.grid(row=2, column=5,sticky='e')

    lb_f_name = Label(frm_f_right,
                      text=': نام',
                      **d
                      )
    lb_f_name.grid(row=3, column=6)

    ent_f_name = Entry(frm_f_right,
                       relief='sunken',
                       bd=4,
                       justify=RIGHT,
                       # state=DISABLED,
                       )
    ent_f_name.grid(row=3, column=5, pady=10, sticky='e')

    lb_f_family = Label(frm_f_right,
                        text=': نام خانوادگی',
                        **d
                        )
    lb_f_family.grid(row=4, column=6)

    ent_f_family = Entry(frm_f_right,
                         relief='sunken',
                         bd=4,
                         justify=RIGHT
                         )
    ent_f_family.grid(row=4, column=5, pady=5, sticky='e')

    lb_f_job = Label(frm_f_right,
                     text=': شغل',
                     **d
                     )
    lb_f_job.grid(row=5, column=6)

    ent_f_job = Entry(frm_f_right,
                      relief='sunken',
                      bd=4,
                      justify='right'
                      )
    ent_f_job.grid(row=5, column=5, pady=5, sticky='e')

    lb_f_meli = Label(frm_f_right,
                      text=': کد ملی',
                      **d
                      )
    lb_f_meli.grid(row=6, column=6, sticky='n')

    ent_f_meli = Entry(frm_f_right,
                       relief='sunken',
                       bd=4,
                       justify='right'
                       )
    ent_f_meli.grid(row=6, column=5, pady=5, sticky='en')

    lb_f_bsal = Label(frm_f_right,
                      text=': دستمزد ساعتی',
                      **d
                      )
    lb_f_bsal.grid(row=7, column=6)

    ent_f_sal = Entry(frm_f_right,
                      relief='sunken',
                      bd=4,
                      justify='right'
                      )
    ent_f_sal.grid(row=7, column=5, pady=5, sticky='e')

    lb_f_degree = Label(frm_f_right,
                        text=': مدرک تحصیلی',
                        **d
                        )
    lb_f_degree.grid(row=9, column=6)

    ent_f_degree = Entry(frm_f_right,
                         relief='sunken',
                         bd=4,
                         justify='right',
                         )
    ent_f_degree.grid(row=9, column=5, pady=5, sticky='e')


    lb_f_children = Label(frm_f_right,
                       text=': تعداد فرزند',
                       **d
                       )
    lb_f_children.grid(row=10, column=6)

    ent_f_children = Entry(frm_f_right,
                         relief='sunken',
                         bd=4,
                         justify='right',
                         )
    ent_f_children.grid(row=10, column=5, pady=5, sticky='e')

    #########buttons
    btn_f_search = Button(frm_f_right,
                          text='جست و جو',
                          font=label_font,
                          command=search
                          )
    btn_f_search.place(x=15,y=110)

    btn_f_fish = Button(frm_f_middle, text='فیش حقوقی', font=label_font, width=15, command=fish_hoghugh)
    btn_f_fish.grid(row=6, column=3, columnspan=2, pady=30)


#######functions
def show_pass(event=None):
    if ent_pass['show'] == '*':
        ent_pass['show'] = ''
    else:
        ent_pass['show'] = '*'


####panel
win = Tk()
win.geometry('520x300+500+200')
win.title('صفحه ورود')
win.resizable(0,0)
win.iconbitmap('salary.ico')


#######label
lb_user = Label(win,
                text=': نام کاربر',
                font=label_font,
                relief=SUNKEN,
                bg = co2,
                width=10
                )
lb_user.grid(row=1,column=2,pady=50)
lb_user.focus()

lb_pass = Label(win,
                text=': رمز عبور',
                font=label_font,
                relief=SUNKEN,
                bg = co2,
                width=10
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
btn_enter.bind('<Return>',lambda event : enter_samaneh())




win.mainloop()
