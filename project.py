from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview, Style

import mysql.connector
from tkcalendar import Calendar

dtabse = mysql.connector.connect(host='localhost',
                                 user="root",
                                 passwd="",
                                 database="prodganize")
pointer = dtabse.cursor(buffered=True)
usrnm = dtabse.cursor(buffered=True)
pswrd = dtabse.cursor(buffered=True)
cursor = dtabse.cursor(buffered=True)
cursor2 = dtabse.cursor(buffered=True)
cursor3 = dtabse.cursor(buffered=True)
curs = dtabse.cursor(buffered=True)
usrnm.execute("SELECT username FROM accounts")
pswrd.execute("SELECT password FROM accounts")
pointer.execute("SELECT * FROM accounts")
usernam = usrnm.fetchall()
passw = pswrd.fetchall()
curs.execute("SELECT pid FROM patients")
cur = [x[0] for x in curs]
username = [i[0] for i in usernam]
password = [a[0] for a in passw]


class proj:
    def __init__(self, window, width, height):
        self.search_button = None
        self.winsearch = None
        self.search = None
        self.todel = None
        screenw = winblit.winfo_screenwidth()
        screenh = winblit.winfo_screenheight()
        self.x = ((screenw / 2) - (width / 2))
        self.y = ((screenh / 2) - (height / 2))
        self.window = window
        self.width = width
        self.height = height
        self.window.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
        self.window.configure(background="#282828")
        self.height = 800
        self.width = 900
        self.window.title("Docganize - Patient Management System")
        self.id = 0
        self.style = Style()
        self.style.theme_use("alt")

        # log in / landing screen
        self.landing_scrn = Frame(self.window)
        self.landing_scrn.pack(expand=True)
        self.lbl = Canvas(self.landing_scrn, width=self.width, height=self.height, bg="#282828", border="0",
                          highlightthickness="0")
        self.lbl.place(x=0, y=0)
        self.show_password_var = BooleanVar()
        self.show_hide_btn = Checkbutton(self.landing_scrn, variable=self.show_password_var, command=self.pass_visib,
                                         background="#282828")
        self.show_hide_btn.pack()
        self.show_hide_btn.place(x=230, y=305)
        self.lbl.create_text(310, 318, text="SHOW PASSWORD", font=("times new roman", 8), fill="white")
        self.lbl.pack()

        self.lbl.create_text(300, 100, text="Welcome to Docganize", font=("times new roman", 30), fill="white")
        self.lbl.pack()
        self.lbl.create_text(300, 180, text="Enter Username:", font=("times new roman", 13, "bold"), fill="white")
        self.lbl.pack()
        self.username = Entry(self.landing_scrn, font=("arial", 13), borderwidth=5, relief="sunken")
        self.username.place(width=270, height=30, x=160, y=190)
        self.lbl.create_text(300, 260, text="Enter Password:", font=("times new roman", 13, "bold"), fill="white")
        self.lbl.pack()
        self.user_pass = Entry(self.landing_scrn, font=("arial", 13), show='*', borderwidth=5, relief="sunken")
        self.user_pass.pack()
        self.user_pass.place(width=270, height=30, x=160, y=270)
        self.login_btn = Button(self.landing_scrn, text="log in", font=("arial", 11, "bold"), borderwidth=5,
                                relief="raised",
                                command=self.enter_indexscrn)
        self.login_btn.place(width=80, height=30, x=250, y=335)
        self.lbl.create_text(290, 380, text="or", font=("times new roman", 13, "bold"), fill="white")
        self.lbl.pack()
        self.rgstr_btn = Button(self.landing_scrn, text="register", font=("arial", 11, "bold"), borderwidth=5,
                                relief="raised",
                                command=self.enter_rgstr)
        self.rgstr_btn.place(width=80, height=30, x=250, y=400)

        # rgister page
        self.rgstr_scrn = Frame(self.window, width=self.width, height=self.height, bg="#282828")
        self.lbl = Canvas(self.rgstr_scrn, width=self.width, height=self.height, bg="#282828", highlightthickness="0")
        self.lbl.place(x=0, y=0)
        self.lbl.create_text(300, 90, text="Register", font=("times new roman", 50), fill="white")
        self.lbl.pack()
        self.lbl.create_text(205, 160, text="Enter your name:", font=("times new roman", 15, "bold"), fill="white")
        self.lbl.pack()
        self.name = Entry(self.rgstr_scrn, font=("arial", 13), show='', borderwidth=5, relief="sunken")
        self.name.place(width=350, height=30, x=130, y=170)
        self.lbl.create_text(195, 220, text="Enter your age:", font=("times new roman", 15, "bold"), fill="white")
        self.lbl.pack()
        self.age = Entry(self.rgstr_scrn, font=("arial", 13), borderwidth=5, relief="sunken")
        self.age.place(width=350, height=30, x=130, y=230)
        self.lbl.create_text(205, 280, text="Username:            ", font=("times new roman", 15, "bold"), fill="white")
        self.lbl.pack()
        self.user_name = Entry(self.rgstr_scrn, font=("arial", 13), show='', borderwidth=5, relief="sunken")
        self.user_name.place(width=350, height=30, x=130, y=290)
        self.lbl.create_text(205, 340, text="Password:            ", font=("times new roman", 15, "bold"), fill="white")
        self.lbl.pack()
        self.user_password = Entry(self.rgstr_scrn, font=("arial", 13), show='*', borderwidth=5, relief="sunken")
        self.user_password.pack()
        self.user_password.place(width=350, height=30, x=130, y=350)
        self.lbl.create_text(218, 400, text="SHOW PASSWORD", font=("times new roman", 8), fill="white")
        self.lbl.pack()
        self.show_hide_bton = Checkbutton(self.rgstr_scrn, variable=self.show_password_var, command=self.pass_visib,
                                          background="#282828")
        self.show_hide_bton.pack()
        self.show_hide_bton.place(x=130, y=388)
        self.submit_btn = Button(self.rgstr_scrn, text="submit", font=("arial", 11, "bold"), borderwidth=5,
                                 relief="raised",
                                 command=self.reg_submit)
        self.submit_btn.place(width=80, height=30, x=290, y=420)
        self.back_btn = Button(self.rgstr_scrn, text="back", font=("arial", 11, "bold"), borderwidth=5, relief="raised",
                               command=self.log_out)
        self.back_btn.place(width=80, height=30, x=205, y=420)

        # interface page
        self.index_scrn = Frame(self.window)
        self.lbl = Canvas(self.index_scrn, width=1650, height=950, bg="#282828", border="0", highlightthickness="0")
        self.lbl.place(x=0, y=0)
        self.lbl.create_text(760, 60, text="Docganize Patient Management Inventory", font=("times new roman", 30),
                             fill="white")
        self.lbl.pack()
        self.interface_frame = Frame(self.index_scrn, bg="#e1e4e8", borderwidth=10,
                                     relief="ridge")  # frame where the Table data will be displayed
        self.interface_frame.place(x=415, y=110, width=1120, height=775)

        # index action options
        self.actop_scrn = Frame(self.index_scrn)
        self.actop_scrn.place(x=15, y=110, width=395, height=775)
        self.act = Canvas(self.actop_scrn, width=375, height=755, bg="#575757", borderwidth=10, relief="ridge")
        self.act.place(x=0, y=0)
        self.act.create_text(200, 50, text="Select action", font=("times new roman", 25, "bold"), fill="WHITE")

        self.search_btn = Button(self.actop_scrn, text="search", font=("OPEN SANS", 13, "bold"), bg="#fcb02b",
                                 borderwidth=5, relief="raised", cursor="circle", command=self.lookup_records)
        self.search_btn.place(width=65, height=30, x=305, y=100)
        self.search_btn1 = Button(self.actop_scrn, text="again", font=("OPEN SANS", 13, "bold"), bg="#fcb02b",
                                  borderwidth=5, relief="raised", cursor="circle", command=self.srchbtn1_act)

        self.srchlbl = Label(self.actop_scrn, text="Click to look for record >>", font=("arial", 13), borderwidth=3,
                             relief="ridge")
        self.srchlbl.place(width=280, height=40, x=15, y=95)
        self.addpatient_btn = Button(self.actop_scrn, text="ADD PATIENT", font=("Open Sans", 13, "bold"), bg="#093145",
                                     fg="WHITE",
                                     borderwidth=3, relief="raised", command=self.add_patient)
        self.addpatient_btn.place(width=170, height=40, x=15, y=140)
        self.delpatient_btn = Button(self.actop_scrn, text="DELETE PATIENT'S \n INFO", font=("open sans", 10, "bold"),
                                     bg="#093145", fg="WHITE", borderwidth=3, relief="raised", command=self.del_patient)
        self.delpatient_btn.place(width=195, height=40, x=190, y=140)
        self.updateinfo_btn = Button(self.actop_scrn, text="UPDATE PATIENT'S \n INFO", font=("open sans", 10, "bold"),
                                     bg="#093145", fg="WHITE", borderwidth=3, relief="raised", command=self.update_inf)
        self.updateinfo_btn.place(width=170, height=40, x=15, y=200)
        self.logout_btn = Button(self.actop_scrn, text="LOG OUT", font=("open sans", 15, "bold"), bg="#093145",
                                 command=self.log_out, borderwidth=3, relief="raised", fg="WHITE")
        self.logout_btn.place(width=195, height=40, x=190, y=200)

        #  add patient form
        self.my_lbl = Label(self.actop_scrn, text="Add Patient", font=("open sans", 15, "bold"), bg="#575757",
                            fg="WHITE")
        self.lname = Label(self.actop_scrn, text="Last Name", font=("open sans", 13), bg="#575757",
                           fg="WHITE")
        self.fname = Label(self.actop_scrn, text="First Name, MI", font=("open sans", 13), bg="#575757",
                           fg="WHITE")
        self.page = Label(self.actop_scrn, text="Age", font=("open sans", 15), bg="#575757",
                          fg="WHITE")
        self.pGender = Label(self.actop_scrn, text="Gender", font=("open sans", 15), bg="#575757",
                             fg="WHITE")
        self.padd = Label(self.actop_scrn, text="Address", font=("open sans", 13), bg="#575757",
                          fg="WHITE")
        self.wbnum = Label(self.actop_scrn, text="Ward/Bed #", font=("open sans", 13), bg="#575757",
                           fg="WHITE")
        self.healthrec = Label(self.actop_scrn, text="Health Record", font=("open sans", 13), bg="#575757",
                               fg="WHITE")
        self.patID = Label(self.actop_scrn, text="Patient's ID", font=("open sans", 13), bg="#575757",
                           fg="WHITE")
        self.pstatus = Label(self.actop_scrn, text="Status", font=("open sans", 13), bg="#575757",
                             fg="WHITE")
        self.dAd = Label(self.actop_scrn, text="Date Admitted", font=("open sans", 12), bg="#575757",
                         fg="WHITE")
        self.dDis = Label(self.actop_scrn, text="Date Discharged", font=("open sans", 11), bg="#575757",
                          fg="WHITE")
        self.dRef = Label(self.actop_scrn, text="Date Referred", font=("open sans", 11), bg="#575757",
                          fg="WHITE")
        self.patientlname = Entry(self.actop_scrn, font=("arial", 13), borderwidth=5, relief="sunken")
        self.patientfname = Entry(self.actop_scrn, font=("arial", 13), borderwidth=5, relief="sunken")
        self.patientage = Entry(self.actop_scrn, font=("arial", 13), borderwidth=5, relief="sunken")
        self.patientgen = Combobox(self.actop_scrn, values=["Male", "Female"])
        self.patientaddress = Entry(self.actop_scrn, font=("arial", 13), borderwidth=5, relief="sunken")
        self.patientwbnum = Entry(self.actop_scrn, font=("arial", 13), borderwidth=5, relief="sunken")
        self.cal = Calendar(self.actop_scrn, selectmode='day', year=2023, month=11, day=1)
        self.patientHealthrec = Text(self.actop_scrn, font=("arial", 13), borderwidth=5, relief="sunken")
        self.patientID = Label(self.actop_scrn, text="Select Patient's ID", font=("arial", 13), borderwidth=5,
                               relief="sunken")
        self.status = Combobox(self.actop_scrn, values=('None', 'Assisted', 'Admitted', 'Discharged', 'Referred', 'D-'),
                               postcommand=self.getdeyt)
        self.nxt_btn = Button(self.actop_scrn, text="nxt", font=("arial", 11), borderwidth=5, relief="raised",
                              command=self.statchng)
        self.slct_btn = Button(self.actop_scrn, text="slct", font=("arial", 9), borderwidth=5, relief="raised",
                               command=self.select_id)
        self.add_submit = Button(self.actop_scrn, text="ADD >>", font=("arial", 11, "bold"), borderwidth=5,
                                 relief="raised", bg="#fcb02b",
                                 command=self.add_submission)
        self.update_submit = Button(self.actop_scrn, text="UPDATE NOW >>", font=("arial", 10, "bold"), borderwidth=5,
                                    relief="raised", bg="#fcb02b",
                                    command=self.update_submission)
        self.dateAd = Combobox(self.actop_scrn, font=("arial", 13), show='', postcommand=self.grad_date)
        self.nxtt_btn = Button(self.actop_scrn, text="ok", font=("arial", 11), borderwidth=5, relief="raised",
                               command=self.getdeyt)
        self.dateDis = Combobox(self.actop_scrn, font=("arial", 13), postcommand=self.grad_date)
        self.dateRef = Combobox(self.actop_scrn, font=("arial", 13), postcommand=self.grad_date)

        # Treeview
        self.tree = Treeview(self.interface_frame, selectmode='browse', height=30)
        self.tree['columns'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        self.tree['show'] = 'headings'
        self.tree.column('1', width=50, minwidth=50, anchor='center')
        self.tree.column('2', width=350, minwidth=350, anchor='center')
        self.tree.column('3', width=350, minwidth=350, anchor='center')
        self.tree.column('4', width=70, minwidth=70, anchor='center')
        self.tree.column('5', width=70, minwidth=70, anchor='center')
        self.tree.column('6', width=400, minwidth=400, anchor='center')
        self.tree.column('7', width=150, minwidth=150, anchor='center')
        self.tree.column('8', width=500, minwidth=500, anchor='center')
        self.tree.column('9', width=100, minwidth=100, anchor='center')
        self.tree.column('10', width=300, minwidth=300, anchor='center')
        self.tree.column('11', width=300, minwidth=300, anchor='center')
        self.tree.column('12', width=300, minwidth=300, anchor='center')
        self.tree.heading('1', text='P-ID')
        self.tree.heading('2', text='Last Name')
        self.tree.heading('3', text='First Name')
        self.tree.heading('4', text='Age')
        self.tree.heading('5', text='Sex')
        self.tree.heading('6', text='Address')
        self.tree.heading('7', text='Ward/Bed#')
        self.tree.heading('8', text='Health Record')
        self.tree.heading('9', text='Status')
        self.tree.heading('10', text='Date Admitted')
        self.tree.heading('11', text='Date Discharged')
        self.tree.heading('12', text='Date Referred')
        self.tree.tag_configure('color1', background="#88a7a8")
        self.tag = ''

        self.style.configure("Treeview.Heading", font=(None, 16, "bold"), foreground="white", background="#093145")
        self.style.configure("Treeview", font=("times new roman", 15), rowheight=40, borderweight=10)
        self.style.configure("Treeview.Column", rowheight=40)
        self.tree.pack(side=TOP, fill="both", expand=True)
        self.treeScrollx = Scrollbar(self.tree, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.treeScrollx.set)
        self.treeScrollx.pack(side="bottom", fill="x")
        self.treeScrolly = Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.treeScrolly.set)
        self.treeScrolly.pack(side="right", fill="y")

    def view_table(self):
        cursor.execute("SELECT * FROM patients")
        rec = cursor.fetchall()
        for record in rec:
            self.tree.insert(parent='', index='end', iid=record, text='',
                             values=(
                                 record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                                 record[8], record[9], record[10], record[11]),
                             )

    def getdeyt(self):  # set date
        a = self.cal.get_date()
        self.cal.pack_forget()
        self.dateAd.set(a)
        self.dateDis.set(a)
        self.dateRef.set(a)

    def grad_date(self):  # show calendar
        self.cal.pack(pady=20)

    def pass_visib(self):
        if self.show_password_var.get():
            self.user_pass.config(show='')
            self.user_password.config(show='')
        else:
            self.user_pass.config(show='*')
            self.user_password.config(show='*')

    # method to enter index screen
    def enter_indexscrn(self):
        if self.username.get() in username and self.user_pass.get() in password:
            self.landing_scrn.forget()
            self.window.geometry('%dx%d+%d+%d' % (1540, 900, 170, 65))
            self.index_scrn.pack(side=LEFT, expand=True)

        else:
            messagebox.showerror(title="Log in Failed", message="No existing credentials found!! Please register")
            return True

    def enter_rgstr(self):
        self.landing_scrn.forget()
        self.rgstr_scrn.place(x=0, y=0, width=self.width, height=self.height)

    def log_out(self):
        self.window.geometry('%dx%d+%d+%d' % (600, 500, self.x, self.y))
        self.rgstr_scrn.place_forget()
        self.index_scrn.forget()
        self.actop_scrn.forget()
        self.landing_scrn.pack(expand=True)

    def reg_submit(self):
        if len(self.user_name.get()) == 0 and len(self.name.get()) == 0:
            messagebox.showerror(title="Registration Failed", message="This field cannot be empty!!")
            return True
        elif len(self.user_password.get()) < 8:
            messagebox.showerror(title="Registration Failed", message="Password must be at least 8 characters")
            return True
        elif self.user_name.get() in username:
            messagebox.showerror(title="Registration Failed", message="Username already exist")
            return True
        elif self.age.get() < "18":
            messagebox.showerror(title="Registration Failed", message="Age must be 18 and above")
            return True
        else:
            pointer.execute("INSERT into accounts(Name, Age, username, password) VALUES(%s, %s, %s, %s)",
                            (self.name.get(), self.age.get(), self.user_name.get(), self.user_password.get()))
            dtabse.commit()
            self.rgstr_scrn.place_forget()
            self.index_scrn.forget()
            self.actop_scrn.forget()
            self.window.geometry('%dx%d+%d+%d' % (600, 500, self.x, self.y))
            self.landing_scrn.pack(expand=True)
            self.name.delete(0, END)
            self.age.delete(0, END)
            self.user_name.delete(0, END)
            self.user_password.delete(0, END)
            messagebox.showinfo(title="Registration Successful!", message="Please login to enter system")
            return True

    def statchng(self):  # to pop the date info
        self.nxtt_btn.place(width=30, height=30, x=355, y=715)
        val = list(self.status['values'])
        if self.status.get() == val[1]:
            self.dateAd.place(width=220, height=30, x=130, y=715)
            self.dAd.place(x=15, y=715)
            self.dateDis.place_forget()
            self.dDis.place_forget()
            self.dRef.place_forget()
            self.dateRef.place_forget()
            self.dateDis.delete(0, END)
            self.dateRef.delete(0, END)
        elif self.status.get() == val[2]:
            self.dateAd.place(width=220, height=30, x=130, y=715)
            self.dAd.place(x=15, y=715)
            self.dateDis.place_forget()
            self.dDis.place_forget()
            self.dRef.place_forget()
            self.dateRef.place_forget()
            self.dateDis.delete(0, END)
            self.dateRef.delete(0, END)
        elif self.status.get() == val[3]:
            self.dateDis.place(width=220, height=30, x=130, y=715)
            self.dDis.place(x=15, y=715)
            self.dateAd.place_forget()
            self.dAd.place_forget()
            self.dRef.place_forget()
            self.dateRef.place_forget()
            self.dateAd.delete(0, END)
            self.dateRef.delete(0, END)
        elif self.status.get() == val[5]:
            self.dateDis.place(width=220, height=30, x=130, y=715)
            self.dDis.place(x=15, y=715)
            self.dateAd.place_forget()
            self.dRef.place_forget()
            self.dateRef.place_forget()
            self.dAd.place_forget()
            self.dateAd.delete(0, END)
            self.dateRef.delete(0, END)
        elif self.status.get() == val[4]:
            self.dateRef.place(width=220, height=30, x=130, y=715)
            self.dRef.place(x=15, y=715)
            self.dateDis.place_forget()
            self.dateAd.place_forget()
            self.dDis.place_forget()
            self.dAd.place_forget()
            self.dateAd.delete(0, END)
            self.dateDis.delete(0, END)

        else:
            self.dateAd.place_forget()
            self.dateDis.place_forget()
            self.dateRef.place_forget()
            self.dAd.place_forget()
            self.dDis.place_forget()
            self.dRef.place_forget()
            self.nxtt_btn.place_forget()
            self.dateAd.delete(0, END)
            self.dateDis.delete(0, END)
            self.dateRef.delete(0, END)

    def update_inf(self):
        self.srchlbl.config(text="Click to look for record >>")
        if self.updateinfo_btn['text'] == "UPDATE PATIENT'S \n INFO":
            self.add_submit.place_forget()
            self.my_lbl.config(text=" Update Patient Information", font=("open sans", 13, "bold"))
            self.my_lbl.place(x=15, y=260)
            self.update_submit.place(width=130, height=50, x=250, y=250)
            self.patID.place(x=15, y=305)
            self.lname.place(x=15, y=345)
            self.fname.place(x=15, y=385)
            self.page.place(x=15, y=425)
            self.pGender.place(x=15, y=465)
            self.padd.place(x=15, y=505)
            self.wbnum.place(x=15, y=545)
            self.healthrec.place(x=15, y=585)
            self.slct_btn.place(width=30, height=30, x=355, y=305)
            self.pstatus.place(x=15, y=680)
            self.nxt_btn.place(width=30, height=30, x=355, y=680)
            self.patientID.place(width=220, height=30, x=130, y=305)
            self.patientlname.place(width=250, height=30, x=130, y=345)
            self.patientfname.place(width=250, height=30, x=130, y=385)
            self.patientage.place(width=250, height=30, x=130, y=425)
            self.patientgen.place(width=250, height=30, x=130, y=465)
            self.patientaddress.place(width=250, height=30, x=130, y=505)
            self.patientwbnum.place(width=250, height=30, x=130, y=545)
            self.patientHealthrec.place(width=250, height=90, x=130, y=585)
            self.status.place(width=220, height=30, x=130, y=680)
            self.updateinfo_btn.config(text="UPDATE PATIENT'S \n INFO  ", bg="white", fg="black", relief="groove")
            self.addpatient_btn.config(text="ADD PATIENT")
            self.addpatient_btn.config(bg="#093145", fg="WHITE", relief="raised")

        else:
            self.srchlbl.config(text="Click to look for record >>")
            self.my_lbl.place_forget()
            self.add_submit.place_forget()
            self.update_submit.place_forget()
            self.lname.place_forget()
            self.fname.place_forget()
            self.page.place_forget()
            self.pGender.place_forget()
            self.padd.place_forget()
            self.wbnum.place_forget()
            self.healthrec.place_forget()
            self.pstatus.place_forget()
            self.patientlname.place_forget()
            self.patientfname.place_forget()
            self.patientage.place_forget()
            self.patientgen.place_forget()
            self.patientaddress.place_forget()
            self.patientwbnum.place_forget()
            self.patientHealthrec.place_forget()
            self.status.place_forget()
            self.nxt_btn.place_forget()
            self.dateAd.place_forget()
            self.dateDis.place_forget()
            self.dateRef.place_forget()
            self.dAd.place_forget()
            self.dDis.place_forget()
            self.dRef.place_forget()
            self.patID.place_forget()
            self.patientID.place_forget()
            self.nxtt_btn.place_forget()
            self.slct_btn.place_forget()
            self.updateinfo_btn.config(text="UPDATE PATIENT'S \n INFO", bg="#093145", fg="WHITE", relief="raised")

    def select_id(self):
        selected = self.tree.focus()
        selval = self.tree.item(selected, 'values')
        self.patientlname.insert(0, selval[1])
        self.patientfname.insert(0, selval[2])
        self.patientage.insert(0, selval[3])
        self.patientgen.insert(0, selval[4])
        self.patientaddress.insert(0, selval[5])
        self.patientwbnum.insert(0, selval[6])
        self.patientHealthrec.insert(INSERT, selval[7])
        self.patientID.config(text=selval[0])
        self.status.insert(0, selval[8])
        self.dateAd.insert(0, selval[9])
        self.dateDis.insert(0, selval[10])
        self.dateRef.insert(0, selval[11])

    def update_submission(self):
        if self.patientID.cget('text') is None:
            messagebox.showerror(title="Adding Failed", message="make sure all required (*) blank is filled!!")
            return True
        else:
            selected = self.tree.focus()
            self.tree.item(selected, values=(
                self.patientID.cget('text'), self.patientlname.get(), self.patientfname.get(), self.patientage.get(),
                self.patientgen.get(),
                self.patientaddress.get(), self.patientwbnum.get(), self.patientHealthrec.get(1.0, "end-1c"),
                self.status.get(), self.dateAd.get(), self.dateDis.get(), self.dateRef.get(),
                self.patientID.cget('text')))
            cursor.execute(
                "UPDATE patients SET `pid`=%s ,`Last Name`=%s, `First Name, MI`=%s, `Age`=%s,  `Sex`=%s, `Address`=%s, `Ward #, Bed#`=%s, `Health Record`=%s, `Status`=%s, `Date Admitted`=%s, `Date Discharged`=%s, `Date Reffered`=%s WHERE  `pid`= %s",
                (self.patientID.cget('text'), self.patientlname.get(), self.patientfname.get(), self.patientage.get(),
                 self.patientgen.get(),
                 self.patientaddress.get(), self.patientwbnum.get(), self.patientHealthrec.get(1.0, "end-1c"),
                 self.status.get(), self.dateAd.get(), self.dateDis.get(), self.dateRef.get(),
                 self.patientID.cget('text')))
            dtabse.commit()

            messagebox.showinfo(title="Update Patient", message="Patient updated successfuly!")
            return True

    def add_patient(self):
        if self.addpatient_btn['text'] == "ADD PATIENT":
            self.srchlbl.config(text="Click to look for record >>")
            self.patientlname.delete(0, END)
            self.patientfname.delete(0, END)
            self.patientage.delete(0, END)
            self.patientgen.delete(0, END)
            self.patientaddress.delete(0, END)
            self.patientwbnum.delete(0, END)
            self.patientHealthrec.delete("1.0", "end")
            self.patientID.config(text="Select Patient's ID")
            self.status.delete(0, END)
            self.dateAd.delete(0, END)
            self.dateDis.delete(0, END)
            self.dateRef.delete(0, END)
            self.slct_btn.place_forget()
            self.update_submit.place_forget()
            self.patID.place_forget()
            self.patientID.place_forget()
            self.my_lbl.place(x=15, y=260)
            self.add_submit.place(width=100, height=50, x=270, y=250)
            self.lname.place(x=15, y=305)
            self.fname.place(x=15, y=345)
            self.page.place(x=15, y=385)
            self.pGender.place(x=15, y=425)
            self.padd.place(x=15, y=465)
            self.wbnum.place(x=15, y=505)
            self.healthrec.place(x=15, y=545)
            self.pstatus.place(x=15, y=675)
            self.nxt_btn.place(width=30, height=30, x=355, y=675)
            self.patientlname.place(width=250, height=30, x=130, y=305)
            self.patientfname.place(width=250, height=30, x=130, y=345)
            self.patientage.place(width=250, height=30, x=130, y=385)
            self.patientgen.place(width=250, height=30, x=130, y=425)
            self.patientaddress.place(width=250, height=30, x=130, y=465)
            self.patientwbnum.place(width=250, height=30, x=130, y=505)
            self.patientHealthrec.place(width=250, height=120, x=130, y=545)
            self.status.place(width=220, height=30, x=130, y=675)
            self.addpatient_btn.config(text="ADD PATIENT ", bg="white", fg="black", relief="groove")
            self.updateinfo_btn.config(text="UPDATE PATIENT'S \n INFO", bg="#093145", fg="WHITE", relief="raised")

        else:
            self.srchlbl.config(text="Click to look for record >>")
            self.my_lbl.place_forget()
            self.add_submit.place_forget()
            self.update_submit.place_forget()
            self.patID.place_forget()
            self.patientID.place_forget()
            self.lname.place_forget()
            self.fname.place_forget()
            self.page.place_forget()
            self.pGender.place_forget()
            self.padd.place_forget()
            self.wbnum.place_forget()
            self.healthrec.place_forget()
            self.pstatus.place_forget()
            self.patientlname.place_forget()
            self.patientfname.place_forget()
            self.patientage.place_forget()
            self.patientgen.place_forget()
            self.patientaddress.place_forget()
            self.patientwbnum.place_forget()
            self.patientHealthrec.place_forget()
            self.status.place_forget()
            self.nxt_btn.place_forget()
            self.dateAd.place_forget()
            self.dateDis.place_forget()
            self.dateRef.place_forget()
            self.dAd.place_forget()
            self.dDis.place_forget()
            self.dRef.place_forget()
            self.nxtt_btn.place_forget()
            self.addpatient_btn.config(text="ADD PATIENT")
            self.addpatient_btn.config(bg="#093145", fg="WHITE", relief="raised")

    def add_submission(self):


        if len(self.patientlname.get()) == 0 or len(self.patientfname.get()) == 0 or len(
                self.patientage.get()) == 0 or len(self.patientaddress.get()) == 0 or len(
                self.patientHealthrec.get(1.0, "end-1c")) == 0 or len(self.status.get()) == 0:
            messagebox.showerror(title="Adding Failed", message="make sure all required (*) blank is filled!!")
            return True
        else:
            cursor2.execute(
                "INSERT into patients(`pid` ,`Last Name`, `First Name, MI`, `Age`,  `Sex`, `Address`, `Ward #, Bed#`, `Health Record`, `Status`, `Date Admitted`, `Date Discharged`, `Date Reffered` )"
                " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                ('', self.patientlname.get(), self.patientfname.get(), self.patientage.get(), self.patientgen.get(),
                 self.patientaddress.get(), self.patientwbnum.get(), self.patientHealthrec.get(1.0, "end-1c"),
                 self.status.get(), self.dateAd.get(), self.dateDis.get(), self.dateRef.get()))
            dtabse.commit()
            for record in self.tree.get_children():
                self.tree.delete(record)
            self.view_table()
            messagebox.showinfo(title="Add Patient", message="New Patient added successfuly!")
            self.srchlbl.config(text="Click to look for record >>")
            self.patientlname.delete(0, END)
            self.patientfname.delete(0, END)
            self.patientage.delete(0, END)
            self.patientgen.delete(0, END)
            self.patientaddress.delete(0, END)
            self.patientwbnum.delete(0, END)
            self.patientHealthrec.delete("1.0", "end")
            self.status.delete(0, END)
            self.dateAd.delete(0, END)
            self.dateDis.delete(0, END)
            self.dateRef.delete(0, END)


    def del_patient(self):
        self.srchlbl.config(text="Click to look for record >>")
        seeldel = self.tree.selection()[0]
        confirmation = messagebox.askquestion(title="Delete Record",
                                              message="Are you sure you want to delete record? action cannot be undone!",
                                              icon='warning')
        if confirmation == 'yes':
            cursor3.execute("DELETE FROM patients WHERE `pid`= %s", [seeldel])
            dtabse.commit()
            if cursor3.rowcount == 1:
                self.tree.delete(seeldel)
                messagebox.showinfo(title="Delete Record",
                                    message="Record has been deleted")

    def srchbtn1_act(self):
        self.search_btn.place(width=65, height=30, x=305, y=100)
        self.search_btn1.place_forget()
        self.srchlbl.config(text="Click to look for record >>")
        self.winsearch.destroy()

        for record in self.tree.get_children():
            self.tree.delete(record)

        self.view_table()

    def lookup_records(self):
        self.srchlbl.config(text="Click to look for record >>")
        self.winsearch = Toplevel(self.index_scrn)
        self.winsearch.title("Lookup Records")
        self.winsearch.geometry('%dx%d+%d+%d' % (400, 200, self.x, self.y))
        self.winsearch.configure(background="#282828")

        search_frame = LabelFrame(self.winsearch, text="Last Name")
        search_frame.pack(padx=10, pady=10)

        # Add entry box
        self.search = Entry(self.winsearch, font=("arial", 13), borderwidth=5, relief="sunken")
        self.search.pack(pady=20, padx=20)

        # Add button
        self.search_button = Button(self.winsearch, text="Search Records", command=self.search_records)
        self.search_button.pack(padx=20, pady=20)

    def search_records(self):
        if len(self.search.get()) == 0:
            messagebox.showinfo(title="Search failed",
                                message="no input found",
                                icon='warning')
        else:
            self.search_btn.place_forget()
            self.search_btn1.place(width=65, height=30, x=305, y=100)
            get_input = self.search.get()

            self.winsearch.destroy()

            for record in self.tree.get_children():
                self.tree.delete(record)
            self.srchlbl.config(text=get_input)
            cursor.execute(
                "SELECT * FROM patients WHERE `pid` like %s OR `Last Name` like %s OR `First Name, MI`like %s OR `Age`like %s OR  `Sex`like %s OR  `Address`like%s OR `Ward #, Bed#`like%s OR `Health Record`like%s OR  `Status`like%s OR `Date Admitted`like %s OR  `Date Discharged`like%s OR  `Date Reffered`like%s",
                (get_input, get_input, get_input, get_input, get_input, get_input, get_input, get_input, get_input,
                 get_input, get_input, get_input))
            rec = cursor.fetchall()
            for record in rec:
                self.tree.insert(parent='', index='end', iid=record, text='',
                                 values=(
                                     record[0], record[1], record[2], record[3], record[4], record[5],
                                     record[6],
                                     record[7],
                                     record[8], record[9], record[10], record[11]),
                                 )

                break

            else:
                conf = messagebox.showinfo(title="Search failed", message="no record found", icon='warning')
                if conf == 'ok':
                    self.search_btn.place(width=65, height=30, x=305, y=100)
                    self.search_btn1.place_forget()
                    self.srchlbl.config(text="Click to look for record >>")

                    for record in self.tree.get_children():
                        self.tree.delete(record)

                    cursor.execute('SELECT * FROM patients')
                    rec = cursor.fetchall()
                    for record in rec:
                        self.tree.insert(parent='', index='end', iid=str(record), text='',
                                         values=(
                                             record[0], record[1], record[2], record[3], record[4], record[5],
                                             record[6],
                                             record[7],
                                             record[8], record[9], record[10], record[11])
                                         )
                        dtabse.commit()


winblit = Tk()
winblit.iconbitmap(r'C:\Users\Janin Anne\OneDrive\Pictures\icons\icon.ico')
my_system = proj(winblit, 600, 500)
my_system.view_table()

winblit.mainloop()
