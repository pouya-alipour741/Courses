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
top_hoghugh_calc = Toplevel()
top_hoghugh_calc.geometry('1300x515+100+200')
top_hoghugh_calc.title('محاسبه فیش حقوقی')
top_hoghugh_calc.configure(bg='cyan')


##########open fish_hoghughi function
def fish_hoghughi_open():
    #####panel
    top_hoghugh_calc.state('withdrawn')
    top_fish_hoghughi = Toplevel()
    top_fish_hoghughi.geometry('1300x470+100+200')
    top_fish_hoghughi.title('فیش حقوقی')
    top_fish_hoghughi.configure(bg='grey')

    ########labels
    #####frame 1
    frm_h_top = LabelFrame(top_fish_hoghughi)
    frm_h_top.grid(row=0, column=1, columnspan=6, padx=5, sticky='we')

    lb_h_name = Label(frm_h_top, text=': نام و نام خانوادگی', font=regular_font)
    lb_h_name.grid(row=1, column=7)

    ent_h_name = Label(frm_h_top, width=30, text='پویا شیر علی پور', font=label_font, anchor='e')
    ent_h_name.grid(row=1, column=6)

    lb_h_meli = Label(frm_h_top, text=': کد ملی', font=regular_font)
    lb_h_meli.grid(row=1, column=5)

    ent_h_meli = Label(frm_h_top, width=30, text='9482', font=label_font, anchor='e')
    ent_h_meli.grid(row=1, column=4)

    lb_h_personel = Label(frm_h_top, text=': شماره پرسنلی', font=regular_font)
    lb_h_personel.grid(row=1, column=3)

    ent_h_personel = Label(frm_h_top, width=30, text='', font=label_font, anchor='e')
    ent_h_personel.grid(row=1, column=2)

    lb_h_acc = Label(frm_h_top, text=': شماره حساب بانکی', font=regular_font)
    lb_h_acc.grid(row=2, column=7)

    ent_h_acc = Label(frm_h_top, width=30, text='---', font=label_font, anchor='e')
    ent_h_acc.grid(row=2, column=6)

    lb_h_work = Label(frm_h_top, text=': محل کار', font=regular_font)
    lb_h_work.grid(row=2, column=5)

    ent_h_work = Label(frm_h_top, width=30, text='---', font=label_font, anchor='e')
    ent_h_work.grid(row=2, column=4)

    img_hoghugh = PhotoImage(file='payday.png')
    lb_h_img = Label(frm_h_top, image=img_hoghugh)
    lb_h_img.grid(row=1, column=1, rowspan=2, sticky='w')

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

    lb_h_hoghugh1 = Label(frm_h_main_1, text='حقوق پایه', font=regular_font, padx=40)
    lb_h_hoghugh1.grid(row=1, column=2, pady=5)
    ent_h_hoghugh2 = Label(frm_h_main_1, text='56000000', font=regular_font, padx=10)
    ent_h_hoghugh2.grid(row=1, column=1, sticky='w')

    lb_h_olad = Label(frm_h_main_1, text='حق اولاد', font=regular_font, padx=65, anchor='e')
    lb_h_olad.grid(row=2, column=2, pady=5, sticky='e')
    ent_h_olad = Label(frm_h_main_1, text='53453', font=regular_font, anchor='e', padx=40)
    ent_h_olad.grid(row=2, column=1, sticky='w')

    lb_h_prop = Label(frm_h_main_1, text='حق مسکن', font=regular_font, padx=65, anchor='e')
    lb_h_prop.grid(row=3, column=2, pady=5, sticky='e')
    ent_h_prop = Label(frm_h_main_1, text='53453', font=regular_font, anchor='e', padx=40)
    ent_h_prop.grid(row=3, column=1)

    lb_h_san = Label(frm_h_main_1, text='پایه سنوات', font=regular_font, padx=65, anchor='e')
    lb_h_san.grid(row=4, column=2, pady=5, sticky='e')
    ent_h_san = Label(frm_h_main_1, text='53453', font=regular_font, anchor='e', padx=40)
    ent_h_san.grid(row=4, column=1)

    lb_h_coup = Label(frm_h_main_1, text='بن غذا', font=regular_font, padx=65, anchor='e')
    lb_h_coup.grid(row=5, column=2, pady=5, sticky='e')
    ent_h_coup = Label(frm_h_main_1, text='53453', font=regular_font, anchor='e', padx=40)
    ent_h_coup.grid(row=5, column=1, )

    lb_h_off = Label(frm_h_main_1, text='تعطیل کاری', font=regular_font, padx=65, anchor='e')
    lb_h_off.grid(row=6, column=2, pady=5, sticky='e')
    ent_h_off = Label(frm_h_main_1, text='53453', font=regular_font, anchor='e', padx=40)
    ent_h_off.grid(row=6, column=1)

    frm_h_main_2 = LabelFrame(top_fish_hoghughi, bd=2)
    frm_h_main_2.grid(row=3, column=3, sticky='ns', pady=5)

    lb_h_tax = Label(frm_h_main_2, text='مالیات', font=regular_font, padx=40)
    lb_h_tax.grid(row=1, column=2, pady=5, sticky='e')

    ent_h_tax = Label(frm_h_main_2, text='53453', font=regular_font, padx=40)
    ent_h_tax.grid(row=1, column=1)

    lb_h_ins = Label(frm_h_main_2, text='بیمه سهم کارمند', font=regular_font, padx=40)
    lb_h_ins.grid(row=2, column=2, pady=5)

    ent_h_ins = Label(frm_h_main_2, text='53453', font=regular_font, padx=40)
    ent_h_ins.grid(row=2, column=1)

    lb_h_saving = Label(frm_h_main_2, text='پس انداز', font=regular_font, padx=40)
    lb_h_saving.grid(row=3, column=2, pady=5, sticky='e')

    ent_h_saving = Label(frm_h_main_2, text='53453', font=regular_font, padx=40)
    ent_h_saving.grid(row=3, column=1)

    frm_h_main_3 = LabelFrame(top_fish_hoghughi, bd=2, pady=5)
    frm_h_main_3.grid(row=3, column=2, sticky='nsew', pady=5)

    lb_h_shifthr = Label(frm_h_main_3, text='کارکرد اضافه کاری', font=regular_font, padx=40)
    lb_h_shifthr.grid(row=1, column=2, pady=5)

    ent_h_shifthr = Label(frm_h_main_3, text='53453', font=regular_font, anchor='n', padx=40)
    ent_h_shifthr.grid(row=1, column=1, sticky='e')

    lb_h_offhr = Label(frm_h_main_3, text='کارکرد تعطیل کاری', font=regular_font, padx=40)
    lb_h_offhr.grid(row=2, column=2, pady=5)

    ent_h_offhr = Label(frm_h_main_3, text='53453', font=regular_font, anchor='n', padx=40)
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

    lb_h_sum = Label(frm_h_footer, text=': جمع پرداختی', font=regular_font, anchor='e', bg=co2, width=15)
    lb_h_sum.grid(row=1, column=6)

    lb_h_sumn = Label(frm_h_footer, text=' 544', font=regular_font, anchor='e', bg=co2, width=25)
    lb_h_sumn.grid(row=1, column=5)

    lb_h_sub = Label(frm_h_footer, text=': جمع کسورات', font=regular_font, anchor='e', bg=co2, width=15)
    lb_h_sub.grid(row=1, column=4)

    lb_h_subn = Label(frm_h_footer, text='76575675', font=regular_font, anchor='e', bg=co2, width=25)
    lb_h_subn.grid(row=1, column=3)

    lb_h_net = Label(frm_h_footer, text=': خالص پرداختی', font=regular_font, anchor='e', bg=co2, width=15)
    lb_h_net.grid(row=1, column=2)

    lb_h_netn = Label(frm_h_footer, text='7567567', font=regular_font, bg=co2, width=25, anchor='e')
    lb_h_netn.grid(row=1, column=1)



