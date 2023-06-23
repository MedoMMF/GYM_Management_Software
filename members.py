from tkinter import *
from tkinter import ttk
import mysql.connector
import random
from datetime import date, datetime, timedelta
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from tkinter import messagebox
import tkinter.messagebox as mb
class Members:
    def __init__(self,root):
        self.root = root
        self.root.title("Add_New_Member")
        self.root.geometry("1295x550+230+200")
        self.root.resizable(0,0)
        self.root.attributes('-toolwindow',True)
        
        #================================Variabels===========================
        self.var_systemnum=IntVar()
        x=random.randint(1000,9999)
        self.var_systemnum.set(str(x))
        
        self.var_member_name = StringVar()
        self.var_gender= StringVar()
        self.var_number = StringVar()
        self.var_number.trace('w', self.validate_phone)
        self.var_traning = StringVar()
        self.var_sub=StringVar()
        self.var_sdate= StringVar()
        self.var_edate= StringVar()
        self.var_total= StringVar()

        #================================Title===============================
        lebl_title = Label(self.root,text="ADD NEW MEMBER",font=("times new roman",18,"bold"),bg="black",fg="#FFBA7B",bd=4,relief=RIDGE)
        lebl_title.place(x=0,y=0,width=1295,height=50)
        
        #===========================label fram===============================
        labelfram_left=LabelFrame(self.root,bd=2,relief=RIDGE,text='Members Details',padx=2,font=("arial",12,"bold"))      
        labelfram_left.place(x=5,y=50,width=425,height=490)
            
        #===========================label and Entry==========================
        labl_name=Label(labelfram_left, bd=2,text='Member Name',font=("arial",12,"bold"),padx=10,pady=6)
        labl_name.grid(row=0,column=0,sticky=W)
        
        entry_name=ttk.Entry(labelfram_left, width=29,textvariable=self.var_member_name,font=("arial",12,"bold"),justify='center')
        entry_name.grid(row=0,column=1)
        
        labl_gender=Label(labelfram_left, bd=2,text='Gender',font=("arial",12,"bold"),padx=10,pady=6)
        labl_gender.grid(row=1,column=0,sticky=W)
        
        combo_gender=ttk.Combobox(labelfram_left,font=("arial",12,"bold"),textvariable=self.var_gender,width=27,justify='center',state="readonly")
        combo_gender["value"]=("Male","Female")
        combo_gender.current(0)
        combo_gender.grid(row=1,column=1)

        labl_phone=Label(labelfram_left, bd=2,text='Phone Number',font=("arial",12,"bold"),padx=10,pady=6)
        labl_phone.grid(row=2,column=0,sticky=W)
        
    
    
        def validate_phone_number(new_value):
            if len(new_value) > 11:
                return False
            return True
        
        entry_phone=ttk.Entry(labelfram_left, width=29, textvariable=self.var_number, font=("arial",12,"bold"), justify='center', validate='key')
        entry_phone['validatecommand'] = (entry_phone.register(validate_phone_number), '%P')
        entry_phone.grid(row=2,column=1)

         
        labl_id=Label(labelfram_left, bd=2,text='ID Number',font=("arial",12,"bold"),padx=10,pady=6)
        labl_id.grid(row=3,column=0,sticky=W)
        
    
        
        entry_id=ttk.Entry(labelfram_left, width=29,textvariable=self.var_systemnum,font=("arial",12,"bold"),justify='center',state="readonly")
        entry_id.grid(row=3,column=1)
    
        
        labl_train=Label(labelfram_left, bd=2,text='Training Type',font=("arial",12,"bold"),padx=10,pady=6)
        labl_train.grid(row=4,column=0,sticky=W)
        
        combo_train=ttk.Combobox(labelfram_left,font=("arial",12,"bold"),width=27,textvariable=self.var_traning,justify='center',state="readonly")
        combo_train["value"]=("Fitness","Private")
        combo_train.current(0)
        combo_train.grid(row=4,column=1)
        
        
        labl_sup=Label(labelfram_left, bd=2,text='Subscription',font=("arial",12,"bold"),padx=10,pady=6)
        labl_sup.grid(row=5,column=0,sticky=W)
        
        combo_sup=ttk.Combobox(labelfram_left,font=("arial",12,"bold"),textvariable=self.var_sub,width=27,justify='center',state="readonly")
        combo_sup["value"]=("Day","Month","3 Monthes")
        combo_sup.current(0)
        combo_sup.grid(row=5,column=1)
        
        
        
        
        def update_end_date(event=None):
            start_date_str = self.var_sdate.get()
            start_date = datetime.strptime(start_date_str, '%d-%m-%Y').date()
            subscription = combo_sup.get()
            if subscription == "Day":
                end_date = start_date + timedelta(days=1)
                if combo_train.get() == "Private":
                    messagebox.showerror("Eror","There is no private for one day",parent=self.root)
                else:
                    self.var_total.set("20 L.E")
            elif subscription == "Month":
                end_date = start_date + relativedelta(months=1)
                if combo_train.get() == "Private":
                    self.var_total.set("250 L.E")
                else:
                    self.var_total.set("200 L.E")
            elif subscription == "3 Months":
                end_date = start_date + relativedelta(months=3)
                if combo_train.get() == "Private":
                    self.var_total.set("500 L.E")
                else:
                    self.var_total.set("450 L.E")
            self.var_edate.set(end_date.strftime('%d-%m-%Y'))
    
        combo_sup.bind("<<ComboboxSelected>>", update_end_date)
    
        labl_sdate=Label(labelfram_left, bd=2, text='Start Date', font=("arial", 12, "bold"), padx=10, pady=6)
        labl_sdate.grid(row=6, column=0, sticky=W)
    
        self.entry_sdate =ttk.Entry(labelfram_left, textvariable=self.var_sdate, font=("arial", 12, "bold"), width=29, justify='center')
        self.entry_sdate.grid(row=6, column=1, sticky=W)
        today = date.today()
        date_string = today.strftime("%d-%m-%Y")
        self.var_sdate.set(date_string)
    
        labl_edate=Label(labelfram_left, bd=2, text='End Date', font=("arial", 12, "bold"), padx=10, pady=6)
        labl_edate.grid(row=7, column=0, sticky=W)
    
        self.entry_edate = ttk.Entry(labelfram_left, textvariable=self.var_edate, font=("arial", 12, "bold"), width=29, justify='center')
        self.entry_edate.grid(row=7, column=1, sticky=W)
        today = date.today()
        date_string = today.strftime("%d-%m-%Y")
        self.var_edate.set(date_string)
        
        labl_total=Label(labelfram_left, bd=2,text='Total Price',font=("arial",12,"bold"),padx=10,pady=6)
        labl_total.grid(row=9,column=0,sticky=W)
        
        entry_total=ttk.Entry(labelfram_left,textvariable=self.var_total, width=29,font=("arial",12,"bold"),justify='center')
        entry_total.grid(row=9,column=1)
        #=================================bttns============================
        
        btn_frame=Frame(labelfram_left,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        btn_add=Button(btn_frame,text="Add",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,command=self.add_data,cursor="hand2")
        btn_add.grid(row=0,column=0,padx=1)
        
        btn_update=Button(btn_frame,text="Update",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,command=self.update_date,cursor="hand2")
        btn_update.grid(row=0,column=1,padx=1)
        
        btn_reset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,command=self.reset_date,cursor="hand2")
        btn_reset.grid(row=0,column=2,padx=1)
        
        btn_delete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="Red",width=10,command=self.delete_date,cursor="hand2")
        btn_delete.grid(row=0,column=3,padx=1)
        #=================================table frame search system==============================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='Veiw deatils and search data',padx=2,font=("arial",12,"bold"))      
        table_frame.place(x=435,y=50,width=860,height=490)
        
        labl_search=Label(table_frame, bd=2,text='Searsh by:',font=("arial",12,"bold"),bg='red',fg='white')
        labl_search.grid(row=0,column=0,sticky=W,padx=2)
        
        self.serch_var=StringVar()
        
        combo_search=ttk.Combobox(table_frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Name","Phone","ID","Start date","End date")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
         
        self.txt_search=StringVar()
        entry_search=ttk.Entry(table_frame,textvariable=self.txt_search, width=29,font=("arial",13,"bold"),justify='center')
        entry_search.grid(row=0,column=2,padx=2)

        btn_search=Button(table_frame,text="Search",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,command=self.search,cursor="hand2")
        btn_search.grid(row=0,column=3,padx=2)
        
        btn_showall=Button(table_frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="#FFBA7B",width=10,command=self.fetch_data,cursor="hand2")
        btn_showall.grid(row=0,column=4,padx=2)
        
        #======================show data table=======================================
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=400)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.member_details_table=ttk.Treeview(details_table,columns=("id","name","gender","num","training","sub","sdate",'edate',"total"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.member_details_table.xview)
        scroll_y.config(command=self.member_details_table.yview)
        
        self.member_details_table.heading("id",text="ID")
        self.member_details_table.heading("name",text="Name")
        self.member_details_table.heading("gender",text="Gender")
        self.member_details_table.heading("num",text="Number")
        self.member_details_table.heading("training",text="Training Type")
        self.member_details_table.heading("sub",text="Subscription")
        self.member_details_table.heading("sdate",text="Start Date")
        self.member_details_table.heading("edate",text="End Date")
        self.member_details_table.heading("total",text="Total")
        
        self.member_details_table["show"]="headings"
        
        self.member_details_table.column("id",width=100)
        self.member_details_table.column("name",width=100)
        self.member_details_table.column("gender",width=100)
        self.member_details_table.column("num",width=100)
        self.member_details_table.column("training",width=100)
        self.member_details_table.column("sub",width=100)
        self.member_details_table.column("sdate",width=100)
        self.member_details_table.column("edate",width=100)
        self.member_details_table.column("total",width=100)
        
        self.member_details_table.pack(fill=BOTH,expand=1)
        self.member_details_table.bind("<ButtonRelease-1>",self.get_cuersor)
        
        self.fetch_data()
        
    def add_data(self):
        if self.var_member_name.get() =="" or self.var_number.get()=="" or self.var_total.get()=="":
            messagebox.showerror("Eror  : ("," اكمل ادخال البينات لو سمحت",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into member values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_systemnum.get(),
                                                                            self.var_member_name.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_number.get(),
                                                                            self.var_traning.get(),
                                                                            self.var_sub.get(),
                                                                            self.var_sdate.get(),
                                                                            self.var_edate.get(),
                                                                            self.var_total.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","تم اضافة العضو",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Worning!!",f"هناك شيء خطاء :{str(es)}",parent=self.root)
                
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from member")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.member_details_table.delete(*self.member_details_table.get_children())
            for i in rows:
                self.member_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cuersor(self,event=""):
        cusrsor_row=self.member_details_table.focus()
        content=self.member_details_table.item(cusrsor_row)
        row=content["values"]
        
        self.var_systemnum.set(row[0]),
        self.var_member_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_number.set(row[3]),
        self.var_traning.set(row[4]),
        self.var_sub.set(row[5]),
        self.var_sdate.set(row[6]),
        self.var_edate.set(row[7]),
        self.var_total.set(row[8]),
        
        
        
    def update_date(self):
        if self.var_number.get()=="" or self.var_total.get()=="":
            messagebox.showerror("Eror  : (","لو سمحت اكمل ادخال البينات",parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
            my_cursor = conn.cursor()
            my_cursor.execute("update member set Name=%s,Gender=%s,Number=%s,Traning=%s,Sub=%s,Sdate=%s,Edate=%s,total=%s where systemnum=%s",(
                                                                                        self.var_member_name.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_number.get(),
                                                                                        self.var_traning.get(),
                                                                                        self.var_sub.get(),
                                                                                        self.var_sdate.get(),
                                                                                        self.var_edate.get(),
                                                                                        self.var_total.get(),
                                                                                        self.var_systemnum.get()
                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update Success","تم التعديل بنجاح",parent=self.root)
        
        
        
    def delete_date(self):
        delete_date=messagebox.askyesno("GYM System","هل تريد حقا حذف هذا العضو؟",parent=self.root)
        if delete_date>0:
            conn = mysql.connector.connect(host='localhost', username = 'root', password = 'password', database='gym')
            my_cursor = conn.cursor()
            query="delete from member where systemnum=%s"
            Value=(self.var_systemnum.get(),)
            my_cursor.execute(query,Value)
        else:
            if not delete_date:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    
    def reset_date(self):
        self.var_member_name.set(""),
        self.var_number.set(""),
        self.var_total.set(""),
        today = date.today()
        date_string = today.strftime("%d-%m-%Y")
        self.var_sdate.set(date_string),
        self.var_edate.set(date_string),
        x=random.randint(1000,9999)
        self.var_systemnum.set(str(x))
        
        
    def search(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='password', database='gym')
        my_cursor = conn.cursor()
        if self.serch_var.get() == 'Name':
            my_cursor.execute("SELECT * FROM member WHERE Name LIKE %s", ('%' + self.txt_search.get() + '%',))
        elif self.serch_var.get() == 'ID':
            my_cursor.execute("SELECT * FROM member WHERE systemnum LIKE %s", ('%' + self.txt_search.get() + '%',))
            
        elif self.serch_var.get() == 'Start date':
            my_cursor.execute("SELECT * FROM member WHERE Sdate LIKE %s", ('%' + self.txt_search.get() + '%',))
            
        elif self.serch_var.get() == 'End date':
            my_cursor.execute("SELECT * FROM member WHERE Edate LIKE %s", ('%' + self.txt_search.get() + '%',))
        else:
            my_cursor.execute("SELECT * FROM member WHERE Number LIKE %s", ('%' + self.txt_search.get() + '%',))
        rows=my_cursor.fetchall()
        if len(rows) != 0:
            self.member_details_table.delete(*self.member_details_table.get_children())
            for i in rows:
                self.member_details_table.insert("",END,values=i)
            conn.commit()
        else:
            mb.showwarning("Eror  :(", "بحث خاطئ حاول مجددا",parent=self.root)
        conn.close()
        

    def validate_phone(self, *args):
        if not self.var_number.get():
            return    
        if not self.var_number.get().isdigit():
            messagebox.showerror("خطاء في الادخال", "ادخل ارقام فقط",parent=self.root)

            self.var_number.set("")
            
    def validate_id(self, *args):
        if not self.var_id.get():
            return
        if not self.var_id.get().isdigit():
            messagebox.showerror("خطاء في الادخال", "ادخل ارقام فقط",parent=self.root)

            self.var_id.set("")
                
    
if __name__ == "__main__":
    root=Tk()
    obj = Members(root)
    root.mainloop()
  
        
