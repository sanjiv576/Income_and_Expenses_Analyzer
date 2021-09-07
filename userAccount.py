"""
This module includes information of income and expenses of the user after login,
which stores, manages, updates and accesses the information as the user provides.
"""
from tkinter import *
import sqlite3

myAccount = Tk()
myAccount.title("MY ACCOUNT")
myAccount.iconbitmap("see.ico")
myAccount.geometry("700x600")
myAccount.configure(bg="black")
myAccount.resizable(False, False)


def open_profile_func():
    """
    This function continues to next module by hiding this module and  calling another function within it.
    :return: None
    """
    myAccount.withdraw()
    profile_win = Toplevel()
    profile_win.title("MY PROFILE")
    profile_win.iconbitmap("profile.ico")
    profile_win.geometry("700x600")
    profile_win.configure(bg="black")
    profile_win.resizable(1, 1)

    # frame is added
    topFrame = Frame(profile_win, bg="yellow")
    topFrame.place(x=10, y=10, width=680, height=80)
    bottomFrame = Frame(profile_win, bg="red")
    bottomFrame.place(x=10, y=100, width=680, height=490)
    #  ============================================== headline added ================================================
    heading_img = PhotoImage(file="profile.png")
    heading = Label(topFrame, text="MY PROFILE", font=("Copperplate", 32, "bold"),
                    bg="green", fg="yellow", bd=6, relief=RIDGE)
    heading.pack(side=TOP, fill=X, expand=0)
    heading.config(image=heading_img, compound=LEFT)

    income = 0
    spend = 0
    balance = 0

    # ----------------------- labels are defined -----------------------
    income_label = Label(bottomFrame, text="Income", font=("courier", 25, "bold"), fg="black", bg="red")
    income_label.grid(row=0, column=0, columnspan=1, padx=50, pady=10)

    spend_label = Label(bottomFrame, text="Expenses", font=("courier", 25, "bold"), fg="black",
                         bg="red")
    spend_label.grid(row=0, column=2, columnspan=1, padx=50, pady=10)

    balance_label = Label(bottomFrame, text="Balance", font=("courier", 25, "bold"), fg="black",
                         bg="red")
    balance_label.grid(row=0, column=4, columnspan=1, padx=50, pady=10)

    # ------------------------- values of respective labels are given ------------------------

    income_value = Label(bottomFrame, text="$"+str(income), font=("courier", 25, "bold"), fg="black", bg="red")
    income_value.grid(row=1, column=0, columnspan=1, padx=50, pady=10)

    spend_value = Label(bottomFrame, text="$"+str(spend), font=("courier", 25, "bold"), fg="black",
                        bg="red")
    spend_value.grid(row=1, column=2, columnspan=1, padx=50, pady=10)

    balance_value = Label(bottomFrame, text="$"+str(balance), font=("courier", 25, "bold"), fg="black",
                          bg="red")
    balance_value.grid(row=1, column=4, columnspan=1, padx=50, pady=10)

    # ------------------------------------ Basic details of the user-------------------------------------
    connect_me = sqlite3.connect("Accounts_details_holder.db")
    # creating a cursor
    cur = connect_me.cursor()
    cur.execute("SELECT first_name, last_name, gender, contact FROM registration_details_holder")
    fetch = cur.fetchall()
    print(fetch)
    profile_win.mainloop()

def open_income_func():
    """
    This function continues to next module by hiding this module and  calling another function within it.
    :return: None
    """
    myAccount.withdraw()





def open_setting_func():
    """
    This function continues to next module by hiding this module and  calling another function within it.
    :return: None
    """
    myAccount.withdraw()


#  ============================================== headline added ================================================
heading_img = PhotoImage(file="incomeAndExpenditure.png")
heading = Label(myAccount, text="INCOME AND EXPENSES ANALYZER", font=("Copperplate", 32, "bold"),
                bg="silver", bd=6, relief=RIDGE)
heading.pack(side=TOP, fill=X, expand=0)
heading.config(image=heading_img, compound=LEFT)

# ============================================== different frames are added ===============================
center_frame = Frame(myAccount, bg="#7C7474", bd=6, relief=SOLID)
center_frame.place(x=180, y=70, width=330, height=500)





# =================================== Buttons with events are defined in left_frame  ============================

myProfile_button = Button(center_frame, text="My Profile", font=("Times New Roman", 24, "bold"), command=open_profile_func,
                          highlightbackground="green")
myProfile_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

income_button = Button(center_frame, text="My Income", font=("Times New Roman", 24, "bold"), command=open_income_func,
                       highlightbackground="green", fg="black")
income_button.pack(padx=54, pady=20, ipadx=4, ipady=6)


setting_button = Button(center_frame, text="My Setting", font=("Times New Roman", 24, "bold"), command=open_setting_func,
                        highlightbackground="green")
setting_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

logout_button = Button(center_frame, text="Log Out", font=("Times New Roman", 24, "bold"),
                        highlightbackground="green")
logout_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

myAccount.mainloop()
