
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmPasswordEntry.delete(0,END) 
    check.set(0)  

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmPasswordEntry.get()=='':
        messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED TO BE FILLED")
    elif passwordEntry.get()!= confirmPasswordEntry.get():
        messagebox.showerror("ERROR","Invalid Password")
    elif check.get()==0:
        messagebox.showerror("ERROR","Please Accept Terms & Condition")
    else:
        try:
            con = pymysql.connect(host = 'localhost', user='root',password='Root@1234')
            mycursor = con.cursor()
        except:
            messagebox.showerror("ERROR","DATABASE CONNECTIVITY ISSUE")
            return
        try:
            query = "CREATE DATABASE userdata"
            mycursor.execute(query)
            query = " use userdata"
            mycursor.execute(query)
            query = "create table data(id int auto_increment primary key not null, email varchar(60), username varchar(60),password varchar(60))"
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query = 'select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        
        row = mycursor.fetchone()
        if row !=None:
            messagebox.showerror("Exist","USERNAME ALREADY EXISTS")
        else:
            query = "insert into data(email,username,password) values(%s,%s,%s)"
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("SUCCESSFULLY","REGISTERATION IS SUCCESSFUL")
            clear()
            signup_window.destroy()
            import LoginPage
        
       
       
        
  
       
       
        
      

def login_page():
    signup_window.destroy()
    import LoginPage

signup_window = Tk()


signup_window.title("SIGN UP PAGE")
signup_window.resizable(False,False)

background = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(signup_window,image=background)
bgLabel.grid()

frame = Frame(signup_window, bg = 'white')
frame.place(x=554,y=100)

heading = Label(frame,text = 'CREATE AN ACCOUNT',font=('Aerial',18),bg="White",fg="firebrick")
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel = Label(frame,text='EMAIL ID',font=('Aerial',10,'bold'),bd=0,fg="firebrick",bg='white')
emailLabel.grid(row=1,column=0,sticky='w',padx=25)
emailEntry = Entry(frame,width=25,font=('Aerial',10,'bold'),bg='firebrick',fg='white')
emailEntry.grid(row = 2, column = 0, sticky='w',padx = 25)

usernameLabel = Label(frame,text='USER NAME',font=('Aerial',10,'bold'),bd=0,fg="firebrick",bg='white')
usernameLabel.grid(row=4,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry = Entry(frame,width=25,font=('Aerial',10,'bold'),bg='firebrick',fg='white')
usernameEntry.grid(row = 5, column = 0, sticky='w',padx = 25)

passwordLabel = Label(frame,text='PASSWORD',font=('Aerial',10,'bold'),bd=0,fg="firebrick",bg='white')
passwordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry = Entry(frame,width=25,font=('Aerial',10,'bold'),bg='firebrick',fg='white')
passwordEntry.grid(row = 8, column = 0, sticky='w',padx = 25)

confirmPasswordLabel = Label(frame,text='CONFIRM PASSWORD',font=('Aerial',10,'bold'),bd=0,fg="firebrick",bg='white')
confirmPasswordLabel.grid(row=10,column=0,sticky='w',padx=25,pady=(10,0))
confirmPasswordEntry = Entry(frame,width=25,font=('Aerial',10,'bold'),bg='firebrick',fg='white')
confirmPasswordEntry.grid(row = 11, column = 0, sticky='w',padx = 25)

check = IntVar()
termsandcondition = Checkbutton(frame,text='I agree to the Terms and Conditions',font=('Aerial',8,'bold'),fg="black",bg='white',activebackground='white',activeforeground='black',cursor='hand2',variable = check)
termsandcondition.grid(row= 12,column=0,padx=25,sticky='w',pady=(10,0))

signupButton = Button(frame, text = 'SIGN UP',font=('Aerial',16,'bold'),fg= 'white',bg='firebrick',activebackground='firebrick',activeforeground='white',cursor= 'hand2',bd = '0',width='15',command=connect_database)
signupButton.grid(row=13,column=0,padx=25,sticky='w',pady=(10,0))
signuptext = Label(frame,text='DONT HAVE AN ACCOUNT?',fg='firebrick',font=('Aerial',8,'bold '),bg='white')
signuptext.grid(row=14,column=0,padx=25,sticky='w',pady=(10,0))

loginButton = Button(frame, text = 'LOG IN',font=('Aerial',8,'bold underline'),fg= 'blue',bg='white',activebackground='white',activeforeground='blue', cursor= 'hand2',bd = '0',command=login_page)
loginButton.grid(row=14,column=0,padx=25,sticky='e',pady=(10,0))
signup_window.mainloop()