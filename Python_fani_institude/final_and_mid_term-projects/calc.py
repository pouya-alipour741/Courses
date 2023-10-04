import tkinter as tk
import math

calculation = ''
Pink = '#ff00ff'
blood_red = '#880808'
oprt = '+-*x^/'

dict1 = {'*' : 'x'}

# output = ''
# for letter in calculation:
#     output += dict1.get(letter,letter)


def add_to_calculation(symbol):
    global calculation
    calculation += f'{symbol}'.replace('**','^').replace('*','x')
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)


def eval_calculation():
    global calculation
    try:
        calculation = str(eval(calculation.replace('^','**').replace('x','*')))
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, calculation)
    except:
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, 'ERROR')


def clear_calculation():
    global calculation
    calculation = ''
    text_result.delete(1.0,'end')



def calc_sin():
    global calculation
    calculation = str(math.sin(math.radians(float(calculation))))
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)


def calc_cos():
    global calculation
    calculation = str(math.cos(math.radians(float(calculation))))
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)


def calc_tan():
    global calculation
    calculation = str(math.tan(math.radians(float(calculation))))
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)


def calc_exp():
    global calculation
    calculation = str(math.exp(int(calculation)))
    text_result.delete(1.0,'end')
    text_result.insert(1.0,calculation)


def memory_save():
    global x
    x = str(calculation.replace('**','^').replace('*','x'))


def memory_call():
    global calculation
    global x
    try:
        if calculation[-1] in oprt:
            calculation += x
            text_result.delete(1.0, 'end')
            text_result.insert(1.0, calculation)
        else:
            calculation = x
            text_result.delete(1.0, 'end')
            text_result.insert(1.0, calculation)

    except IndexError:
        calculation = x
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, calculation)


def back():
    global calculation
    lst = []
    for i in calculation:
        lst.append(i)

    del lst[-1]

    calculation = ''.join(lst)
    text_result.delete(1.0,'end')
    text_result.insert(1.0,calculation)


def memory_clear():
    global x
    x = ''
    # text_result.insert(1.0,calculation)



win = tk.Tk()
win.geometry('398x386')
win.resizable(0, 0)
win.title('calculator')
win.iconbitmap('calc.ico')
win.configure(bg=blood_red)

text_result = tk.Text(win,width=22, height=3, font=("Arial", 24))
text_result.grid(row=1,column=1,columnspan=5,sticky='w')


btn_1 = tk.Button(win, text='1', command=lambda: add_to_calculation(1), width=8, font=('Arial', 14))
btn_1.grid(row=2, column=1,sticky=tk.NSEW)
btn_2 = tk.Button(win, text='2', width=8, font=('Arial', 14), command=lambda: add_to_calculation(2))
btn_2.grid(row=2, column=2,sticky=tk.NSEW)
btn_3 = tk.Button(win, text='3', width=8, font=('Arial', 14), command=lambda: add_to_calculation(3))
btn_3.grid(row=2, column=3,sticky=tk.NSEW)
btn_4 = tk.Button(win, text='4', width=8, font=('Arial', 14), command=lambda: add_to_calculation(4))
btn_4.grid(row=3, column=1,sticky=tk.NSEW)
btn_5 = tk.Button(win, text='5', width=8, font=('Arial', 14), command=lambda: add_to_calculation(5))
btn_5.grid(row=3, column=2,sticky=tk.NSEW)
btn_6 = tk.Button(win, text='6', width=8, font=('Arial', 14), command=lambda: add_to_calculation(6))
btn_6.grid(row=3, column=3,sticky=tk.NSEW)
btn_7 = tk.Button(win, text='7', width=8, font=('Arial', 14), command=lambda: add_to_calculation(7))
btn_7.grid(row=4, column=1,sticky=tk.NSEW)
btn_8 = tk.Button(win, text='8', width=8, font=('Arial', 14), command=lambda: add_to_calculation(8))
btn_8.grid(row=4, column=2,sticky=tk.NSEW)
btn_9 = tk.Button(win, text='9', width=8, font=('Arial', 14), command=lambda: add_to_calculation(9))
btn_9.grid(row=4, column=3,sticky=tk.NSEW)
btn_0 = tk.Button(win, text='0', width=8, font=('Arial', 14), command=lambda: add_to_calculation(0))
btn_0.grid(row=5, column=2,sticky=tk.NSEW)
btn_period = tk.Button(win, text='.', width=8, font=('Arial', 14), command=lambda: add_to_calculation('.'))
btn_period.grid(row=6, column=2,sticky=tk.NSEW)
btn_open = tk.Button(win, text='(', width=8, font=('Arial', 14), command=lambda: add_to_calculation('('))
btn_open.grid(row=5, column=1,sticky=tk.NSEW)
btn_close = tk.Button(win, text=')', width=8, font=('Arial', 14), command=lambda: add_to_calculation(')'))
btn_close.grid(row=5, column=3,sticky=tk.NSEW)
btn_add = tk.Button(win, text='+', width=8, font=('Arial', 14), command=lambda: add_to_calculation('+'))
btn_add.grid(row=2, column=4,sticky=tk.NSEW)
btn_minus = tk.Button(win, text='-', width=8, font=('Arial', 14), command=lambda: add_to_calculation('-'))
btn_minus.grid(row=3, column=4,sticky=tk.NSEW)
btn_mul = tk.Button(win, text='*', width=8, font=('Arial', 14), command=lambda: add_to_calculation('*'))
btn_mul.grid(row=4, column=4,sticky=tk.NSEW)
btn_div = tk.Button(win, text='/', width=8, font=('Arial', 14), command=lambda: add_to_calculation('/'))
btn_div.grid(row=5, column=4,sticky=tk.NSEW)


