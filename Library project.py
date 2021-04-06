import tkinter
import sqlite3
from tkinter import messagebox as mb

root = tkinter.Tk()
root.title("Sign In")
root.geometry("1200x800")
root.resizable()
root.configure(background = "cyan")

txt = None
txt2 = None
regwindow =None

txt21 = None
txt22 = None
txt23 = None
txt24 = None
txt25 = None
student = None
add = None
txt42=None
txt43=None
txt44=None
txt52 = None
txt53 = None
user = None
var = None
password=None
a = 0
var = tkinter.IntVar()

def disp1():
    display=tkinter.Tk()
    display.title("DISPLAY")
    display.geometry("1200x800")
    display.resizable(0,0)
    display.configure(background = "cyan")
    
    lb1 = tkinter.Label(display, text = "BOOK_ID", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lb1.grid(row = 0, column = 0, padx=20,pady=20 )

    lb2 = tkinter.Label(display, text = "BOOK_NAME", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lb2.grid(row = 0, column = 1, padx=20,pady=20 )

    lb3 = tkinter.Label(display, text = "AUTHOR_NAME", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lb3.grid(row = 0, column = 2, padx=20,pady=20 )

    lb4 = tkinter.Label(display, text = "ISBN", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lb4.grid(row = 0, column = 3, padx=20,pady=20 )

    lb5 = tkinter.Label(display, text = "Status", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lb5.grid(row = 0, column = 4, padx=20,pady=20 )


    conn=sqlite3.connect("Library.db")
    conn.execute(''' create table if not exists Bookwindow( BookId text primary key, Bookname text, Author_Name text, ISBN_No text, Status text)''')
    c=1
    rows=conn.execute("Select * from Bookwindow") #all rows containing values 
    for row in rows:        
        lb12 = tkinter.Label(display, text = row[0], fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
        lb12.grid(row = c, column = 0, padx=20,pady=20 )
        lb13 = tkinter.Label(display, text = row[1], fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
        lb13.grid(row = c, column = 1, padx=20,pady=20 )
        lb14 = tkinter.Label(display, text = row[2], fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
        lb14.grid(row = c, column = 2, padx=20,pady=20 )
        lb15 = tkinter.Label(display, text = row[3], fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
        lb15.grid(row = c, column = 3, padx=20,pady=20 )
        lb16 = tkinter.Label(display, text = row[4], fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
        lb16.grid(row = c, column = 4, padx=20,pady=20 )
        c= c+1

def issue():
     global txt52
     issue = tkinter.Tk()
     issue.title("ISSUE")
     issue.geometry("1200x800")
     issue.resizable()
     issue.configure(background = "cyan")

     lbl51 = tkinter.Label(issue, text = "ISSUE", fg = "black", bg = "white", font = ("Arial", 30, "bold italic"), bd = 20, width = 10 )
     lbl51.grid(row = 0, column = 0, columnspan = 2, padx = 500, pady = 50)

     lbl52 = tkinter.Label(issue , text = "BOOK ID", fg = "black", bg = "white", font = ("Arial", 30, "bold"), bd = 10)
     lbl52.grid(row = 1, column = 0, pady = 50)

     txt52 = tkinter.Entry(issue, fg = "black", font = ("Arial", 20, "bold"), bd = 10)
     txt52.grid(row = 1, column = 1 )

     btn53 = tkinter.Button(issue, text = "SUBMIT",fg = "black", bg = "white", font = ("Arial",20,"bold"), command = issue2)
     btn53.grid(row = 5,column = 0, columnspan = 2, padx = 200, pady = 20)

def return1():
    global txt53
    ret = tkinter.Tk()
    ret.title("RETURN")
    ret.geometry("1200x800")
    ret.resizable()
    ret.configure(background = "cyan")

    lbl51 = tkinter.Label(ret, text = "RETURN", fg = "black", bg = "white", font = ("Arial", 30, "bold italic"), bd = 20, width = 10 )
    lbl51.grid(row = 0, column = 0, columnspan = 2, padx = 500, pady = 50)

    lbl52 = tkinter.Label(ret, text = "BOOK ID", fg = "black", bg = "white", font = ("Arial", 30, "bold"), bd = 10)
    lbl52.grid(row = 1, column = 0, pady = 50)

    txt53 = tkinter.Entry(ret, fg = "black", font = ("Arial", 20, "bold"), bd = 10)
    txt53.grid(row = 1, column = 1 )

    btn53 = tkinter.Button(ret, text = "SUBMIT",fg = "black", bg = "white", font = ("Arial",20,"bold"), command  = return2)
    btn53.grid(row = 5,column = 0, columnspan = 2, padx = 200, pady = 20)

    

def upd2():
     global txt42
     global txt43
     global txt44
    
     conn=sqlite3.connect("Library.db")
     conn.execute(''' create table if not exists Bookwindow( BookId text primary key, Bookname text, Author_Name text, ISBN_No text, Status text)''')
     BOOK_ID= txt42.get()        
     BOOK_NAME=txt43.get()
     AUTHOR_NAME =txt44.get()



     row=[(BOOK_ID, BOOK_NAME, AUTHOR_NAME)]
     conn.execute("update Bookwindow set Bookname='"+BOOK_NAME+"',Author_Name='" +AUTHOR_NAME+"' where BookId='"+BOOK_ID+"'")
     conn.commit()
     if conn.total_changes>0:
         mb.showinfo("Success! "," Information updated successfully!!")


def upd1():
    global txt42
    global txt43
    global txt44
    update = tkinter.Tk()
    update.title("Sign In")
    update.geometry("1200x800")
    update.resizable()
    update.configure(background = "cyan")

    lbl41 = tkinter.Label(update , text = "UPDATE", fg = "black", bg = "white", font = ("Arial", 30, "bold italic"), bd = 10 )
    lbl41.grid(row = 0, column = 0, columnspan = 2, pady = 50)

    lbl42 = tkinter.Label(update , text = "BOOK_ID", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lbl42.grid(row = 1, column = 0, padx=30,pady=30 )

    txt42 = tkinter.Entry(update , fg = "navy", font = ("Arial", 20, "bold"),bd = 10)
    txt42.grid(row = 1, column = 1, padx = 30)

    lbl43 = tkinter.Label(update , text = "BOOK_NAME", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lbl43.grid(row = 2, column = 0, padx=30,pady=30 )

    txt43 = tkinter.Entry(update , fg = "navy", font = ("Arial", 20, "bold"),bd = 10)
    txt43.grid(row = 2, column = 1, padx = 30)

    lbl44 = tkinter.Label(update , text = "AUTHOR_NAME", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lbl44.grid(row = 3, column = 0, padx=30,pady=30 )

    txt44 = tkinter.Entry(update , fg = "navy", font = ("Arial", 20, "bold"),bd = 10)
    txt44.grid(row = 3, column = 1, padx = 30)

    btn45 = tkinter.Button(update , text = "UPDATE",fg = "black", bg = "white", font = ("Arial",20,"bold"),command= upd2)
    btn45.grid(row = 4,column = 0, columnspan = 2, padx = 200, pady = 50)

def issue2():
     global txt52
     conn=sqlite3.connect("Library.db")
     conn.execute(''' create table if not exists Bookwindow( BookId text primary key, Bookname text, Author_Name text, ISBN_No text, Status text)''')
     BOOK_ID = txt52.get()
           
     row=[(BOOK_ID)]
     conn.execute("update Bookwindow set Status = 'Not Available' where BookId='"+BOOK_ID+"'")
     conn.commit()

     if conn.total_changes>0:
         mb.showinfo("Success! "," Issued!!")

def return2():
     global txt53
     conn=sqlite3.connect("Library.db")
     conn.execute(''' create table if not exists Bookwindow( BookId text primary key, Bookname text, Author_Name text, ISBN_No text, Status text)''')

     BOOK_ID = txt53.get()        

     row=[(BOOK_ID)]
     conn.execute("update Bookwindow set Status = 'Available' where BookId='"+BOOK_ID+"'")
     conn.commit()

     if conn.total_changes>0:
         mb.showinfo("Success!","Returned")
     
def add2():
    global txt21
    global txt22
    global txt23
    global txt24
    global txt25
    conn = sqlite3.connect("library.db")
    conn.execute(''' Create table if not exists BookWindow(BOOK_ID text primary key, BOOK_NAME text, AUTHOR_NAME text, ISBN_No text, Status text)''')
    BOOK_ID = txt21.get()
    BOOK_NAME = txt22.get()
    AUTHOR_NAME = txt23.get()
    ISBN_No = txt24.get()
    Status = txt25.get()
    
    row1 = [(BOOK_ID, BOOK_NAME, AUTHOR_NAME, ISBN_No, Status)]
    conn.executemany("Insert into BookWindow values (?,?,?,?,?)",row1)
    conn.commit()
    if conn.total_changes > 0:
        mb.showinfo("Success! "," You have added successfully ")
##        Bookwindow.withdraw()
##        root.deiconify()

def disp():
    view=tkinter.Toplevel()
    view.title("DISPLAY")
    view.geometry("1200x800")
    view.resizable(0,0)
    view.configure(background = "cyan")
    
    lbl7 = tkinter.Label(view, text = "BOOK_ID", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lbl7.grid(row = 0, column = 0, padx=20,pady=20 )

    lbl8 = tkinter.Label(view, text = "BOOK_NAME", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lbl8.grid(row = 0, column = 1, padx=20,pady=20 )

    lbl9 = tkinter.Label(view, text = "AUTHOR_NAME", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lbl9.grid(row = 0, column = 2, padx=20,pady=20 )

    lbl10 = tkinter.Label(view, text = "ISBN", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lbl10.grid(row = 0, column = 3, padx=20,pady=20 )

    lbl11 = tkinter.Label(view, text = "Status", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
    lbl11.grid(row = 0, column = 4, padx=20,pady=20 )


    conn=sqlite3.connect("Library.db")
    conn.execute(''' create table if not exists Bookwindow( BookId text primary key, Bookname text, Author_Name text, ISBN_No text, Status text)''')
    c=1
    rows=conn.execute("Select * from Bookwindow")
    for row in rows:        
        lbl12 = tkinter.Label(view, text = row[0], fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
        lbl12.grid(row = c, column = 0, padx=20,pady=20 )
        lbl13 = tkinter.Label(view, text = row[1], fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
        lbl13.grid(row = c, column = 1, padx=20,pady=20 )
        lbl14 = tkinter.Label(view, text = row[2], fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
        lbl14.grid(row = c, column = 2, padx=20,pady=20 )
        lbl15 = tkinter.Label(view, text = row[3], fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
        lbl15.grid(row = c, column = 3, padx=20,pady=20 )
        lbl16 = tkinter.Label(view, text = row[4], fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
        lbl16.grid(row = c, column = 4, padx=20,pady=20 )
        c= c+1
        
def add1():
          global txt21
          global txt22
          global txt23
          global txt24
          global txt25
             
          add=tkinter.Toplevel()
          add.title("ADD")
          add.geometry("1200x800")
          add.resizable(0,0)
          add.configure(background = "cyan")

          lbl21 = tkinter.Label(add, text = "BOOK_ID", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
          lbl21.grid(row = 0, column = 0, padx=30,pady=30 )

          txt21 = tkinter.Entry(add, fg = "navy", font = ("Arial", 20, "bold"),bd = 10)
          txt21.grid(row = 0, column = 1, padx = 30)

          lbl22 = tkinter.Label(add, text = "BOOK_NAME", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
          lbl22.grid(row = 1, column = 0, padx=30,pady=30 )

          txt22 = tkinter.Entry(add, fg = "navy", font = ("Arial", 20, "bold"),bd = 10)
          txt22.grid(row = 1, column = 1, padx = 30)

          lbl23 = tkinter.Label(add, text = "AUTHOR_NAME", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
          lbl23.grid(row = 2, column = 0, padx=30,pady=30 )

          txt23 = tkinter.Entry(add, fg = "navy", font = ("Arial", 20, "bold"),bd = 10)
          txt23.grid(row = 2, column = 1, padx = 30)

          lbl24 = tkinter.Label(add, text = "ISBN_NO.", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
          lbl24.grid(row = 3, column = 0, padx=30,pady=30 )

          txt24 = tkinter.Entry(add, fg = "navy", font = ("Arial", 20, "bold"),bd = 10)
          txt24.grid(row = 3, column = 1, padx = 30)

          lbl25 = tkinter.Label(add, text = "STATUS", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10 )
          lbl25.grid(row = 4, column = 0, padx=30,pady=30 )

          txt25 = tkinter.Entry(add, fg = "navy", font = ("Arial", 20, "bold"),bd = 10)
          txt25.grid(row = 4, column = 1, padx = 30)

          btn26 = tkinter.Button(add, text = "SUBMIT",fg = "black", bg = "white", font = ("Arial",40,"bold"), command = add2)
          btn26.grid(row = 5,column = 0, columnspan = 2, padx = 200)


def check():

    global user
    global password
    conn = sqlite3.connect("library.db")
    user = txt0.get()
    password = txt1.get()
    rows = conn.execute("Select * from reg where username = '"+user+"' and password = '"+password+"'")

    count = 0
    for row in rows:
        count +=1
    print(count)

    
    if user == "admin" and password=="1234":
            if a==2:
                
                home=tkinter.Toplevel()
                home.title("Home")
                home.geometry("1200x800")
                home.resizable(0,0)
                home.configure(background = "cyan")

                lbl = tkinter.Label(home, text = "ADMIN HOME PAGE",fg = "black", bg = "white", font = ("Arial",30,"bold italic"), bd = 20, width = 30)
                lbl.grid(row = 0, column = 0, columnspan = 3, pady = 50)

                btn10 = tkinter.Button(home, text = "VIEW",fg = "black", bg = "white", font = ("Arial",20,"bold"), command = disp)
                btn10.grid(row = 2,column = 0, padx = 200, pady = 50)

                btn20 = tkinter.Button(home, text = "ADD",fg = "black", bg = "white", font = ("Arial",20,"bold"), command = add1)
                btn20.grid(row = 2,column = 1)

                btn30 = tkinter.Button(home, text = "UPDATE",fg = "black", bg = "white", font = ("Arial",20,"bold"),command=upd1)
                btn30.grid(row = 2,column = 2, padx = 200)

    elif not user =="admin" and a==1 and count==1:
               student = tkinter.Tk()
               student.title("Student Home Page")
               student.geometry("1200x800")
               student.resizable()
               student.configure(background = "cyan")

                


               lbl41 = tkinter.Label(student, text = "STUDENT HOME PAGE", fg = "black", bg = "white", font = ("Arial", 30, "bold italic"),bd = 20, width = 30)
               lbl41.grid(row = 0, column = 1, columnspan = 2, padx = 200, pady = 50)

               lbl42 = tkinter.Label(student, text = "WELCOME " +user+"!", fg = "black", bg = "white", font = ("Arial", 30, "bold italic"),bd = 20, width = 30)
               lbl42.grid(row = 1, column = 0, columnspan = 2, padx = 200, pady = 50)               

               btn41 = tkinter.Button(student, text = "VIEW",fg = "black", bg = "white", font = ("Arial",20,"bold"),command = disp1)
               btn41.grid(row = 3,column = 1, columnspan = 2, padx = 200, pady = 20)

               btn42 = tkinter.Button(student, text = "ISSUE",fg = "black", bg = "white", font = ("Arial",20,"bold"), command = issue)
               btn42.grid(row = 4,column = 1, columnspan = 2, padx = 200, pady = 20)

               btn43 = tkinter.Button(student, text = "RETURN",fg = "black", bg = "white", font = ("Arial",20,"bold"), command = return1)
               btn43.grid(row = 5,column = 1, columnspan = 2, padx = 200, pady = 20)

               
                             
           
    else:
        mb.showinfo("Error! "," Invalid user name or password ")
    

def val():
    global a
    global var
    a = var.get()
    print("a = ",a)
    
#-------------------SIGN IN FORM----------------

lbl = tkinter.Label(regwindow,text = "LIBRARY",fg = "black", bg = "white", font = ("Arial",40,"bold"))
lbl.grid(row = 0,column = 0, columnspan = 2, padx = 30, pady = 20)

lbl0 = tkinter.Label(root,text = "Username",fg = "navy", bg = "white", font = ("Arial",20,"bold"),bd = 10)
lbl0.grid(row = 1,column = 0, padx = 40, pady = 40)

txt0 = tkinter.Entry(root, fg = "navy", font = ("Arial", 20, "bold"),bd = 10)
txt0.grid(row = 1, column = 1 )

lbl1 = tkinter.Label(root,text = "Password",fg = "navy", bg = "white", font = ("Arial",20,"bold"), bd = 10)
lbl1.grid(row = 2,column = 0, padx = 40, pady = 40)

txt1 = tkinter.Entry(root, show = '*', fg = "navy", font = ("Arial", 20, "bold"),bd = 10)
txt1.grid(row = 2, column = 1, padx = 40)

lbl1 = tkinter.Label(root,text = "User Type",fg = "navy", bg = "white", font = ("Arial",20,"bold"), bd = 10)
lbl1.grid(row = 3,column = 0, padx = 40, pady = 40)

rd0 = tkinter.Radiobutton(root, text = "Student", variable = var, value = 1, command = val)
rd0.grid(row = 3, column = 1, columnspan = 2)

rd1 = tkinter.Radiobutton(root, text = "Admin", variable = var, value = 2, command = val)
rd1.grid(row = 3, column = 2, columnspan = 2)

btn0 = tkinter.Button(root, text = "SIGN IN", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10, command = check)
btn0.grid(row = 4, column = 0, columnspan = 2 )


def save():
    global txt
    global txt2
    global regwindow
    conn = sqlite3.connect("library.db")
    conn.execute(''' Create table if not exists reg(username text primary key, password text)''')
    user = txt.get()
    password = txt2.get()

    row = [(user, password)]
    conn.executemany("Insert into reg values (?,?)",row)
    conn.commit()
    if conn.total_changes > 0:
        mb.showinfo("Success! "," You have registered successfully ")
        regwindow.withdraw()
        root.deiconify()

def reg():
    global txt
    global txt2
    global regwindow
    
    root.withdraw()
    
    regwindow = tkinter.Tk()
    regwindow.title("Sign Up")
    regwindow.geometry("1200x800")
    regwindow.resizable(0,0)
    regwindow.configure(background = "Light Blue")
    
    lbl = tkinter.Label(regwindow,text = "REGISTRATION",fg = "black", bg = "white", font = ("Arial",40,"bold"))
    lbl.grid(row = 0,column = 0, columnspan = 2, padx = 300, pady = 20)

    lbl = tkinter.Label(regwindow,text = "First Name",fg = "black", bg = "white", font = ("Arial",20,"bold"))
    lbl.grid(row = 1,column = 0, padx = 200, pady = 20)

    txt = tkinter.Entry(regwindow, fg = "black", font = ("Arial", 20, "bold"))
    txt.grid(row = 1, column = 1 )

    lbl = tkinter.Label(regwindow,text = "Last  Name",fg = "black", bg = "white", font = ("Arial",20,"bold"))
    lbl.grid(row = 2,column = 0, pady = 20)

    txt = tkinter.Entry(regwindow, fg = "black", font = ("Arial", 20, "bold"))
    txt.grid(row = 2, column = 1)

    lbl = tkinter.Label(regwindow,text = "Regn No.",fg = "black", bg = "white", font = ("Arial",20,"bold"))
    lbl.grid(row = 3,column = 0, pady = 20)

    txt = tkinter.Entry(regwindow, fg = "black", font = ("Arial", 20, "bold"))
    txt.grid(row = 3, column = 1)

    lbl = tkinter.Label(regwindow,text = "Email Id",fg = "black", bg = "white", font = ("Arial",20,"bold"))
    lbl.grid(row = 4,column = 0, pady = 20)

    txt = tkinter.Entry(regwindow, fg = "black", font = ("Arial", 20, "bold"))
    txt.grid(row = 4, column = 1)

    lbl = tkinter.Label(regwindow,text = "User  Name",fg = "black", bg = "white", font = ("Arial",20,"bold"))
    lbl.grid(row = 5,column = 0, pady = 20)

    txt = tkinter.Entry(regwindow, fg = "black", font = ("Arial", 20, "bold"))
    txt.grid(row = 5, column = 1)

    lbl1 = tkinter.Label(regwindow,text = " Password ",fg = "black", bg = "white", font = ("Arial",20,"bold"))
    lbl1.grid(row = 6,column = 0, pady = 20)

    txt2 = tkinter.Entry(regwindow, fg = "black", font = ("Arial", 20, "bold"))
    txt2.grid(row = 6, column = 1)

    txt2 = tkinter.Entry(regwindow, show = '*', fg = "navy", font = ("Arial", 20, "bold"),bd = 10)
    txt2.grid(row = 6, column = 1, padx = 40)

    btn = tkinter.Button(regwindow, text = "SIGN UP", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10, command = save)
    btn.grid(row = 7, column = 0, columnspan = 2, pady = 50 )

    
btn1 = tkinter.Button(root, text = "New user...? , click to SIGN UP", fg = "black", bg = "white", font = ("Arial", 20, "bold"), bd = 10, command = reg)
btn1.grid(row = 5, column = 0, columnspan = 2, pady = 50)
