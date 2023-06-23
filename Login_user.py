from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from gym_admin import GYM_Admin 
from gym_user import GYM_user
from reigster import Rigester
class Loginu:
    def __init__(self,root):
        self.root = root
        self.root.title("Login as user")
        self.root.geometry("1550x800+0+0")
        self.root.iconbitmap('pohots\Silvster gym.ico.ico')
        self.root.resizable(0,0)

        ####
        self.bg=ImageTk.PhotoImage(file=r"pohots\ganteli-trenazhernyy-zal.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)    
        
        frame=Frame(self.root,bg="black",bd=2,relief=RIDGE)
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"pohots\Sylvester_GYM.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(self.root,image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_start=Label(frame,text="WELCOME",font=("times new roman",20,"bold"),fg="#FFBA7B",bg="black")
        get_start.place(x=90,y=100)
        
        def focus_next_widget(event):
            event.widget.tk_focusNext().focus()
            return "break"
        
        def focus_prev_widget(event):
            event.widget.tk_focusPrev().focus()
            return "break"
        
        username=labl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="#FFBA7B",bg="black")
        username.place(x=40,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("arial",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        self.txtuser.bind("<Down>", focus_next_widget)
        
        password=labl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="#FFBA7B",bg="black")
        password.place(x=40,y=225)
        
        self.passw = ttk.Entry(frame, font=("arial", 15, "bold"), show='●')
        self.passw.place(x=40,y=250,width=230)
        self.passw.bind("<Up>", focus_prev_widget)
        #login button
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),fg="white",bg="red",bd=3,relief=RIDGE,activeforeground="white",activebackground="red",cursor="hand2",command=self.login)
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        def on_enter_key(event):
            loginbtn.invoke()
        
        root.bind("<Return>", on_enter_key)
        
        reigsterbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),fg="#FFBA7B",bg="black",bd=0,relief=RIDGE,activeforeground="red",activebackground="black",cursor="hand2",command=self.register)
        reigsterbtn.place(x=35,y=350,width=120,height=35)
        
        forgtpassbtn=Button(frame,text="Forget Passowrd",font=("times new roman",10,"bold"),fg="#FFBA7B",bg="black",bd=0,relief=RIDGE,activeforeground="red",activebackground="black",cursor="hand2",command=self.forget_pass)
        forgtpassbtn.place(x=29,y=375,width=120,height=35)
        
        
        #===========================hide and show btn================================
        
        def toggle_password_visibility():
            if self.passw.cget('show') == '●':
                self.passw.config(show='')
            else:
                self.passw.config(show='●')

        img2=Image.open(r"pohots\show-password.png")
        img2=img2.resize((25,30),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        leblimg2=Button(frame,image=self.photoimg2,bd=0,relief=RIDGE,bg="black",activebackground="black",command=toggle_password_visibility,cursor="hand2")
        leblimg2.place(x=280,y=250,width=25,height=30)
        
        
    def login(self):
        if self.txtuser.get()=="" or self.passw.get()=="":
            messagebox.showerror("Eror","all fields are required",parent=self.root)
            
        elif self.txtuser.get()=="admin"and self.passw.get()!="47200325":
            messagebox.showerror("Invalid","Password is invalid",parent=self.root)
            
        elif self.txtuser.get()!="admin" and self.passw.get()=="47200325":
            messagebox.showerror("Invalid","Username is invalid",parent=self.root)
            
        elif self.txtuser.get()=="admin" and self.passw.get()=="47200325":
            open_main=messagebox.askyesno("Yes/NO",'Accsess only Admin?',parent=self.root)
            if open_main>0:
                    self.admin() 
            else:
                if not open_main:
                    return    
        else:
            conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass=%s", (
                                                                    self.txtuser.get(),
                                                                    self.passw.get()
                                                                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Eror","Invaild user name and password",parent=self.root)
            else:
                    messagebox.showinfo("Succsess","Wellcom to Sylvester Gym System",parent=self.root)
                    self.user() 
                    
            conn.commit()
            conn.close()
    
    
    def reset_pass(self):
        if self.txt_security_A.get()=="":
            messagebox.showerror("Eror","please enter the answer",parent=self.root2)
        elif self.newpass.get()=="":
            messagebox.showerror("Eror","please enter the new password",parent=self.root2)
        else:
             conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
             my_cursor = conn.cursor()
             query = "select * from register where email=%s and securtyq=%s and securtya=%s"
             value = (self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get())
             my_cursor.execute(query, value)
             row=my_cursor.fetchone()
             if row ==None:
                messagebox.showerror("Eror","please enter the correct answer",parent=self.root2)
             else:
                query = ("update register set pass=%s where email=%s")
                value=(self.newpass.get(),self.txtuser.get())
                my_cursor.execute(query, value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo('info','your password is reset,please login with new password',parent=self.root2)
                self.root2.destroy()
                
    def forget_pass(self):
        if self.txtuser.get() =="":
            messagebox.showerror("Invalid","Please enter email to reset password",parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row ==None:
                messagebox.showerror("Invalid","please enter your vaild name",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title('Forget Password')
                self.root2.geometry("340x450+610+178")
                self.root2.attributes('-toolwindow',True)
                self.root2.configure(bg='black')
                lebl_title = Label(self.root2,text="Forget Password",font=("times new roman",18,"bold"),bg="black",fg="#FFBA7B",bd=4,relief=RIDGE)
                lebl_title.place(x=0,y=10,relwidth=1)
                
                security_Q=Label(self.root2,text="Verify Questions",font=("times new Roman",15,"bold"),bg="black",fg="#FFBA7B")
                security_Q.place(x=50,y=80)
        
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new Roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Your Birth Date","Your Best Friend Name","ID Number")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                
                security_A=Label(self.root2,text="Verify Answer",font=("times new Roman",15,"bold"),bg="black",fg="#FFBA7B")
                security_A.place(x=50,y=150)
        
                self.txt_security_A=ttk.Entry(self.root2,font=("times new Roman",15,"bold"))
                self.txt_security_A.place(x=50,y=180,width=250)
                
                newpasslbl=Label(self.root2,text="New Password",font=("times new Roman",15,"bold"),bg="black",fg="#FFBA7B")
                newpasslbl.place(x=50,y=220)
        
                self.newpass=ttk.Entry(self.root2,font=("times new Roman",15,"bold"))
                self.newpass.place(x=50,y=250,width=250)
                
                resetbtn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green",bd=3,relief=RIDGE,activeforeground="white",activebackground="red",cursor="hand2",command=self.reset_pass)
                resetbtn.place(x=115,y=300,width=120,height=35)
            
    def admin(self):
        self.root.destroy()
        root = Tk()
        app = GYM_Admin(root)
        root.mainloop()
    
    def user(self):
        self.root.destroy()
        root = Tk()
        app = GYM_user(root)
        root.mainloop()
        
    def register(self):
        if not hasattr(self, 'new_window') or not self.new_window.winfo_exists():
            self.new_window = Toplevel(self.root)
            self.app = Rigester(self.new_window)
        else:
            self.new_window.lift()
    
            
if __name__ == "__main__":
    root=Tk()
    obj = Loginu(root)
    root.mainloop()
  
        