btn_equal = tk.Button(win, text='=', width=8, font=('Arial', 14), command=eval_calculation,bg='cyan')
btn_equal.grid(row=6, column=1,sticky=tk.NSEW)
btn_clear = tk.Button(win, text='C', width=8, font=('Arial', 14), command=clear_calculation,bg='red')
btn_clear.grid(row=6, column=3,sticky=tk.NSEW)
btn_back = tk.Button(win,text='back',width=8,font=('Arial', 14),command=back)
btn_back.grid(row=6,column=4,sticky=tk.NSEW)

#memory call
btn_ms = tk.Button(win, text='MS', width=5, command=memory_save, font=("Arial", 14), borderwidth=2)
btn_ms.grid(row=7, column=2,sticky=tk.NSEW)
btn_mr = tk.Button(win, text='MR', width=5, command=memory_call, font=('Arial', 14), borderwidth=2)
btn_mr.grid(row=7, column=3,sticky=tk.NSEW)
btn_mc = tk.Button(win, text='MC', width=5, command=memory_clear, font=('Arial', 14), borderwidth=2)
btn_mc.grid(row=7,column=1,sticky=tk.NSEW)

#math library
btn_sin = tk.Button(win, text='sin', width=8, font=('Arial', 14), command=calc_sin)
btn_sin.grid(column=1, row=8,sticky=tk.NSEW)

btn_cos = tk.Button(win, text='cos', width=8, font=('Arial', 14), command=calc_cos)
btn_cos.grid(column=2, row=8,sticky=tk.NSEW)

btn_tan = tk.Button(win, text='tan',width=8, font=('Arial', 14), command=calc_tan)
btn_tan.grid(column=3, row=8,sticky=tk.NSEW)

# img_e = tk.PhotoImage(file='image/e num.PNG')
# btn_exp = tk.Label(win,image=img_e,relief='ridge',bd=4,width=90,height=32)
# btn_exp.grid(column=4, row=8)


btn_exp = tk.Button(win, text='e^x', width=8, font=('Arial', 14), command=calc_tan)
btn_exp.grid(column=4, row=8,sticky=tk.NSEW)

btn_power = tk.Button(win,text='x^y',width=8, font=('Arial', 14), command=lambda :add_to_calculation('**'))
btn_power.grid(row=7,column=4,sticky=tk.NSEW)

# btn_exp.bind('<Button-1>',lambda event : calc_exp())

win.mainloop()

