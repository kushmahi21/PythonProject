from tkinter import *
import sqlite3
#*******************DELETE DATA PAGE********************

#after clicking Delete Button
def DeleteRecord():
    deletename = deledata.get()
    con = sqlite3.connect('library.db')
    c = con.cursor()
    deletebook = "DELETE FROM AddBook WHERE BookName='"+ deletename +"'"
    c.execute(deletebook)
    Label(win5, text="Delete Sucessful").pack()
    deledata.delete(0, END)
    con.commit()
    con.close()

#after clicking Delete
def deletere():
    global win5
    win5 = Toplevel(screen)
    win5.title("Delete Record")
    win5.geometry("400x300")

    # Delete Data
    lb1 = Label(win5, text="Delete Data:", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    global deledata
    deledata = Entry(win5)
    deledata.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Delete Button
    DeleteBtn = Button(win5, text="Delete", bg='#d1ccc0', fg='black', command=DeleteRecord)
    DeleteBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(win5, text="Quit", bg='#f7f1e3', fg='black', command=win5.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)


#************UPDATE DATA PAGE**********************
#after clicking update button
def updatedata():
    old = oldup.get()
    new = newup.get()
    con = sqlite3.connect('library.db')
    c = con.cursor()
    upbook = "update AddBook set BookName='" + new + "' where BookName='" + old + "'"
    c.execute(upbook)
    Label(win4,text="Sucessful Update").pack()
    oldup.delete(0,END)
    newup.delete(0,END)
    con.commit()
    con.close()

#after clicking update
def update():
    global win4
    win4 = Toplevel(screen)
    win4.title("Update ")
    win4.geometry("400x300")

    # Old Update
    lb1 = Label(win4, text="oldUpdate:", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    global oldup
    oldup = Entry(win4)
    oldup.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # New Update
    lb2 = Label(win4, text="NewUpdate", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    global newup
    newup = Entry(win4)
    newup.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)



    # Update Button
    UpdateBtn = Button(win4, text="Update", bg='#d1ccc0', fg='black', command=updatedata)
    UpdateBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(win4, text="Quit", bg='#f7f1e3', fg='black', command=win4.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)


#******************VIEW Detail Page*************************
#after clicking viewdetail
def viewdetail():
    con = sqlite3.connect('library.db')
    c = con.cursor()
    c.execute(""" 
            select * from AddBook
    """)
    a = c.fetchall()
    for i in a:
        Label(win3, text=i[0]).pack()
        Label(win3, text=i[1]).pack()
        Label(win3, text=i[2]).pack()
        Label(win3, text="-----------------").pack()

    con.commit()

    con.close()

#after clicking view button
def viewbook():
    global win3
    win3 = Toplevel(screen)
    win3.title("ViewBook")
    win3.geometry("400x300")

    # Submit Button
    SubmitBtn = Button(win3, text="ViewDetail", bg='#d1ccc0', fg='black', command=viewdetail)
    SubmitBtn.pack()

    quitBtn = Button(win3, text="Quit", bg='#f7f1e3', fg='black', command=win3.destroy)
    quitBtn.pack()

#**************AddBook Page***************
#after clicking submit button
def bookreg():
    BI1 = bookInfo1.get()
    BI2 = bookInfo2.get()
    BI3 = bookInfo3.get()

    con = sqlite3.connect('library.db')
    c = con.cursor()

    c.execute("INSERT INTO AddBook VALUES (:boi1, :boi2, :boi3)",
              {
                  'boi1': BI1,
                  'boi2': BI2,
                  'boi3': BI3,
              })

    con.commit()
    con.close()

#after clicking the addbook
def addbook():
    global win2
    win2 = Toplevel(screen)
    win2.title("BOOK")
    win2.geometry("400x300")
    # Book ID
    lb1 = Label(win2, text="Book ID:", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    global bookInfo1
    bookInfo1 = Entry(win2)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Book Name
    lb2 = Label(win2, text="Book Name:", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    global bookInfo2
    bookInfo2 = Entry(win2)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(win2, text="Author:", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    global bookInfo3
    bookInfo3 = Entry(win2)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(win2, text="SUBMIT", bg='#d1ccc0', fg='black',command=bookreg)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(win2, text="Quit", bg='#f7f1e3', fg='black' ,command=win2.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

#***********************REGISTER PAGE**************************
def library():
    global win1
    win1 = Toplevel(screen)
    win1.title("Welcome To Library World")
    win1.geometry("400x300")

    con = sqlite3.connect('library.db')
    c = con.cursor()

    c.execute("select * from Student")
    det = c.fetchall()
    for v in det:
        Label(win1, text="FirstName: " + v[0]).pack()
        Label(win1, text="LastName: " + v[1]).pack()
        Label(win1, text="Class: " + v[2]).pack()
        Label(win1, text="Roll NO: " + v[3]).pack()
        Label(win1, text="Div: " + v[4]).pack()
        Label(win1, text="Contact No: " + str(v[5])).pack()
        Label(win1, text=".......................").pack()

    con.commit()
    con.close()


# after clicking submit button of register page
def stud_reg(caa=None):
    user_reg = uid_reg.get()
    password_reg = passw_reg.get()
    fs = f_reg.get()
    ls = l_reg.get()
    cl = caa_reg.get()
    rn = ro_reg.get()
    div = di_reg.get()
    cn = mo_reg.get()

    con = sqlite3.connect('library.db')
    c = con.cursor()

    c.execute("INSERT INTO Stu_Login VALUES (:id_reg, :pss_reg)",
              {
                  'id_reg': user_reg,
                  'pss_reg': password_reg,
              })

    c.execute("INSERT INTO Student VALUES (:f_nm, :l_nm, :cl, :rn, :div, :cn)",
              {
                  'f_nm': fs,
                  'l_nm': ls,
                  'cl': cl,
                  'rn': rn,
                  'div': div,
                  'cn': cn
              })

    Label(stu_reg, text="Sucessfully Register").pack()
    uid_reg.delete(0, END)
    passw_reg.delete(0, END)
    f_reg.delete(0, END)
    l_reg.delete(0, END)
    caa_reg.delete(0, END)
    ro_reg.delete(0, END)
    di_reg.delete(0, END)
    mo_reg.delete(0, END)
    con.commit()
    con.close()

# after clicking register button
def regi_func():
    global stu_reg
    stu_reg = Toplevel(lib_root)
    stu_reg.title("Register")
    stu_reg.geometry("500x500")
    t_reg = Label(stu_reg, text="Register", font=("Arial", 25))
    t_reg.place(x=250, y=40)

    # UserId lable and textbox
    u_reg = Label(stu_reg, text="User Id*", font=("Arial", 10))
    u_reg.place(x=150, y=100)

    global uid_reg
    uid_reg = Entry(stu_reg, width=30)
    uid_reg.place(x=210, y=100)

    # Password lable and textbox
    p_reg = Label(stu_reg, text="Password*", font=("Arial", 10))
    p_reg.place(x=150, y=120)

    global passw_reg
    passw_reg = Entry(stu_reg, width=30)
    passw_reg.place(x=220, y=120)

    # User First name lable and text
    fl_reg = Label(stu_reg, text="FirstName*", font=("Arial", 10))
    fl_reg.place(x=150, y=160)

    global f_reg
    f_reg = Entry(stu_reg, width=30)
    f_reg.place(x=220, y=160)

    # User Last name lable and text
    ll_reg = Label(stu_reg, text="LastName*", font=("Arial", 10))
    ll_reg.place(x=150, y=190)

    global l_reg
    l_reg = Entry(stu_reg, width=30)
    l_reg.place(x=220, y=190)

    # User Class lable and text
    clas_reg = Label(stu_reg, text="Class*", font=("Arial", 10))
    clas_reg.place(x=150, y=220)

    global caa_reg
    caa_reg = Entry(stu_reg, width=30)
    caa_reg.place(x=220, y=220)

    # User Roll No lable and text
    ron_reg = Label(stu_reg, text="Roll No*", font=("Arial", 10))
    ron_reg.place(x=150, y=250)

    global ro_reg
    ro_reg = Entry(stu_reg, width=30)
    ro_reg.place(x=220, y=250)

    # User Div lable and text
    dia_reg = Label(stu_reg, text="Div*", font=("Arial", 10))
    dia_reg.place(x=150, y=280)

    global di_reg
    di_reg = Entry(stu_reg, width=30)
    di_reg.place(x=220, y=280)

    # User Contact No lable and text
    mob_reg = Label(stu_reg, text="Contact No*", font=("Arial", 10))
    mob_reg.place(x=150, y=310)

    global mo_reg
    mo_reg = Entry(stu_reg, width=30)
    mo_reg.place(x=220, y=310)

    # Submit button
    global subm_reg
    subm_reg = Button(stu_reg, text="Submit", bg='blue', command=stud_reg)
    subm_reg.place(x=250, y=340)

#**********************Welcome To Library World(2nd Page)*************
def detail():
    global screen
    screen = Toplevel(lib_root)
    screen.geometry("550x400")
    screen.title("Welcome World Library")
    B = Button(screen, bg='red',text='Record', command=library)
    B.place(x=80,y=30, relwidth=0.25, relheight=0.08)
    B2 = Button(screen,bg='yellow', text='Add Book', command=addbook)
    B2.place(x=145, y=70, relwidth=0.25, relheight=0.08)
    B3 = Button(screen,bg='green', text='View Books', command=viewbook)
    B3.place(x=210, y=110, relwidth=0.25, relheight=0.08)
    B4 = Button(screen,bg='grey', text = 'Update', command=update)
    B4.place(x=275, y=150, relwidth=0.25, relheight=0.08)
    B5 = Button(screen,bg='white', text = 'Delete Record', command=deletere)
    B5.place(x=340, y=190, relwidth=0.25, relheight=0.08)

#************************Login Page********************
# After clicking submit button
def sub_func():
    global user, password
    user = uid.get()
    password = passw.get()
    con = sqlite3.connect('library.db')
    c = con.cursor()
    uid.delete(0, END)
    passw.delete(0, END)

    c.execute("""
            select * from Stu_Login
            """)
    a = c.fetchall()

    for row in a:
        if (user == row[0]):
            if (password == row[1]):
                detail()

    con.commit()
    con.close()

lib_root = Tk()
lib_root.title("LOGIN PAGE")
lib_root.geometry("744x434")
lib_root.minsize(300,100)
lib_root.maxsize(1200,988)

con = sqlite3.connect('library.db')

c = con.cursor()



#UserId lable and textbox
u_lb = Label(lib_root, text="Student Id*", font=("Arial", 10))
u_lb.place(x=160, y=100)

global uid
uid = Entry(lib_root, width=30)
uid.place(x = 260 , y=100)

#Password lable and textbox
p_lb = Label(lib_root, text="Password*", font=("Arial", 10))
p_lb.place(x=160, y=130)

global passw
passw = Entry(lib_root, width=30)
passw.place(x = 260 , y=130)

#Submit button
global subm
subm = Button(lib_root, text="Submit",width = 10, command = sub_func)
subm.place(x =260 , y = 170)

reg = Button(lib_root, text="Register",width = 10, command = regi_func)
reg.place(x=380 , y= 170)

con.commit()

con.close()



lib_root.mainloop()