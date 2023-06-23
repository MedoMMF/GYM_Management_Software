from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
class Rigester:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.iconbitmap('pohots\Silvster gym.ico.ico')
        self.root.geometry("1600x900+0+0")
        ######
        self.var_fname=StringVar()
        self.var_l_name=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_Q=StringVar()
        self.var_security_A=StringVar()
        self.var_passw=StringVar()
        self.var_conf_passw=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"pohots\ganteli-trenazhernyy-zal.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        img3=Image.open(r"pohots\Silvster gym.png")
        img3=img3.resize((650,170),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        leblimg3=Label(root,image=self.photoimg3,bd=2,relief=RIDGE,bg="black")
        leblimg3.place(x=450,y=100,width=650,height=170)

        frame=Frame(self.root,bg="black",bd=2,relief=RIDGE)
        frame.place(x=450,y=200,width=650,height=500)

        regist_lbl=Label(frame,text="REGISTERATION ",font=("times new Roman",30,"bold"),fg="#FFBA7B",bg="black")
        regist_lbl.place(x=150,y=20)
        ###
        fname=Label(frame,text="First Name",font=("times new Roman",15,"bold"),bg="black",fg="#FFBA7B")
        fname.place(x=50,y=80)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new Roman",15,"bold"))
        self.txt_fname.place(x=50,y=110,width=250)
        ###
        l_name=Label(frame,text="Last Name",font=("times new Roman",15,"bold"),bg="black",fg="#FFBA7B")
        l_name.place(x=370,y=80)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_l_name,font=("times new Roman",15,"bold"))
        self.txt_lname.place(x=370,y=110,width=250)
        ###
        contact=Label(frame,text="Contact Number",font=("times new Roman",15,"bold"),bg="black",fg="#FFBA7B")
        contact.place(x=50,y=150)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new Roman",15,"bold"))
        self.txt_contact.place(x=50,y=180,width=250)
        ###
        email=Label(frame,text="Email",font=("times new Roman",15,"bold"),bg="black",fg="#FFBA7B")
        email.place(x=370,y=150)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new Roman",15,"bold"))
        self.txt_email.place(x=370,y=180,width=250)
        
        ###
        security_Q=Label(frame,text="Verify Questions",font=("times new Roman",15,"bold"),bg="black",fg="#FFBA7B")
        security_Q.place(x=50,y=220)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_security_Q,font=("times new Roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Your Birth Date","Your Best Friend Name","ID Number")
        self.combo_security_Q.place(x=50,y=250,width=250)
        self.combo_security_Q.current(0)
        
        ###
        security_A=Label(frame,text="Verify Answer",font=("times new Roman",15,"bold"),bg="black",fg="#FFBA7B")
        security_A.place(x=370,y=220)

        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_security_A,font=("times new Roman",15,"bold"))
        self.txt_security_A.place(x=370,y=250,width=250)

        ###
        passw=Label(frame,text="Password",font=("times new Roman",15,"bold"),bg="black",fg="#FFBA7B")
        passw.place(x=50,y=290)
        
        self.passw=ttk.Entry(frame,textvariable=self.var_passw,font=("times new Roman",15,"bold"), show='●')
        self.passw.place(x=50,y=320,width=250)
        
        # self.passw = ttk.Entry(frame, font=("arial", 15, "bold"), show='●')
        # self.passw.place(x=50,y=320,width=250)

        ###
        conf_passw=Label(frame,text="Confirm Password",font=("times new Roman",15,"bold"),bg="black",fg="#FFBA7B")
        conf_passw.place(x=370,y=290)

        self.txt_conf_passw=ttk.Entry(frame,textvariable=self.var_conf_passw,font=("times new Roman",15,"bold"), show='●')
        self.txt_conf_passw.place(x=370,y=320,width=250)

        ###
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new Roman",12,"bold"),bg="black",onvalue=1,offvalue=0,fg="red",activeforeground="black",activebackground="black")
        self.checkbtn.place(x=50,y=360)

        ###
        registerbtn=Button(frame,text="REGISTER",font=("times new roman",15,"bold"),fg="white",bg="red",bd=3,relief=RAISED,activeforeground="white",command=self.register_data)
        registerbtn.place(x=55,y=410,width=200)
        
        ###
        
        signinbtn=Button(frame,text="SIGN IN",font=("times new roman",15,"bold"),fg="white",bg="red",bd=3,relief=RAISED,activeforeground="white",command=self.login)
        signinbtn.place(x=370,y=410,width=200)
        
        def toggle_password_visibility():
            if self.passw.cget('show') == '●' and self.txt_conf_passw.cget('show') == '●' :
                self.passw.config(show='')
                self.txt_conf_passw.config(show='')
            else:
                self.passw.config(show='●')
                self.txt_conf_passw.config(show='●')

        img2=Image.open(r"pohots\show-password.png")
        img2=img2.resize((25,30),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        leblimg2=Button(frame,image=self.photoimg2,bd=0,relief=RIDGE,bg="black",activebackground="black",command=toggle_password_visibility,cursor="hand2")
        leblimg2.place(x=310,y=320,width=25,height=30)
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_Q.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_passw.get()!=self.var_conf_passw.get():
            messagebox.showerror("Error","password and confirm password must be the same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & conditions",parent=self.root)
        else:
         conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
         my_cursor = conn.cursor()
         query = "select * from register where email=%s"
         value = (self.var_email.get(),)
         my_cursor.execute(query, value)
         row = my_cursor.fetchone()
        if row != None:
            messagebox.showerror("Error", "User already exists. Please try another email.",parent=self.root)
        else:
            my_cursor.execute("insert into register values (%s,%s,%s,%s,%s,%s,%s)", (
                self.var_email.get(),
                self.var_fname.get(),
                self.var_l_name.get(),
                self.var_contact.get(),
                self.var_security_Q.get(),
                self.var_security_A.get(),
                self.var_passw.get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration successful.",parent=self.root)
    
    
    def login(self):
            self.root.destroy()

        
if __name__ == "__main__":
    root=Tk()
    obj = Rigester(root)
    root.mainloop()