from tkinter import *
from PIL import ImageTk
import pyodbc
root=Tk()
root.geometry('500x500')
root.resizable(False, False)
btn=ImageTk.PhotoImage(file='C:/Project1/arr1.png')
btn0=ImageTk.PhotoImage(file='C:/Project1/arr2.png')
var=IntVar()
li=[]
count=0
countc=0
def login_screen():
    fr=Frame(root, bg='white')
    lab1=Label(fr, text='Eneter Details', bg='white')
    lab1.pack(anchor='c', pady=20)
    lab2=Label(fr, text='Enter Full Name', bg='white')
    lab2.place(x=100, y=80)
    entr1=Entry(fr)
    entr1.place(x=250, y=80)
    lab3=Label(fr, text='Enter Fathers Name', bg='white')
    lab3.place(x=100, y=110)
    entr2=Entry(fr)
    entr2.place(x=250, y=110)
    lab4=Label(fr, text='Enter Mothers Name', bg='white')
    lab4.place(x=100, y=140)
    entr3=Entry(fr)
    entr3.place(x=250, y=140)
    lab5=Label(fr, text='Enter Class', bg='white')
    lab5.place(x=100, y=170)
    entr4=Entry(fr)
    entr4.place(x=250, y=170)
    but=Button(fr, text='Continue', command=lambda: question_print(1, entr1.get(), entr2.get(), entr3.get(), entr4.get()))
    but.place(x=200, y=420, height=50, width=100)
    fr.place(x=0, y=0, height=500, width=500)
def print_result(name, fname, mname, clas):
    global countc, count
    fr=Frame(root, bg='white')
    lab0=Label(fr, text='Result', bg='white')
    lab0.pack(anchor='c', pady=20)
    lab1=Label(fr, text='User Name', bg='white')
    lab1.place(x=100, y=80)
    lab2=Label(fr, text=name, bg='white')
    lab2.place(x=250, y=80)
    lab3=Label(fr, text='Fathers Name', bg='white')
    lab3.place(x=100, y=110)
    lab4=Label(fr, text=fname, bg='white')
    lab4.place(x=250, y=110)
    lab5=Label(fr, text='Mothers Name', bg='white')
    lab5.place(x=100, y=140)
    lab6=Label(fr, text=mname, bg='white')
    lab6.place(x=250, y=140)
    lab7=Label(fr, text='Class', bg='white')
    lab7.place(x=100, y=170)
    lab8=Label(fr, text=clas, bg='white')
    lab8.place(x=250, y=170)
    lab9=Label(fr, text='Question Attempted', bg='white')
    lab9.place(x=100, y=200)
    lab10=Label(fr, text=str(count), bg='white')
    lab10.place(x=250, y=200)
    lab11=Label(fr, text='Correct Answers', bg='white')
    lab11.place(x=100, y=230)
    lab12=Label(fr, text=str(countc), bg='white')
    lab12.place(x=250, y=230)
    lab13=Label(fr, text='Wrong Answers', bg='white')
    lab13.place(x=100, y=260)
    lab14=Label(fr, text=str(count-countc), bg='white')
    lab14.place(x=250, y=260)
    fr.place(x=0, y=0, height=500, width=500)
def check_ans(i, fr):
    global count, countc, var, li
    value=var.get()
    if i not in li:
        count=count+1
    conn=pyodbc.connect('Driver={SQL Server};' 'Server=LAPTOP-HNP465U9;' 'Database=Project_DB;' 'Trusted_Connection=yes;')
    cur=conn.cursor()
    cur.execute(f'''SELECT correct_ans
                    FROM questions
                    WHERE question_no={i};''')
    for row in cur:
        x=row
    if value==0:
        lab=Label(fr, text='Nothing Selected.', bg='white')
        lab.place(x=200, y=250)
    elif x[0]==value:
        if i not in li:
            countc=countc+1
        lab=Label(fr, text='_Correct Answer_', bg='white')
        lab.place(x=200, y=250)
    else:
        lab=Label(fr, text='Incorrect Answer.', bg='white')
        lab.place(x=200, y=250)
    li.append(i)
def question_print(i, name, fname, mname, clas):
    global var, btn, btn0
    fr=Frame(root, bg='white')
    conn=pyodbc.connect('Driver={SQL Server};' 'Server=LAPTOP-HNP465U9;' 'Database=Project_DB;' 'Trusted_Connection=yes;')
    cur=conn.cursor()
    cur.execute(f'''SELECT question
                    FROM questions
                    WHERE question_no={i};''')
    for row in cur:
        lab1=Label(fr, text=row[0], bg='white')
        lab1.pack(anchor='c', pady=20)
    cur.execute(f'''SELECT option_1, option_2, option_3, option_4
                    FROM questions
                    WHERE question_no={i};''')
    for row in cur:
        j=0
        for line in row:
            opt=Radiobutton(fr, text=line, variable=var, value=j+1, bg='white')
            opt.pack(anchor='c', pady=5)
            j=j+1
    if i>=2:
        prev=Button(fr, image=btn, bd=0, command=lambda: question_print(i-1, name, fname, mname, clas))
        prev.place(x=50, y=410, height=70, width=85)
    ca=Button(fr, text='Check\nAnswer', command=lambda: check_ans(i, fr))
    ca.place(x=200, y=350, height=50, width=100)
    pr=Button(fr, text='Print\nResult', command=lambda: print_result(name, fname, mname, clas))
    pr.place(x=145, y=420, height=50, width=100)
    qu=Button(fr, text='Exit', command=quit)
    qu.place(x=255, y=420, height=50, width=100)
    if i<100:
        nex=Button(fr, image=btn0, bd=0, command=lambda: question_print(i+1, name, fname, mname, clas))
        nex.place(x=365, y=410, height=70, width=85)
    fr.place(x=0, y=0, height=500, width=500)
def quit():
    root.destroy()
login_screen()
root.mainloop()
