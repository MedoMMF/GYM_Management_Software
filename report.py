from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
from tkcalendar import DateEntry
import mysql.connector
from tkinter import messagebox
import tkinter.messagebox as mb
from sendemail import EmailSender
class Report:
    def __init__(self,root):
        self.root = root
        self.root.title("Reports")
        self.root.geometry("1295x550+230+200")
        self.root.resizable(0,0)
        self.root.attributes('-toolwindow',True)
        
        
        self.var_sub= StringVar()
        self.var_total= StringVar()
        self.var_sdate= StringVar()
        self.var_edate= StringVar()
        self.var_systemnum=IntVar()
        x=random.randint(1000,9999)
        self.var_systemnum.set(str(x))
    
        #================================lable===============================
        lebl_title = Label(self.root,text="REPORT",font=("times new roman",18,"bold"),bg="black",fg="#FFBA7B",bd=4,relief=RIDGE)
        lebl_title.place(x=0,y=0,width=1295,height=50)
        
        labelfram_left=LabelFrame(self.root,bd=2,relief=RIDGE,padx=2,font=("arial",12,"bold"))      
        labelfram_left.place(x=5,y=50,width=1285,height=50)
        #===========================label and Entry==========================
        
        labl_sdate=Label(labelfram_left, bd=2,text='From',font=("arial",12,"bold"),padx=10,pady=6)
        labl_sdate.grid(row=0,column=2,sticky=W)
        
        self.entry_sdate = DateEntry(labelfram_left, textvariable=self.var_sdate,font=("arial", 12, "bold"), width=27, date_pattern="dd-mm-yyyy", state="readonly",justify='center')
        self.entry_sdate.grid(row=0,column=3,sticky=W)

        
        labl_edate=Label(labelfram_left, bd=2,text='To',font=("arial",12,"bold"),padx=10,pady=6)
        labl_edate.grid(row=0,column=4,sticky=W)
        
        self.entry_edate = DateEntry(labelfram_left, textvariable=self.var_edate,font=("arial", 12, "bold"), width=27, date_pattern="dd-mm-yyyy", state="readonly",justify='center')
        self.entry_edate.grid(row=0,column=5,sticky=W)
        
        # btn_print=Button(labelfram_left,text="Print",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",relief=RIDGE)
        # btn_print.place(x=1050,y=5)
        
        btn_sende=Button(labelfram_left,text="Send Email",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",relief=RIDGE,command=self.send_email)
        btn_sende.place(x=1170,y=5)
        
        
        ##
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='Revenue Report',padx=2,font=("arial",12,"bold"))      
        table_frame.place(x=5,y=100,width=1285,height=440)
        #===========================label and Entry==========================
        table_frame_entry=LabelFrame(table_frame,bd=2,relief=RIDGE,padx=2,font=("arial",12,"bold"))      
        table_frame_entry.place(x=5,y=10,width=380,height=170)
        
        labl_sup=Label(table_frame_entry, bd=2,text='Sub. Today',font=("arial",12,"bold"),padx=10,pady=6)
        labl_sup.grid(row=1,column=0,sticky=W)
            
        entry_sup=ttk.Entry(table_frame_entry, width=25,font=("arial",12,"bold"),justify='center',textvariable=self.var_sub)
        entry_sup.grid(row=1,column=1)
            
        labl_total=Label(table_frame_entry, bd=2,text='Total',font=("arial",12,"bold"),padx=10,pady=6)
        labl_total.grid(row=2,column=0,sticky=W)
            
        entry_total=ttk.Entry(table_frame_entry, width=25,font=("arial",12,"bold"),justify='center',textvariable=self.var_total)
        entry_total.grid(row=2,column=1)
            
        labl_id=Label(table_frame_entry, bd=2,text='Report Num.',font=("arial",12,"bold"),padx=10,pady=6)
        labl_id.grid(row=3,column=0,sticky=W)
            
        entry_id=ttk.Entry(table_frame_entry, width=25,textvariable=self.var_systemnum,font=("arial",12,"bold"),justify='center',state="readonly")
        entry_id.grid(row=3,column=1)
        
        #=================================bttns============================
        
        btn_frame=Frame(table_frame_entry,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=120,width=380,height=40)
        
        btn_add=Button(btn_frame,text="Save",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=9,cursor="hand2",command=self.add_data)
        btn_add.grid(row=0,column=0,padx=1)
        
        btn_update=Button(btn_frame,text="Update",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=9,cursor="hand2",command=self.update_date)
        btn_update.grid(row=0,column=1,padx=1)
        
        btn_reset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=9,cursor="hand2",command=self.reset_date)
        btn_reset.grid(row=0,column=2,padx=1)
        
        btn_delete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="Red",width=9,cursor="hand2",command=self.delete_date)
        btn_delete.grid(row=0,column=3,padx=1)
        
        #========================================================================================
        
        img2=Image.open(r"pohots\Quick-Report-Development-1-3253075316.png")
        img2=img2.resize((385,215),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        leblimg2=Label(table_frame,image=self.photoimg2,bd=1,relief=RIDGE)
        leblimg2.place(x=1,y=185,width=385,height=215)
        
        #=================================table frame search system==============================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='Veiw deatils and search data',padx=2,font=("arial",12,"bold"))      
        table_frame.place(x=400,y=120,width=885,height=400)
        
        labl_search=Label(table_frame, bd=2,text='Search by:',font=("arial",12,"bold"),bg='red',fg='white')
        labl_search.grid(row=0,column=0,sticky=W,padx=2)
        
        self.serch_var=StringVar()
        
        combo_search=ttk.Combobox(table_frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("ID","Date")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
         
        self.txt_search=StringVar()
        entry_search=ttk.Entry(table_frame,textvariable=self.txt_search, width=29,font=("arial",13,"bold"),justify='center')
        entry_search.grid(row=0,column=2,padx=2)

        btn_search=Button(table_frame,text="Search",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",command=self.search)
        btn_search.grid(row=0,column=3,padx=2)
        
        btn_showall=Button(table_frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,cursor="hand2",command=self.fetch_data)
        btn_showall.grid(row=0,column=4,padx=2)


        #======================show data table=======================================
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=40,width=880,height=330)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.rent_details_table=ttk.Treeview(details_table,columns=("id","sub","total","fromd",'tod'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.rent_details_table.xview)
        scroll_y.config(command=self.rent_details_table.yview)
        self.rent_details_table.heading("id",text="Report ID")
        self.rent_details_table.heading("sub",text="Sub Numbers")
        self.rent_details_table.heading("total",text="Total Salary")
        self.rent_details_table.heading("fromd",text="Date From")
        self.rent_details_table.heading("tod",text="To")
        
        
        
        self.rent_details_table["show"]="headings"
        
        self.rent_details_table.column("id",width=80)
        self.rent_details_table.column("sub",width=100)
        self.rent_details_table.column("total",width=100)
        self.rent_details_table.column("fromd",width=100)
        self.rent_details_table.column("tod",width=100)
        
        
        self.rent_details_table.pack(fill=BOTH,expand=1)
        self.rent_details_table.bind("<ButtonRelease-1>",self.get_cuersor)
        
        self.fetch_data()   
            
            
        
    def add_data(self):
        if self.var_sub.get() =="" and self.var_sub.get() =="":
            messagebox.showerror("Eror  : ("," اكمل ادخال البينات لو سمحت",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into report values(%s,%s,%s,%s,%s)",(
                                                                            self.var_systemnum.get(),
                                                                            self.var_sub.get(),
                                                                            self.var_total.get(),
                                                                            self.var_sdate.get(),
                                                                            self.var_edate.get()
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
        my_cursor.execute("select * from report")
        
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
        
        self.var_systemnum.set(row[0])
        self.var_sub.set(row[1])
        self.var_total.set(row[2])
        self.var_sdate.set(row[3])
        self.var_edate.set(row[4])

    
    def update_date(self):
        if self.var_sub.get() =="" and self.var_sub.get() =="":
            messagebox.showerror("Eror  : (","لو سمحت اكمل ادخال البينات",parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
            my_cursor = conn.cursor()
            my_cursor.execute("update report set sub=%s,total=%s,sdate=%s,edate=%s where id=%s",(
                                                                                        self.var_sub.get(),
                                                                                        self.var_total.get(),
                                                                                        self.var_sdate.get(),
                                                                                        self.var_edate.get(),
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
            query="delete from report where id=%s"
            Value=(self.var_systemnum.get(),)
            my_cursor.execute(query,Value)
        else:
            if not delete_date:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    
    def reset_date(self):
        self.var_sub.set(""),
        self.var_total.set(""),
        self.entry_sdate.set_date(None),
        self.entry_edate.set_date(None),
        x = random.randint(1000, 9999)
        self.var_systemnum.set(str(x))
        # Clear the DateEntry widget
    
    def send_email(self):
        if not hasattr(self, 'new_window') or not self.new_window.winfo_exists():
            self.new_window = Toplevel(self.root)
            self.app = EmailSender(self.new_window)
        else:
            self.new_window.lift()
    
    def search(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='password', database='gym')
        my_cursor = conn.cursor()
        if self.serch_var.get() == 'Date':
            my_cursor.execute("SELECT * FROM report WHERE sdate LIKE %s", ('%' + self.txt_search.get() + '%',))
        else:
            my_cursor.execute("SELECT * FROM report WHERE id LIKE %s", ('%' + self.txt_search.get() + '%',))
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
    obj = Report(root)
    root.mainloop()