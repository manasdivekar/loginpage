from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
#Functionality 

def forget_pass():
    
    def change_password():
        if userEntry.get()=='' or newPass_Entry.get()==''or confPass_Entry.get()=='':
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED",parent=window)
        elif newPass_Entry.get()!=confPass_Entry.get():
            messagebox.showerror("ERROR","WRONG INPUT OF PASSWORD",parent=window)
        else:
            con = pymysql.connect(host = 'localhost', user='root',password='Root@1234',database='userdata')
            mycursor = con.cursor()
            query = 'select * from data where username = %s'
            mycursor.execute(query,(userEntry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("ERROR","INCORRECT USERNAME",parent = window)
            else:
                query = "update data set password=%s where username =%s"
                mycursor.execute(query,(newPass_Entry.get(),userEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("SUCCESSFULLY","PASSWORD IS RESET SUCCESSFULLY",parent=window)
                window.destroy()
    window = Toplevel()
    window.title("CHANGE PASSWORD")
    bgPic = ImageTk.PhotoImage( file = "background.jpg")
    bglabel = Label(window, image=bgPic)
    bglabel.grid()
    
    heading_label = Label(window,text="RESET PASSWORD",font=('Aerial',20,'bold'),fg="firebrick",bd=0,bg="white")
    heading_label.place(x=480,y=60)
    
    userLabel = Label(window,text = "USERNAME",font=('Aerial',12,'bold'),fg="firebrick",bg="white")
    userLabel.place(x=470,y=130)
    userEntry = Label(window,font=('Aerial',12,'bold'),bd=0, width= 25,fg="firebrick",bg="white" )
    userEntry.place(x=470,y=160)
    Frame(window,width=200,height=2,bg='firebrick').place(x=470,y=180)
    newPassword = Label(window,text = "NEW PASSWORD",font=('Aerial',12,'bold'),fg="firebrick",bg="white" )
    newPassword.place(x=470,y=210)
    newPass_Entry = Label(window,font=('Aerial',12,'bold'),bd=0, width= 25,fg="firebrick",bg="white" )
    newPass_Entry.place(x=470,y=240)
    Frame(window,width=200,height=2,bg='firebrick').place(x=470,y=260)
    confPassword = Label(window,text = "CONFIRM PASSWORD",font=('Aerial',12,'bold'),fg="firebrick",bg="white" )
    confPassword.place(x=470,y=290)
    confPass_Entry = Label(window,font=('Aerial',12,'bold'),bd=0, width= 25,fg="firebrick",bg="white" )
    confPass_Entry.place(x=470,y=320)
    Frame(window,width=200,height=2,bg='firebrick').place(x=470,y=340)
    submitButton =Button(window,text = "SUBMIT",bd= 0,bg="firebrick",fg= 'white',font=('Aerial',12,'bold'),width = 19,cursor='hand2',activebackground='firebrick',activeforeground='white',command=change_password)
    submitButton.place(x=470,y=390)
    
    
    window.mainloop()
    
    
    




def on_enter(event):
    if usernameEntry.get()=='USER NAME':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='PASSWORD':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
    
def show():
      openeye.config(file='openeye.png')  
      passwordEntry.config(show='')
      eyeButton.config(command=hide)
def signup_page():
    login_window.destroy()
    import signup
    
def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror("ERROR","FIELDS ARE REQUIRED TO BE FILLED")
    else:
        try:
            
            con = pymysql.connect(host = 'localhost', user='root',password='Root@1234')
            mycursor = con.cursor()
        except:
            messagebox.showerror("ERROR","CONNECTION IS NOT ESTABLISHED")
            return 
        
        query = ("use userdata")
        mycursor.execute(query)
        query = ("select * from data where username = %s and password = %s")
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row = mycursor.fetchone()
        if row ==None:
            messagebox.showerror("ERROR","INVALID USERNAME OR PASSWORD")
        else:
            messagebox.showinfo("SUCCESS","LOGIN IS SUCCESSFUL")
        

    
#GUI
login_window = Tk()
login_window.resizable(0,0)  #Maximixe button stop functioning using this statement
login_window.title("Login Page")
bgImage = ImageTk.PhotoImage (file='bg.jpg')

bgLabel = Label(login_window,image=bgImage)
bgLabel.grid(row = 0,column=0)

heading = Label(login_window,text = 'USER LOGIN',font=('Aerial',24,'bold'),bg="White",fg="firebrick")
heading.place(x=605 , y= 120)

usernameEntry = Entry(login_window,width= 24,font=('Aerial',12,'bold'),bd=0,fg="firebrick")
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'USER NAME')

usernameEntry.bind("<FocusIn>",on_enter)

frame1 = Frame(login_window , width=250,height=2, bg="firebrick") 
frame1.place(x=580,y=222)

passwordEntry = Entry(login_window,width= 24,font=('Aerial',12,'bold'),bd=0,fg="firebrick")
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'PASSWORD')

passwordEntry.bind("<FocusIn>",password_enter)

frame1 = Frame(login_window , width=250,height=2, bg="firebrick") 
frame1.place(x=580,y=282)
openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image = openeye, bd=0, bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x= 800, y=253)

forgotpassword = Button(login_window, text = "FORGOT PASSWORD?",font=('Aerial',8,'bold'),fg="firebrick", bd=0, bg='white',activebackground='white',activeforeground='firebrick', cursor='hand2',command=forget_pass)
forgotpassword.place(x= 715, y=295)

loginButton = Button(login_window, text = 'LOGIN',font=('Aerial',15,'bold'),fg= 'white',bg='firebrick',activebackground='firebrick',activeforeground='white',cursor= 'hand2',bd = '0',width='19',command = login_user)
loginButton.place(x=578,y=350)

orlabel = Label(login_window,text='--------------OR-------------',fg='firebrick',font=('Aerial',15),bg='white')
orlabel.place(x='583',y= '400')

facebook_logo = PhotoImage(file='facebook.png')
google_logo = PhotoImage(file='google.png')
twitter_logo = PhotoImage(file='twitter.png')
fbLabel = Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=620,y=440)
twitterLabel = Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=680,y=440)
googleLabel = Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=740,y=440)

signup = Label(login_window,text='DONT HAVE AN ACCOUNT?',fg='firebrick',font=('Aerial',8,'bold '),bg='white')
signup.place(x='590',y= '490')

newaccountButton = Button(login_window, text = 'NEW ACCOUNT',font=('Aerial',8,'bold underline'),fg= 'blue',bg='white',background='white', cursor= 'hand2',bd = '0',command=signup_page)
newaccountButton.place(x=739,y=490)
login_window.mainloop()
