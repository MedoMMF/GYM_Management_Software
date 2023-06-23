from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
from tkcalendar import DateEntry
import random
from dateutil.relativedelta import relativedelta
import mysql.connector
from tkinter import filedialog
from tkinter import messagebox
import tkinter.messagebox as mb
class Emplyees:
    def __init__(self,root):
        self.root = root
        self.root.title("Emplyees")
        self.root.geometry("1295x550+230+200")
        self.root.resizable(0,0)
        self.root.attributes('-toolwindow',True)
        
        self.var_systemnum=IntVar()
        x=random.randint(1000,9999)
        self.var_systemnum.set(str(x))
        
        self.var_name= StringVar()
        self.var_phone= StringVar()
        self.var_phone.trace('w', self.validate_phone)
        self.var_job= StringVar()
        self.var_address= StringVar()
        self.var_age= StringVar()
        self.var_sdate= StringVar()
        self.var_email= StringVar()
        self.var_workday= StringVar()
        self.var_workhour= StringVar()
        self.var_salary= StringVar()
        
        

        #================================lable===============================
        lebl_title = Label(self.root,text="ADD EMPLOYEES",font=("times new roman",18,"bold"),bg="black",fg="#FFBA7B",bd=4,relief=RIDGE)
        lebl_title.place(x=0,y=0,width=1295,height=50)
        
        labelfram_left=LabelFrame(self.root,bd=2,relief=RIDGE,text='Add Details',padx=2,font=("arial",12,"bold"))      
        labelfram_left.place(x=5,y=50,width=425,height=490)
        
         #===========================label and Entry==========================
        labl_name=Label(labelfram_left, bd=2,text='Name',font=("arial",12,"bold"),padx=10,pady=6)
        labl_name.grid(row=0,column=0,sticky=W)
        
        entry_name=ttk.Entry(labelfram_left, width=29,font=("arial",12,"bold"),justify='center',textvariable=self.var_name)
        entry_name.grid(row=0,column=1)
        
        labl_phone=Label(labelfram_left, bd=2,text='Phone',font=("arial",12,"bold"),padx=10,pady=6)
        labl_phone.grid(row=1,column=0,sticky=W)
        
        def validate_phone_number(new_value):
            if len(new_value) > 11:
                return False
            return True
            
        entry_phone=ttk.Entry(labelfram_left, width=29,font=("arial",12,"bold"),justify='center',textvariable=self.var_phone, validate='key')
        entry_phone['validatecommand'] = (entry_phone.register(validate_phone_number), '%P')
        entry_phone.grid(row=1,column=1)
        
        
        
        labl_job=Label(labelfram_left, bd=2,text='Job Title',font=("arial",12,"bold"),padx=10,pady=6)
        labl_job.grid(row=2,column=0,sticky=W)
        
        combo_job=ttk.Combobox(labelfram_left,font=("arial",12,"bold"),width=27,justify='center',state="readonly",textvariable=self.var_job)
        combo_job["value"]=("Resption","Coach","Cleaning",)
        combo_job.current(0)
        combo_job.grid(row=2,column=1)
        
        labl_address=Label(labelfram_left, bd=2,text='Address',font=("arial",12,"bold"),padx=10,pady=6)
        labl_address.grid(row=3,column=0,sticky=W)
        
        entry_address=ttk.Entry(labelfram_left, width=29,font=("arial",12,"bold"),justify='center',textvariable=self.var_address)
        entry_address.grid(row=3,column=1)
        
        labl_age=Label(labelfram_left, bd=2,text='Age',font=("arial",12,"bold"),padx=10,pady=6)
        labl_age.grid(row=4,column=0,sticky=W)
        
        entry_age=ttk.Entry(labelfram_left, width=29,font=("arial",12,"bold"),justify='center',textvariable=self.var_age)
        entry_age.grid(row=4,column=1)
        
        labl_sdate=Label(labelfram_left, bd=2,text='Start Date',font=("arial",12,"bold"),padx=10,pady=6)
        labl_sdate.grid(row=5,column=0,sticky=W)
        
        self.entry_sdate = DateEntry(labelfram_left, textvariable=self.var_sdate,font=("arial", 12, "bold"), width=27, date_pattern="dd-mm-yyyy", state="readonly",justify='center')
        self.entry_sdate.grid(row=5,column=1,sticky=W)
        
        labl_nsystem=Label(labelfram_left, bd=2,text='ID',font=("arial",12,"bold"),padx=10,pady=6)
        labl_nsystem.grid(row=6,column=0,sticky=W)
        
        entry_nsystem=ttk.Entry(labelfram_left, width=29,textvariable=self.var_systemnum,font=("arial",12,"bold"),justify='center',state="readonly")
        entry_nsystem.grid(row=6,column=1)
        
        labl_email=Label(labelfram_left, bd=2,text='Email',font=("arial",12,"bold"),padx=10,pady=6)
        labl_email.grid(row=7,column=0,sticky=W)
        
        entry_email=ttk.Entry(labelfram_left, width=29,font=("arial",12,"bold"),justify='center',textvariable=self.var_email)
        entry_email.grid(row=7,column=1)
        
        labl_workday=Label(labelfram_left, bd=2,text='Work days:',font=("arial",12,"bold"),padx=10,pady=6)
        labl_workday.grid(row=8,column=0,sticky=W)
        
        entry_workday=ttk.Entry(labelfram_left, width=10,font=("arial",12,"bold"),justify='center', textvariable=self.var_workday)
        entry_workday.grid(row=8,column=1,sticky=W)
        
        labl_worktime=Label(labelfram_left, bd=2,text='Hours:',font=("arial",12,"bold"),padx=1,pady=1)
        labl_worktime.place(x=220,y=285)
        
        entry_worktime=ttk.Entry(labelfram_left, width=10,font=("arial",12,"bold"),justify='center',textvariable=self.var_workhour)
        entry_worktime.place(x=280,y=285)
        
        labl_salary=Label(labelfram_left, bd=2,text='Salary',font=("arial",12,"bold"),padx=10,pady=6)
        labl_salary.grid(row=9,column=0,sticky=W)
        
        entry_salay=ttk.Entry(labelfram_left, width=29,font=("arial",12,"bold"),justify='center',textvariable=self.var_salary)
        entry_salay.grid(row=9,column=1)
        
        
        #=================================bttns============================
        
        btn_frame=Frame(labelfram_left,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=420,width=412,height=40)
        
        btn_add=Button(btn_frame,text="Save",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",command=self.add_data)
        btn_add.grid(row=0,column=0,padx=1)
        
        btn_update=Button(btn_frame,text="Update",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",command=self.update_date)
        btn_update.grid(row=0,column=1,padx=1)
        
        btn_reset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",command=self.reset_date)
        btn_reset.grid(row=0,column=2,padx=1)
        
        btn_delete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="Red",width=10,cursor="hand2",command=self.delete_date)
        btn_delete.grid(row=0,column=3,padx=1)
   
        #=================================table frame search system==============================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View details and search data',padx=2,font=("arial",12,"bold"))      
        table_frame.place(x=430,y=50,width=860,height=490)
        
        labl_search=Label(table_frame, bd=2,text='Search by:',font=("arial",12,"bold"),bg='red',fg='white')
        labl_search.grid(row=0,column=0,sticky=W,padx=2)
        
        self.serch_var=StringVar()
        
        combo_search=ttk.Combobox(table_frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=20,state="readonly")
        combo_search["values"]=("Name","Job Title",'Date',"Phone","ID")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        
        def replace_entry_with_combobox():
            self.serch_var.set("Job Title")  # Clear the search input
            self.txt_search.set("Resption")  # Clear the search variable
            entry_search.grid_forget()  # Remove the entry widget
            combo_rentals.grid(row=0,column=2,padx=2)  # Add the combobox widget
        
        def restore_entry_widget():
            self.txt_search.set("")  # Clear the search variable
            combo_rentals.grid_forget()  # Remove the combobox widget
            entry_search.grid(row=0,column=2,padx=2)  # Add the entry widget
        
        combo_search.bind("<<ComboboxSelected>>", lambda event: replace_entry_with_combobox() if combo_search.get() == "Job Title" else restore_entry_widget())
        
        
        entry_search=ttk.Entry(table_frame,textvariable=self.txt_search, width=29,font=("arial",13,"bold"),justify='center')
        entry_search.grid(row=0,column=2,padx=2)
        
        combo_rentals=ttk.Combobox(table_frame,textvariable=self.txt_search,font=("arial",12,"bold"),width=28,state="readonly")
        combo_rentals["values"]=("Resption","Coach","Cleaning")
        combo_rentals.grid_forget()  # Hide the combobox initially
        
        btn_search=Button(table_frame,text="Search",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",command=self.search)
        btn_search.grid(row=0,column=3,padx=2)
        
        btn_showall=Button(table_frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",command=self.fetch_data)
        btn_showall.grid(row=0,column=4,padx=2)
         #======================show data table=======================================
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=420)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.rent_details_table=ttk.Treeview(details_table,columns=("id",'name',"phone","jop","address","age","sdate",'email','workday',"workhour",'salary'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.rent_details_table.xview)
        scroll_y.config(command=self.rent_details_table.yview)
        
        self.rent_details_table.heading("id",text="ID")
        self.rent_details_table.heading("name",text="Name")
        self.rent_details_table.heading("phone",text="Phone")
        self.rent_details_table.heading("jop",text="Jop Title")
        self.rent_details_table.heading("address",text="Adress")
        self.rent_details_table.heading("age",text="Age")
        self.rent_details_table.heading("sdate",text="Start Date")
        self.rent_details_table.heading("email",text="Email")
        self.rent_details_table.heading("workday",text="Work Days")
        self.rent_details_table.heading("workhour",text="Work Hours")
        self.rent_details_table.heading("salary",text="Salary")
        
        self.rent_details_table["show"]="headings"
        
        self.rent_details_table.column("id",width=100)
        self.rent_details_table.column("name",width=100)
        self.rent_details_table.column("phone",width=100)
        self.rent_details_table.column("jop",width=100)
        self.rent_details_table.column("address",width=100)
        self.rent_details_table.column("age",width=100)
        self.rent_details_table.column("sdate",width=100)
        

        self.rent_details_table.column("email",width=100)
        self.rent_details_table.column("workday",width=100)
        self.rent_details_table.column("workhour",width=100)
        self.rent_details_table.column("salary",width=100)
        
        self.rent_details_table.pack(fill=BOTH,expand=1)
        self.rent_details_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_name.get() =="":
            messagebox.showerror("Eror  : ("," اكمل ادخال البينات لو سمحت",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into emp values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_systemnum.get(),
                                                                            self.var_name.get(),
                                                                            self.var_phone.get(),
                                                                            self.var_job.get(),
                                                                            self.var_address.get(),
                                                                            self.var_age.get(),
                                                                            self.var_sdate.get(),
                                                                            self.var_email.get(),
                                                                            self.var_workday.get(),
                                                                            self.var_workhour.get(),
                                                                            self.var_salary.get(),
                
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Added Employee Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Worning!!",f"There is a problem :{str(es)}",parent=self.root)
                
                
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from emp")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.rent_details_table.delete(*self.rent_details_table.get_children())
            for i in rows:
                self.rent_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
        
        
    def delete_date(self):
        delete_date=messagebox.askyesno("GYM System","Are you sure to delete this employee?",parent=self.root)
        if delete_date>0:
            conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
            my_cursor = conn.cursor()
            query="delete from emp where id=%s"
            Value=(self.var_systemnum.get(),)
            my_cursor.execute(query,Value)
        else:
            if not delete_date:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def update_date(self):
        if self.var_name.get()=="" :
            messagebox.showerror("Eror  : (","Please enter all failds",parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
            my_cursor = conn.cursor()
            my_cursor.execute("update emp set name=%s,phone=%s,jop=%s,address=%s,age=%s,Sdate=%s,email=%s,workd=%s,workh=%s,salary=%s where id=%s",(
                                                                                        self.var_name.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_job.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_age.get(),
                                                                                        self.var_sdate.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_workday.get(),
                                                                                        self.var_workhour.get(),
                                                                                        self.var_salary.get(),
                                                                                        self.var_systemnum.get()
                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update Success","Updated Successfully",parent=self.root)
    
    
            
    def get_cuersor(self,event=""):
        cusrsor_row=self.rent_details_table.focus()
        content=self.rent_details_table.item(cusrsor_row)
        row=content["values"]
        
        self.var_systemnum.set(row[0]),
        self.var_name.set(row[1]),
        self.var_phone.set(row[2]),
        self.var_job.set(row[3]),
        self.var_address.set(row[4]),
        self.var_age.set(row[5]),
        self.var_sdate.set(row[6]),
        self.var_email.set(row[7]),
        self.var_workday.set(row[8]),
        self.var_workhour.set(row[9]),
        self.var_salary.set(row[10]),
     
    def reset_date(self):
        self.var_name.set(""),
        self.var_phone.set(""),
        self.var_age.set(""),
        self.var_address.set(""),
        self.var_email.set(""),
        self.var_workday.set(""),
        self.var_workhour.set(""),
        self.var_salary.set(""),
        self.entry_sdate.set_date(None),
        x = random.randint(1000, 9999)
        self.var_systemnum.set(str(x))
    
    def search(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='password', database='gym')
        my_cursor = conn.cursor()
        if self.serch_var.get() == 'Name':
            my_cursor.execute("SELECT * FROM emp WHERE name LIKE %s", ('%' + self.txt_search.get() + '%',))
        elif self.serch_var.get() == 'Job Title':
            my_cursor.execute("SELECT * FROM emp WHERE jop LIKE %s", ('%' + self.txt_search.get() + '%',))
            
        elif self.serch_var.get() == 'Date':
            my_cursor.execute("SELECT * FROM emp WHERE sdate LIKE %s", ('%' + self.txt_search.get() + '%',))
            
        elif self.serch_var.get() == 'ID':
            my_cursor.execute("SELECT * FROM emp WHERE id LIKE %s", ('%' + self.txt_search.get() + '%',))
        else:
            my_cursor.execute("SELECT * FROM emp WHERE phone LIKE %s", ('%' + self.txt_search.get() + '%',))
        rows=my_cursor.fetchall()
        if len(rows) != 0:
            self.rent_details_table.delete(*self.rent_details_table.get_children())
            for i in rows:
                self.rent_details_table.insert("",END,values=i)
            conn.commit()
        else:
            mb.showwarning("Eror  :(", "Wrong search please try agin",parent=self.root)
        conn.close()    
    
    def validate_phone(self, *args):
        if not self.var_phone.get():
            return    
        if not self.var_phone.get().isdigit():
            messagebox.showerror("خطاء في الادخال", "ادخل ارقام فقط",parent=self.root)

            self.var_phone.set("")
    
if __name__ == "__main__":
    root=Tk()
    obj = Emplyees(root)
    root.mainloop()