#######labels
img_invoice = PhotoImage(file='invoice.png')
lb_invoice = Label(top_hoghugh_calc, image=img_invoice)
lb_invoice.grid(row=1,column=1,rowspan=10)

lb_titr2 = Label(top_hoghugh_calc, text='پس از وارد کردن مقادیر دکمه فیش حقوقی را وارد کنید', font=bold_font, bg='cyan')
lb_titr2.grid(row=1,column=3,columnspan=2)

lb_f_workday = Label(top_hoghugh_calc, text=': ساعت کار کرد', font=regular_font, bg=co2, relief='raised', bd=2)
lb_f_workday.grid(row=2,column=4,sticky='s',pady=10)

ent_f_workday = Entry(top_hoghugh_calc, justify=RIGHT, relief='sunken', bd=4)
ent_f_workday.grid(row=2,column=3,sticky='es',pady=10)

lb_f_shift = Label(top_hoghugh_calc, text=': ساعات اضافه کاری', font=regular_font, bg=co2, relief='raised', bd=2)
lb_f_shift.grid(row=3,column=4)

ent_f_shift = Entry(top_hoghugh_calc, justify=RIGHT, relief='sunken', bd=4)
ent_f_shift.grid(row=3,column=3,sticky='e')

lb_f_night_shift= Label(top_hoghugh_calc, text=': ساعات شب کاری', font=regular_font, bg=co2, relief='raised', bd=2)
lb_f_night_shift.grid(row=4,column=4)

