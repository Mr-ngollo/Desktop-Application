import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql

class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System | Designed by ngollo | OOP-WORK")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Create a Label for the title
        title=Label(self.root, 
                       text="Employee Payroll Management System", 
                       font=("times new roman", 30, "bold"), 
                       fg="white",
                       anchor="w",
                       padx=10, 
                       bg="brown").place(x=0, y=0, relwidth=1)
        
        # ============================================= the first frame on the right side ============================================================= 
        # =============================== Variables ====================================================

        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_hr_location = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_proof_id = StringVar() # ==== card =========
        self.var_contact = StringVar()
        self.var_status = StringVar()
        self.var_experience = StringVar()


        Frame1 = Frame(self.root,
                       bd=5,
                       bg="white", 
                       relief=RIDGE)
        Frame1.place(x=10, 
                     y=70, 
                     width=750, 
                     height=600)
        title2 = Label(Frame1, 
                       text="Employee Details", 
                       font=("times new roman", 20), 
                       fg="black",
                       anchor="w",
                       padx=10, 
                       bg="lightgray").place(x=0, y=0, relwidth=1)
        lbl_code = Label(Frame1, 
                       text="Employee Code", 
                       font=("times new roman", 20), 
                       fg="black",
                       bg="white").place(x=10, y=70)
        txt_code = Entry(Frame1, 
                       font=("times new roman", 15),
                       textvariable=self.var_emp_code,  
                       fg="black",
                       bg="lightyellow").place(x=220, y=74, width=200)
        btn_search = Button(Frame1,
                       text="Search", 
                       font=("times new roman", 15), 
                       fg="black",
                       bg="gray").place(x=440, y=72, height=30)

                      #  the first row 
        lbl_designation = Label(Frame1, 
                       text="Designation:", 
                       font=("times new roman", 20), 
                       fg="black", 
                       bg="white").place(x=10, y=120)
        txt_designation = Entry(Frame1, 
                       font=("times new roman", 15),
                       textvariable=self.var_designation, 
                       fg="black",
                       bg="lightyellow").place(x=170, y=125, width=200)
        lbl_doj = Label(Frame1, 
                       text="D.O.J:", 
                       font=("times new roman", 20), 
                       fg="black", 
                       bg="white").place(x=390, y=120)
        txt_doj = Entry(Frame1, 
                       font=("times new roman", 15), 
                       textvariable=self.var_doj,
                       fg="black",
                       bg="lightyellow").place(x=520, y=125)

                      #  the second row 
        lbl_name = Label(Frame1, 
                       text="Name:", 
                       font=("times new roman", 20), 
                       fg="black", 
                       bg="white").place(x=10, y=160)
        txt_name = Entry(Frame1, 
                       font=("times new roman", 15),
                       textvariable=self.var_name, 
                       fg="black",
                       bg="lightyellow").place(x=170, y=165, width=200)
        lbl_dob = Label(Frame1, 
                       text="D.O.B:", 
                       font=("times new roman", 20), 
                       fg="black", 
                       bg="white").place(x=390, y=160)
        txt_dob = Entry(Frame1, 
                       font=("times new roman", 15),
                       textvariable=self.var_dob, 
                       fg="black",
                       bg="lightyellow").place(x=520, y=165)

                      #  the third row 
        lbl_age = Label(Frame1, 
                       text="Age:", 
                       font=("times new roman", 20), 
                       fg="black", 
                       bg="white").place(x=10, y=200)
        txt_age = Entry(Frame1, 
                       font=("times new roman", 15),
                       textvariable=self.var_age, 
                       fg="black",
                       bg="lightyellow").place(x=170, y=205, width=200)
        lbl_experience = Label(Frame1, 
                       text="Experience:", 
                       font=("times new roman", 18), 
                       fg="black", 
                       bg="white").place(x=390, y=200)
        txt_experience = Entry(Frame1, 
                       font=("times new roman", 15),
                       textvariable=self.var_experience, 
                       fg="black",
                       bg="lightyellow").place(x=520, y=205)
        
        
                      #  the forth row 
        lbl_gender = Label(Frame1, 
                       text="Gender:", 
                       font=("times new roman", 20), 
                       fg="black", 
                       bg="white").place(x=10, y=240)
        txt_gender = Entry(Frame1, 
                       font=("times new roman", 15),
                       textvariable=self.var_gender, 
                       fg="black",
                       bg="lightyellow").place(x=170, y=245, width=200)
        lbl_proof_id = Label(Frame1, 
                       text="Proof ID:", 
                       font=("times new roman", 20), 
                       fg="black", 
                       bg="white").place(x=390, y=240)
        txt_proof_id = Entry(Frame1, 
                       font=("times new roman", 15),
                       textvariable=self.var_proof_id, 
                       fg="black",
                       bg="lightyellow").place(x=520, y=245)
        
        
                      #  the fifth row 
        lbl_email = Label(Frame1, 
                       text="Email:", 
                       font=("times new roman", 20), 
                       fg="black", 
                       bg="white").place(x=10, y=280)
        txt_email = Entry(Frame1, 
                       font=("times new roman", 15),
                       textvariable=self.var_email, 
                       fg="black",
                       bg="lightyellow").place(x=170, y=285, width=200)
        lbl_contact_no = Label(Frame1, 
                       text="Contact No:", 
                       font=("times new roman", 18), 
                       fg="black", 
                       bg="white").place(x=390, y=280)
        txt_contact_no = Entry(Frame1, 
                       font=("times new roman", 15),
                       textvariable=self.var_contact, 
                       fg="black",
                       bg="lightyellow").place(x=520, y=285)
                           
                      #  the sixth row 
        lbl_hired = Label(Frame1, 
                       text="Hired Location:", 
                       font=("times new roman", 18), 
                       fg="black", 
                       bg="white").place(x=10, y=320)
        txt_hired = Entry(Frame1, 
                       font=("times new roman", 15),
                       textvariable=self.var_hr_location, 
                       fg="black",
                       bg="lightyellow").place(x=170, y=325, width=200)
        lbl_status = Label(Frame1, 
                       text="Status:", 
                       font=("times new roman", 20), 
                       fg="black", 
                       bg="white").place(x=390, y=320)
        txt_status = Entry(Frame1, 
                       font=("times new roman", 15),
                       textvariable=self.var_status, 
                       fg="black",
                       bg="lightyellow").place(x=520, y=325)

                       # the seventh row
        lbl_address = Label(Frame1, 
                       text="Address:", 
                       font=("times new roman", 20), 
                       fg="black", 
                       bg="white").place(x=10, y=360)
        self.txt_address = Text(Frame1, 
                       font=("times new roman", 15), 
                       fg="black",
                       bg="lightyellow")
        self.txt_address.place(x=170, y=365, width=555, height=150)

        
        # ===================================== the second frame on the right side ======================================================
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_t_days = StringVar()
        self.var_abscent = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_net_salary = StringVar()
        
        Frame2 = Frame(self.root,
                       bd=5,
                       bg="white", 
                       relief=RIDGE)
        Frame2.place(x=770, 
                     y=70, 
                     width=500, 
                     height=300)

        title3 = Label(Frame2, 
                       text="Employee Salary Details", 
                       font=("times new roman", 20), 
                       fg="black",
                       anchor="w",
                       padx=10, 
                       bg="lightgray").place(x=0, y=0, relwidth=1)

                       # the first row
        lbl_month = Label(Frame2, 
                       text="Month:", 
                       font=("times new roman", 15), 
                       fg="black",
                       bg="white").place(x=10, y=62)
        txt_month = Entry(Frame2, 
                       font=("times new roman", 14),
                       textvariable=self.var_month, 
                       fg="black",
                       bg="lightyellow").place(x=75, y=60, width=80)

        lbl_year = Label(Frame2, 
                       text="Year:", 
                       font=("times new roman", 15), 
                       fg="black",
                       bg="white").place(x=165, y=62)
        txt_year = Entry(Frame2, 
                       font=("times new roman", 14),
                       textvariable=self.var_year, 
                       fg="black",
                       bg="lightyellow").place(x=225, y=60, width=60)

        lbl_salary = Label(Frame2, 
                       text="B-Salary:", 
                       font=("times new roman", 15), 
                       fg="black",
                       bg="white").place(x=298, y=62)
        txt_salary = Entry(Frame2, 
                       font=("times new roman", 14),
                       textvariable=self.var_salary, 
                       fg="black",
                       bg="lightyellow").place(x=390, y=60, width=90)

                      #  the second row 
        lbl_days = Label(Frame2, 
                       text="Total Days:", 
                       font=("times new roman", 15), 
                       fg="black", 
                       bg="white").place(x=10, y=112)
        txt_days = Entry(Frame2, 
                       font=("times new roman", 15), 
                       textvariable=self.var_t_days,
                       fg="black",
                       bg="lightyellow").place(x=120, y=107, width=100)
        lbl_abscent = Label(Frame2, 
                       text="Abscents:", 
                       font=("times new roman", 15), 
                       fg="black", 
                       bg="white").place(x=260, y=112)
        txt_abscent = Entry(Frame2, 
                       font=("times new roman", 15),
                       textvariable=self.var_abscent, 
                       fg="black",
                       bg="lightyellow").place(x=350, y=107, width=100)

                    #  the third row 
        lbl_medical = Label(Frame2, 
                       text="Medical:", 
                       font=("times new roman", 15), 
                       fg="black", 
                       bg="white").place(x=10, y=152)
        txt_medical = Entry(Frame2, 
                       font=("times new roman", 15),
                       textvariable=self.var_medical, 
                       fg="black",
                       bg="lightyellow").place(x=120, y=150, width=100)
        lbl_fund = Label(Frame2, 
                       text="P-Fund:", 
                       font=("times new roman", 15), 
                       fg="black", 
                       bg="white").place(x=260, y=152)
        txt_fund = Entry(Frame2, 
                       font=("times new roman", 15),
                       textvariable=self.var_pf, 
                       fg="black",
                       bg="lightyellow").place(x=350, y=150, width=100)

                      #  the forth row 
        lbl_convence = Label(Frame2, 
                       text="Convence:", 
                       font=("times new roman", 15), 
                       fg="black", 
                       bg="white").place(x=10, y=199)
        txt_convence = Entry(Frame2, 
                       font=("times new roman", 15),
                       textvariable=self.var_convence, 
                       fg="black",
                       bg="lightyellow").place(x=120, y=197, width=100)
        lbl_net_salary = Label(Frame2, 
                       text="N-Salary:", 
                       font=("times new roman", 15), 
                       fg="black", 
                       bg="white").place(x=260, y=199)
        txt_net_salary = Entry(Frame2, 
                       font=("times new roman", 15),
                       textvariable=self.var_net_salary, 
                       fg="black",
                       bg="lightyellow").place(x=350, y=197, width=100)        
        
                      #  the fifth row 
        btn_calculate = Button(Frame2,
                       text="Calculate", 
                       font=("times new roman", 15),
                       command=self.calculate,
                       fg="black",
                       bg="yellow").place(x=50, y=240, height=30, width=120)
        btn_save = Button(Frame2,
                       text="Save",
                       command=self.add, 
                       font=("times new roman", 15), 
                       fg="white",
                       bg="green").place(x=190, y=240, height=30, width=120)
        btn_clear = Button(Frame2,
                       text="Clear", 
                       font=("times new roman", 15), 
                       fg="black",
                       bg="red").place(x=330, y=240, height=30, width=120)   
        
          # ================================ the third frame on the left side down ==================================================================
        Frame3 = Frame(self.root,
                       bd=5,
                       bg="white", 
                       relief=RIDGE)
        Frame3.place(x=770, 
                     y=380, 
                     width=500, 
                     height=288)

          # ================================ Calculator Frame ======================================================
        self.var_txt = StringVar()
        self.var_operator = ""
        def btn_click(num):
          self.var_operator = self.var_operator + str(num)
          self.var_txt.set(self.var_operator)

        # defining the function for calculating results
        def result():
          res = str(eval(self.var_operator))
          self.var_txt.set(res)
          self.var_operator = ""

        # define the function for clearing the results
        def clear():
          self.var_txt.set("")
          self.var_operator = ""
        
        Cal_Frame = Frame(Frame3,
                          bd=2,
                          relief=RIDGE,
                          bg="white")
        Cal_Frame.place(x=2, y=2, width=246, height=300)
        txt_Result = Entry(Cal_Frame,
                          bg="lightyellow",
                          textvariable=self.var_txt, 
                          font=("times new roman", 20, "bold",), justify=RIGHT).place(x=0, y=0, relwidth=1, height=40)
        
        # row 1
        btn_7 = Button(Cal_Frame, 
                        text="7",
                        command=lambda:btn_click(7),
                        fg="white",
                        bg="gray", 
                        font=("times new roman", 15, "bold")).place(x=0, y=42, w=60, h=60)
        btn_8 = Button(Cal_Frame, 
                        text="8", 
                        command=lambda:btn_click(8),
                        fg="white",
                        bg="gray", 
                        font=("times new roman", 15, "bold")).place(x=61, y=42, w=60, h=60)
        btn_9 = Button(Cal_Frame, 
                        text="9",
                        command=lambda:btn_click(9), 
                        fg="white",
                        bg="gray", 
                        font=("times new roman", 15, "bold")).place(x=122, y=42, w=60, h=60)
        btn_div = Button(Cal_Frame, 
                        text="/", 
                        command=lambda:btn_click("/"),
                        fg="white",
                        bg="orange",
                        font=("times new roman", 15, "bold")).place(x=183, y=42, w=60, h=60)

        # row 2
        btn_4 = Button(Cal_Frame, 
                        text="4",
                        command=lambda:btn_click(4),
                        bg="gray", 
                        fg="white", 
                        font=("times new roman", 15, "bold")).place(x=0, y=102, w=60, h=60)
        btn_5 = Button(Cal_Frame, 
                        text="5",
                        command=lambda:btn_click(5), 
                        fg="white",
                        bg="gray", 
                        font=("times new roman", 15, "bold")).place(x=61, y=102, w=60, h=60)
        btn_6 = Button(Cal_Frame, 
                        text="6",
                        command=lambda:btn_click(6), 
                        bg="gray", 
                        fg="white",
                        font=("times new roman", 15, "bold")).place(x=122, y=102, w=60, h=60)
        btn_mult = Button(Cal_Frame, 
                        text="*",
                        command=lambda:btn_click("*"), 
                        fg="white",
                        bg="orange",
                        font=("times new roman", 15, "bold")).place(x=183, y=102, w=60, h=60)

        # row 3
        btn_1 = Button(Cal_Frame, 
                        text="1", 
                        command=lambda:btn_click(1),
                        bg="gray", 
                        fg="white",
                        font=("times new roman", 15, "bold")).place(x=0, y=162, w=60, h=60)
        btn_2 = Button(Cal_Frame, 
                        text="2",
                        command=lambda:btn_click(2), 
                        bg="gray", 
                        fg="white",
                        font=("times new roman", 15, "bold")).place(x=61, y=162, w=60, h=60)
        btn_3 = Button(Cal_Frame, 
                        text="3",
                        command=lambda:btn_click(3),
                        bg="gray",  
                        fg="white",
                        font=("times new roman", 15, "bold")).place(x=122, y=162, w=60, h=60)
        btn_min = Button(Cal_Frame, 
                        text="-",
                        command=lambda:btn_click("-"), 
                        fg="white",
                        bg="orange",
                        font=("times new roman", 15, "bold")).place(x=183, y=162, w=60, h=60)

        # row 4
        btn_0 = Button(Cal_Frame, 
                        text="0",
                        command=lambda:btn_click(0),
                        bg="black",
                        fg="white", 
                        font=("times new roman", 15, "bold")).place(x=0, y=222, w=60, h=60)
        btn_clear = Button(Cal_Frame, 
                        text="C",
                        command=clear,
                        bg="black",
                        fg="white",
                        font=("times new roman", 15, "bold")).place(x=61, y=222, w=60, h=60)
        btn_sum = Button(Cal_Frame, 
                        text="+", 
                        command=lambda:btn_click("+"),
                        bg="black", 
                        fg="white",
                        font=("times new roman", 15, "bold")).place(x=122, y=222, w=60, h=60)
        btn_equal = Button(Cal_Frame, 
                        text="=",
                        command=result,
                        fg="white", 
                        bg="orange",
                        font=("times new roman", 15, "bold")).place(x=183, y=222, w=60, h=60)


        # =========================== the salary Frame =========================
        salary_Frame = Frame(Frame3,
                          bd=2,
                          relief=RIDGE,
                          bg="white")
        salary_Frame.place(x=250, y=2, width=240, height=300)

        salary_title = Label(salary_Frame, 
                       text="Salary Receipt", 
                       font=("times new roman", 20), 
                       fg="black",
                       anchor="w",
                       padx=10, 
                       bg="lightgray").place(x=0, y=0, relwidth=1)
        salary_Frame2 = Frame(salary_Frame, 
                              bg="white", 
                              bd=2, relief=RIDGE)
        salary_Frame2.place(x=0, y=30, relwidth=1, height=210)

        scroll_y = Scrollbar(salary_Frame2, 
                              orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_salary_receipt = Text(salary_Frame2, 
                                      font=("times new roman", 15),
                                      yscrollcommand=scroll_y.set, 
                                      bg="lightyellow")
        self.txt_salary_receipt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)  

        btn_print = Button(salary_Frame,
                       text="Print", 
                       font=("times new roman", 20), 
                       fg="black",
                       bg="orange").place(x=120, y=250, height=30, width=100)

        self.check_connection()

  # ================== All of the functions start here ==================================
    def add(self):
                if self.var_emp_code.get() =="" or self.var_net_salary.get() =="" or self.var_name.get() =="":
                  messagebox.showerror("Error","Employee details are required")
                else:
                  try:
                      con = pymysql.connect(host="localhost", user="root", password="", db="pms")
                      cur = con.cursor()
                      cur.execute("SELECT * FROM emp_salary where em_id=%s", (self.var_emp_code.get()))
                      row = cur.fetchone()
                      # print(rows)
                      if row != None:
                        messagebox.showerror("Error", "This Employee ID is already available in our records, try again with another employee ID", parent = self.root)
                      else:
                        cur.execute("insert into emp_salary values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                        (
                          self.var_emp_code.get(),
                          self.var_designation.get(),
                          self.var_name.get(),
                          self.var_age.get(),
                          self.var_gender.get(),
                          self.var_email.get(),
                          self.var_hr_location.get(),
                          self.var_doj.get(),
                          self.var_dob.get(),
                          self.var_experience.get(),
                          self.var_proof_id.get(),
                          self.var_contact.get(),
                          self.var_status.get(),
                          self.txt_address.get("1.0", END),
                          self.var_month.get(),
                          self.var_year.get(),
                          self.var_salary.get(),
                          self.var_t_days.get(),
                          self.var_abscent.get(),
                          self.var_medical.get(),
                          self.var_pf.get(),
                          self.var_convence.get(),
                          self.var_net_salary.get(),
                          "receipt"
                      )
                      )
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success", "Record Added Successfully") 
                  except Exception as ex:
                      messagebox.showerror("Error", f'Error due to: {str(ex)}')
    def calculate(self):
      if self.var_month.get() == "" or self.var_year.get() =="" or self.var_salary.get() == "" or self.var_t_days.get() == "" or self.var_abscent.get() == "" or self.var_medical.get() == "" or self.var_pf.get() == "" or self.var_convence.get() == "":
        messagebox.showerror("Errorr", "All fields are required")
      else :
        per_day = int(self.var_salary.get()) / int(self.var_t_days.get())
        work_day = int(self.var_t_days.get()) - int(self.var_abscent.get())
        sal_ = per_day * work_day
        deduct = int(self.var_medical.get()) + int(self.var_pf.get())
        addition = int(self.var_convence.get())
        net_sal = sal_ - deduct + addition 
        self.var_net_salary.set(str(round(net_sal,2)))

    def check_connection(self):
        try:
           con = pymysql.connect(host="localhost", user="root", password="", db="pms")
           cur = con.cursor()
           cur.execute("SELECT * FROM emp_salary")
           rows = cur.fetchall()
           print(rows)

        except Exception as ex:
          messagebox.showerror("Error", f'Error due to: {str(ex)}')



# Create the Tkinter root window
root = Tk()

# Initialize the EmployeeSystem with the root window
app = EmployeeSystem(root)

# Run the main event loop to display the GUI
root.mainloop()
