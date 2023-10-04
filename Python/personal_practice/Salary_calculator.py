from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk

################# colors ###############

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

################# create window ###############

window = Tk ()
window.title ("")
window.geometry('500x350')
window.configure(background=co9)
window.resizable(width=FALSE, height=FALSE)

style = ttk.Style(window)
style.theme_use("clam")


################# Frames ####################

top_frame = Frame(window, width=1043, height=60, pady=5, bg=co1,  relief="flat",)
top_frame.grid(row=0, column=0)

bottom_frame = Frame(window,width=1043, height=400,bg=co1, pady=0, relief="flat")
bottom_frame.grid(row=1, column=0,pady=0, padx=0, sticky=NSEW)

# loading app image

app_lg  = Image.open('png_img.png')
app_lg = app_lg.resize((25, 25))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(top_frame,image=app_lg,  text=" Salary Calculator", width=500, compound=LEFT, relief=RAISED, anchor=SW, font=('Verdana 15'),bg=co1, fg=co4 )
app_logo.place(x=0, y=0)


# salary function
def salary():
    year = 365 
    weeks = 52 

    name = e_name.get()
    hours_per_day = int(e_hours.get())
    work_days = int(e_days_work.get())
    annual_salary = float(e_salary.get())

    # weekly and annually working hours
    weely_working_hours = hours_per_day * work_days
    annually_working_hours = weeks * weely_working_hours


    # Salary per hour
    hourly_wage = annual_salary / annually_working_hours
    
    # daily salary
    daily_salary = hourly_wage * 8

    # weekly salary:
    weekly_salary = annual_salary / 52
    
    # monthly salary:
    monthly_Salary = annual_salary / 12

    # annual salary:
    annual_salary = monthly_Salary * 12
    

    # showing results in labels
    l_name['text'] = name
    l_days['text'] = 'working hours per day: ' + str(hours_per_day)
    l_h_days['text'] = 'working days per week: ' + str(work_days)
    l_anual['text'] = '$ {:,.2f}'.format(annual_salary)
    
    
    # hourly wage
    l_hour['text']  = ' hourly wage: $ {:,.2f}'.format(hourly_wage) 

    # salary per day
    l_day['text'] = ' Daily Salary: $ {:,.2f}'.format(daily_salary) 

    # salary per week
    l_week['text'] =' Weekly Salary: $ {:,.2f}'.format(weekly_salary) 

    # salary per month
    l_month['text'] = ' monthly salary: $ {:,.2f}'.format(monthly_Salary) 

    # salary per year
    l_year['text'] = ' Annual salary: $ {:,.2f}'.format(annual_salary)

l_name = Label(bottom_frame, text="Write your full name ", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_name.place(x=10, y=10)
e_name = Entry(bottom_frame, width=25, justify='left',relief="solid")
e_name.place(x=200, y=11)

l_hours = Label(bottom_frame, text="How many hours do you work per day?", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_hours.place(x=10, y=40)
e_hours = Entry(bottom_frame, width=15, justify='center',relief="solid")
e_hours.place(x=260, y=41)

l_days_work = Label(bottom_frame, text="How many days do you work per week?", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_days_work.place(x=10, y=70)
e_days_work = Entry(bottom_frame, width=15, justify='center',relief="solid")
e_days_work.place(x=260, y=71)

l_salary = Label(bottom_frame, text="What is your Annual Salary?", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_salary.place(x=10, y=100)
e_salary = Entry(bottom_frame, width=15, justify='center',relief="solid")
e_salary.place(x=260, y=101)

# loading image
app_img  = Image.open('salary.jpg')
app_img = app_img.resize((90, 90))
app_img = ImageTk.PhotoImage(app_img)
app_ = Label(bottom_frame, image=app_img, anchor=NW, bg=co1, fg=co4 )
app_.place(x=380, y=0)

app_calculator  = Image.open('salary.jpg')
app_calculator = app_calculator.resize((20, 20))
app_calculator = ImageTk.PhotoImage(app_calculator)
calculate_button = Button(bottom_frame,command=salary, image=app_calculator, compound=LEFT, anchor=NW, text="  Calculate".upper(), width=100,  overrelief=RIDGE, font=('ivy 8 bold'),bg=co1, fg=co0 )
calculate_button.place(x=370, y=100)

# -------------------------result ------------------------

l_name = Label(bottom_frame,width=25, text='' ,relief=RAISED, anchor=NW, padx=5, pady=5, font=('Ivy 10'), bg=co9, fg=co0)
l_name.place(x=10, y=150)
l_days = Label(bottom_frame,width=25, text='' ,relief=RAISED, anchor=NW, padx=5, pady=5, font=('Ivy 10'), bg=co9, fg=co0)
l_days.place(x=10, y=180)
l_h_days = Label(bottom_frame,width=25, text='' ,relief=RAISED, anchor=NW, padx=5, pady=5, font=('Ivy 10'), bg=co9, fg=co0)
l_h_days.place(x=10, y=210)
l_anual = Label(bottom_frame,width=25, text='' ,relief=RAISED, anchor=NW, padx=5, pady=5, font=('Ivy 10 bold'), bg=co9, fg=co0)
l_anual.place(x=10, y=240)

# hourly wage
img_hour  = Image.open('png_img.png')
img_hour = img_hour.resize((20, 20))
img_hour = ImageTk.PhotoImage(img_hour)
l_hour = Label(bottom_frame,image=img_hour,width=300, text='',compound=LEFT, anchor=NW, font=('Ivy 10'), bg=co1, fg=co0)
l_hour.place(x=253, y=140)


# salary per day
img_day  = Image.open('png_img.png')
img_day = img_day.resize((20, 20))
img_day = ImageTk.PhotoImage(img_day)
l_day = Label(bottom_frame,image=img_day,width=300, text='',compound=LEFT, anchor=NW, font=('Ivy 10'), bg=co1, fg=co0)
l_day.place(x=253, y=165)

# salary per week
img_week  = Image.open('png_img.png')
img_week = img_week.resize((20, 20))
img_week = ImageTk.PhotoImage(img_week)
l_week = Label(bottom_frame,image=img_week,width=300, text='',compound=LEFT, anchor=NW, font=('Ivy 10'), bg=co1, fg=co0)
l_week.place(x=253, y=195)

# salary per month
img_month  = Image.open('png_img.png')
img_month = img_month.resize((20, 20))
img_month = ImageTk.PhotoImage(img_month)
l_month = Label(bottom_frame,image=img_month,width=300, text='',compound=LEFT, anchor=NW, font=('Ivy 10'), bg=co1, fg=co0)
l_month.place(x=253, y=225)

# salary per year
img_year  = Image.open('png_img.png')
img_year = img_year.resize((20, 20))
img_year = ImageTk.PhotoImage(img_year)
l_year = Label(bottom_frame,image=img_year,width=300, text='',compound=LEFT, anchor=NW, font=('Ivy 10'), bg=co1, fg=co0)
l_year.place(x=253, y=255)

window.mainloop ()