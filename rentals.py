from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
from tkcalendar import DateEntry
import mysql.connector
from tkinter import messagebox
import tkinter.messagebox as mb
class Rentals:
    def __init__(self,root):
        self.root = root
        self.root.title("GYM Informations")
        self.root.geometry("1295x550+230+200")
        self.root.resizable(0,0)
        self.root.attributes('-toolwindow',True)
        
        #================================Variabels===========================
        self.var_systemnum=IntVar()
        x=random.randint(1000,9999)
        self.var_systemnum.set(str(x))
        
        self.var_rent = StringVar()
        self.var_date = StringVar()
        self.var_total = StringVar()
        
        
         #================================Title===============================
        lebl_title = Label(self.root,text="GYM Informations",font=("times new roman",18,"bold"),bg="black",fg="#FFBA7B",bd=4,relief=RIDGE)
        lebl_title.place(x=0,y=0,width=1295,height=50)
        
        #===========================label fram===============================
        labelfram_left=LabelFrame(self.root,bd=2,relief=RIDGE,text='Gym inf. Rentals',padx=2,font=("arial",12,"bold"))      
        labelfram_left.place(x=5,y=50,width=425,height=220)
            
        #===========================label and Entry==========================
        
        labl_rent=Label(labelfram_left, bd=2,text='Rentals',font=("arial",12,"bold"),padx=10,pady=6)
        labl_rent.grid(row=0,column=0,sticky=W)
        
        combo_rent=ttk.Combobox(labelfram_left,font=("arial",12,"bold"),width=27,justify='center',state="readonly",textvariable=self.var_rent)
        combo_rent["value"]=("Electricity rent","Water rent","Gym rent","Maintenance rent")
        combo_rent.current(0)
        combo_rent.grid(row=0,column=1)
        
        labl_date=Label(labelfram_left, bd=2,text='Date',font=("arial",12,"bold"),padx=10,pady=6)
        labl_date.grid(row=1,column=0,sticky=W)
        
        
        self.entry_date = DateEntry(labelfram_left, font=("arial", 12, "bold"), width=27, date_pattern="dd-mm-yyyy", state="readonly", justify='center', textvariable=self.var_date)
        self.entry_date.grid(row=1, column=1, sticky=W)
        
        
        labl_total=Label(labelfram_left, bd=2,text='Price',font=("arial",12,"bold"),padx=10,pady=6)
        labl_total.grid(row=2,column=0,sticky=W)
        
        entry_total=ttk.Entry(labelfram_left, width=29,font=("arial",12,"bold"),justify='center',textvariable=self.var_total)
        entry_total.grid(row=2,column=1)
        
        labl_nsystem=Label(labelfram_left, bd=2,text='Rent ID',font=("arial",12,"bold"),padx=10,pady=6)
        labl_nsystem.grid(row=3,column=0,sticky=W)
        
        entry_nsystem=ttk.Entry(labelfram_left, width=29,textvariable=self.var_systemnum,font=("arial",12,"bold"),justify='center',state="readonly")
        entry_nsystem.grid(row=3,column=1)
        #==================================btn=======================================
  
        btn_frame=Frame(labelfram_left,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=150,width=412,height=40)
        
        btn_add=Button(btn_frame,text="Add",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",command=self.add_data)
        btn_add.grid(row=0,column=0,padx=1)
        
        btn_update=Button(btn_frame,text="Update",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",command=self.update_date)
        btn_update.grid(row=0,column=1,padx=1)
        
        btn_reset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",command=self.reset_date)
        btn_reset.grid(row=0,column=2,padx=1)
        
        btn_delete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="Red",width=10,cursor="hand2",command=self.delete_date)
        btn_delete.grid(row=0,column=3,padx=1)
        
        
        #=====================================Right side photo===================================
        
        img1=Image.open(r"pohots\photo-1534438327276-14e5300c3a48.jpg")
        img1=img1.resize((850,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        leblimg1=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        leblimg1.place(x=440,y=55,width=850,height=200)
        
        img2=Image.open(r"pohots\Blog_Is-Gym-Air-Safe.jpeg")
        img2=img2.resize((420,250),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        leblimg2=Label(self.root,image=self.photoimg2,bd=1,relief=RIDGE)
        leblimg2.place(x=8,y=275,width=420,height=250)
        
        #=================================table frame search system==============================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View details and search data',padx=2,font=("arial",12,"bold"))      
        table_frame.place(x=435,y=200,width=860,height=330)
        
        labl_search=Label(table_frame, bd=2,text='Search by:',font=("arial",12,"bold"),bg='red',fg='white')
        labl_search.grid(row=0,column=0,sticky=W,padx=2)
        
        self.serch_var=StringVar()
        
        combo_search=ttk.Combobox(table_frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["values"]=("Date","Rentals",)
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        
        def replace_entry_with_combobox():
            self.serch_var.set("Rentals")  # Clear the search input
            self.txt_search.set("Electricity rent")  # Clear the search variable
            entry_search.grid_forget()  # Remove the entry widget
            combo_rentals.grid(row=0,column=2,padx=2)  # Add the combobox widget
        
        def restore_entry_widget():
            self.serch_var.set("Date")  # Clear the search input
            self.txt_search.set("")  # Clear the search variable
            combo_rentals.grid_forget()  # Remove the combobox widget
            entry_search.grid(row=0,column=2,padx=2)  # Add the entry widget
        
        combo_search.bind("<<ComboboxSelected>>", lambda event: replace_entry_with_combobox() if combo_search.get() == "Rentals" else restore_entry_widget())
        
        
        entry_search=ttk.Entry(table_frame,textvariable=self.txt_search, width=29,font=("arial",13,"bold"),justify='center')
        entry_search.grid(row=0,column=2,padx=2)
        
        combo_rentals=ttk.Combobox(table_frame,textvariable=self.txt_search,font=("arial",12,"bold"),width=29,state="readonly")
        combo_rentals["values"]=("Electricity rent","Water rent","Gym rent","Maintenance rent")
        combo_rentals.grid_forget()  # Hide the combobox initially
        
        btn_search=Button(table_frame,text="Search",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",command=self.search)
        btn_search.grid(row=0,column=3,padx=2)
        
        btn_showall=Button(table_frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",command=self.fetch_data)
        btn_showall.grid(row=0,column=4,padx=2)
        
        #======================show data table=======================================
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=255)
        
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.rent_details_table=ttk.Treeview(details_table,columns=("id","rent","date","price"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        

        scroll_y.config(command=self.rent_details_table.yview)
        self.rent_details_table.heading("id",text="Rent ID")
        self.rent_details_table.heading("rent",text="Rentals")
        self.rent_details_table.heading("date",text="Date")
        self.rent_details_table.heading("price",text="Price")
        
        
        
        self.rent_details_table["show"]="headings"
        
        self.rent_details_table.column("id",width=80)
        self.rent_details_table.column("rent",width=100)
        self.rent_details_table.column("date",width=100)
        self.rent_details_table.column("price",width=100)
        
        
        self.rent_details_table.pack(fill=BOTH,expand=1)
        self.rent_details_table.bind("<ButtonRelease-1>",self.get_cuersor)
        
        self.fetch_data()
        
    def add_data(self):
        if self.var_total.get() =="":
            messagebox.showerror("Eror  : ("," اكمل ادخال البينات لو سمحت",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into admin values(%s,%s,%s,%s)",(
                                                                            self.var_systemnum.get(),
                                                                            self.var_rent.get(),
                                                                            self.var_date.get(),
                                                                            self.var_total.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","تم اضافة فاتوره",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Worning!!",f"هناك شيء خطاء :{str(es)}",parent=self.root)
                
                
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from admin")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.rent_details_table.delete(*self.rent_details_table.get_children())
            for i in rows:
                self.rent_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()      
    
    def get_cuersor(self,event=""):
        cusrsor_row=self.rent_details_table.focus()
        content=self.rent_details_table.item(cusrsor_row)
        row=content["values"]
        
        self.var_systemnum.set(row[0]),
        self.var_rent.set(row[1]),
        self.var_date.set(row[2]),
        self.var_total.set(row[3]),
        
    def update_date(self):
        if self.var_total.get() =="":
            messagebox.showerror("Eror  : (","لو سمحت اكمل ادخال البينات",parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
            my_cursor = conn.cursor()
            my_cursor.execute("update admin set rent=%s,date=%s,total=%s where systemnum=%s",(
                                                                                        self.var_rent.get(),
                                                                                        self.var_date.get(),
                                                                                        self.var_total.get(),
                                                                                        self.var_systemnum.get()
                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update Success","تم التعديل بنجاح",parent=self.root)
            
    def delete_date(self):
        delete_date=messagebox.askyesno("GYM System","سيتم حذف هذه الفاتوره هل توافق؟",parent=self.root)
        if delete_date>0:
            conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
            my_cursor = conn.cursor()
            query="delete from admin where systemnum=%s"
            Value=(self.var_systemnum.get(),)
            my_cursor.execute(query,Value)
        else:
            if not delete_date:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
      
    def reset_date(self):
        self.var_total.set(""),
        self.var_rent.set("Electricity rent"),
        self.entry_date.set_date(None),
        x = random.randint(1000, 9999)
        self.var_systemnum.set(str(x))
        # Clear the DateEntry widget
    
        
    def search(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='password', database='gym')
        my_cursor = conn.cursor()
        if self.serch_var.get() == 'Rentals':
            my_cursor.execute("SELECT * FROM admin WHERE rent LIKE %s", ('%' + self.txt_search.get() + '%',))
        else:
            my_cursor.execute("SELECT * FROM admin WHERE date LIKE %s", ('%' + self.txt_search.get() + '%',))
        rows=my_cursor.fetchall()
        if len(rows) != 0:
            self.rent_details_table.delete(*self.rent_details_table.get_children())
            for i in rows:
                self.rent_details_table.insert("",END,values=i)
            conn.commit()
        else:
            mb.showwarning("Eror  :(", "بحث خاطئ حاول مجددا",parent=self.root)
        conn.close()
        
        
if __name__ == "__main__":
    root=Tk()
    obj = Rentals(root)
    root.mainloop()
  
        