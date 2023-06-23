from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import time
from report import Report
from tkinter import messagebox
from members import Members
from rentals import Rentals
from emplyees import Emplyees

class GYM_Admin:
    def __init__(self,root):
        self.root = root
        self.root.title("Sylvester_GYM")
        self.root.geometry("1550x800+0+0")
        self.root.attributes('-fullscreen',True)
        
        #==============================First img==========================
        img1=Image.open(r"pohots\673a910a2e9a4f7c3c6580a15fff58cf7380a116.webp")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        leblimg1=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        leblimg1.place(x=0,y=0,width=1550,height=140)
        
        #===============================logo icon===========================
        img2=Image.open(r"pohots\Silvster gym.jpeg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        leblimg2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        leblimg2.place(x=0,y=0,width=230,height=140)
        
        #================================Title===============================
        lebl_title = Label(self.root,text="SYLVESTER_GYM_SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="#FFBA7B",bd=4,relief=RIDGE)
        lebl_title.place(x=0,y=140,width=1550,height=50)
        #============================Main Frame===============================
        main_frame = Frame(self.root,bd=4,relief=RIDGE,)
        main_frame.place(x=0,y=190,width=1550,height=620)
        #================================Welcom lbl============================
        labl_title = Label(main_frame,text="Welcome",font=("times new roman",20,"bold"),bg="black",fg="#FFBA7B",bd=4,relief=RIDGE)
        labl_title.place(x=0,y=0,width=230)
        #================================Buttens===============================
        bt_frame = Frame(main_frame,bd=4,relief=RIDGE,)
        bt_frame.place(x=0,y=35,width=228,height=193)

        member_btn = Button(bt_frame,text="Add Member",width=22,font=("times new roman",14,"bold"),bg="black",fg="#FFBA7B",bd=0,cursor="hand2",command=self.members)
        member_btn.grid(row=0,column=0,pady=1)
        
        emp_btn = Button(bt_frame,text="Employees",width=22,font=("times new roman",14,"bold"),bg="black",fg="#FFBA7B",bd=0,cursor="hand2",command=self.emp)
        emp_btn.grid(row=1,column=0,pady=1)
        
        
        rent_btn = Button(bt_frame,text="Rentals",width=22,font=("times new roman",14,"bold"),bg="black",fg="#FFBA7B",bd=0,cursor="hand2",command=self.rent)
        rent_btn.grid(row=2,column=0,pady=1)
        
        report_btn = Button(bt_frame,text="Reports",width=22,font=("times new roman",14,"bold"),bg="black",fg="#FFBA7B",bd=0,cursor="hand2",command=self.report)
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn = Button(bt_frame,text="Logout",width=22,font=("times new roman",14,"bold"),bg="black",fg="#FFBA7B",bd=0,cursor="hand2",command=self.iexit)
        logout_btn.grid(row=4,column=0,pady=1)
        #=============================background img===========================
        img3=Image.open(r"pohots\istockphoto-675179390-612x612.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        leblimg3=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        leblimg3.place(x=225,y=0,width=1310,height=590)
        
        img4=Image.open(r"pohots\Gym-weights.webp")
        img4=img4.resize((230,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        leblimg4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        leblimg4.place(x=0,y=223,width=230,height=190)
        
        img5=Image.open(r"pohots\Blog_Is-Gym-Air-Safe.jpeg")
        img5=img5.resize((230,230),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        leblimg5=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        leblimg5.place(x=0,y=400,width=230,height=200)
        
        img6=Image.open(r"pohots\WhatsApp Image 2023-03-07 at 5.24.33 AM.jpeg")
        img6=img6.resize((1550,100),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        leblimg6=Label(self.root,image=self.photoimg6,bd=4,relief=RIDGE)
        leblimg6.place(x=0,y=775,width=1550,height=100)
        
        #=============================clock===========================
        def clock():
            h = time.strftime("%I")
            m = time.strftime("%M")
            am_pm = time.strftime("%p")
            time_lable.config(text=h+":"+m+" "+am_pm)
            time_lable.after(1000, clock)


        time_lable = Label(self.root, bg='black',fg='#FFBA7B', text="", font=("times new roman",20,"bold"))
        time_lable.place(x=1300, y=145)
        clock()
        
        #================================================================
        
    def members(self):
        if not hasattr(self, 'new_window') or not self.new_window.winfo_exists():
            self.new_window = Toplevel(self.root)
            self.app = Members(self.new_window)
        else:
            self.new_window.lift()
        
            
    def report(self):
        if not hasattr(self, 'new_window') or not self.new_window.winfo_exists():
            self.new_window = Toplevel(self.root)
            self.app = Report(self.new_window)
        else:
            self.new_window.lift()

            
    def rent(self):
        if not hasattr(self, 'new_window') or not self.new_window.winfo_exists():
            self.new_window = Toplevel(self.root)
            self.app = Rentals(self.new_window)
        else:
            self.new_window.lift()
            
    def emp(self):
        if not hasattr(self, 'new_window') or not self.new_window.winfo_exists():
            self.new_window = Toplevel(self.root)
            self.app = Emplyees(self.new_window)
        else:
            self.new_window.lift()
    
    
    def iexit(self):
        iexit=messagebox.askyesno("Gym System","Are you sure you want to exit",parent=self.root)
        if iexit >0:
            self.root.deiconify()
            self.root.destroy() 
    
        


if __name__ == "__main__":
    root=Tk()
    obj = GYM_Admin(root)
    root.mainloop()