ent_f_night_shift = Entry(top_hoghugh_calc, justify=RIGHT, relief='sunken', bd=4)
ent_f_night_shift.grid(row=4,column=3,sticky='e')



lb_titr = Label(top_hoghugh_calc, text='برای محاسبه حقوق پرسنل مورد نظر،کد آن را جست و جو کنید', font=bold_font, bg='cyan')
lb_titr.grid(row=1,column=5,pady=20,padx=20,columnspan=2)

lb_f_personel = Label(top_hoghugh_calc,
                      text=': کد پرسنل',
                      font=label_font,
                      relief='raised',
                      bg='grey',
                      )
lb_f_personel.grid(row=2, column=6, pady=30,sticky='w')

ent_f_personel = Entry(top_hoghugh_calc,
                       width=5,
                       relief='sunken',
                       bd=4,
                       justify='right'
                       )
ent_f_personel.grid(row=2, column=5,sticky='e')


lb_f_name = Label(top_hoghugh_calc,
                  text=': نام',
                  font=label_font,
                  relief='raised',
                  bg='grey',
                  )
lb_f_name.grid(row=3, column=6)

ent_f_name = Entry(top_hoghugh_calc,
                   relief='sunken',
                   bd=4,
                   justify=RIGHT,
                   state=DISABLED,
                   )
ent_f_name.grid(row=3, column=5, pady=10,sticky='e')

lb_f_family = Label(top_hoghugh_calc,
                    text=': نام خانوادگی',
                    font=label_font,
                    relief='raised',
                    bg='grey',
                    )
lb_f_family.grid(row=4, column=6)

ent_f_family = Entry(top_hoghugh_calc,
                     relief='sunken',
                     bd=4,
                     justify=RIGHT
                     )
ent_f_family.grid(row=4, column=5, pady=5,sticky='e')

lb_f_job = Label(top_hoghugh_calc,
                 text=': شغل',
                 font=label_font,
                 relief='raised',
                 bg='grey',
                 )
lb_f_job.grid(row=5, column=6)


ent_f_job = Entry(top_hoghugh_calc,
                  relief='sunken',
                  bd=4,
                  justify='right'
                  )
ent_f_job.grid(row=5, column=5,pady=5,sticky='e')

lb_f_meli = Label(top_hoghugh_calc,
                  text=': کد ملی',
                  font=label_font,
                  relief='raised',
                  bg='grey',
                  )
lb_f_meli.grid(row=6, column=6,sticky='n')

ent_f_meli = Entry(top_hoghugh_calc,
                   relief='sunken',
                   bd=4,
                   justify='right'
                   )
ent_f_meli.grid(row=6, column=5,pady=5,sticky='en')

lb_f_bsal = Label(top_hoghugh_calc,
                  text=': حقوق پایه',
                  font=label_font,
                  relief='raised',
                  bg='grey',
                  )
lb_f_bsal.grid(row=7, column=6)

ent_b_sal = Entry(top_hoghugh_calc,
                  relief='sunken',
                  bd=4,
                  justify='right'
                  )
ent_b_sal.grid(row=7, column=5, pady=5,sticky='e')


lb_f_degree = Label(top_hoghugh_calc,
                    text=': مدرک تحصیلی',
                    font=label_font,
                    relief='raised',
                    bg='grey',
                    )
lb_f_degree.grid(row=9, column=6)

ent_f_degree = Entry(top_hoghugh_calc,
                     relief='sunken',
                     bd=4,
                     justify='right'
                     )
ent_f_degree.grid(row=9, column=5, pady=5,sticky='e')

#########buttons
btn_f_search = Button(top_hoghugh_calc,
                      text='جست و جو',
                      font=label_font,
                      )
btn_f_search.grid(row=2, column=4,columnspan=3)


btn_f_fish = Button(top_hoghugh_calc, text='فیش حقوقی', font=label_font, width=15, command=fish_hoghughi_open)
btn_f_fish.grid(row=5,column=3,columnspan=2,pady=30)




top_hoghugh_calc.mainloop()