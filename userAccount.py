"""
This module includes information of income and expenses of the user after login,
which stores, manages, updates and accesses the information as the user provides.
"""
from tkinter import *
def open_userAccount():
    myAccount = Tk()
    myAccount.title("MY ACCOUNT")
    # remaining to change icon
    myAccount.iconbitmap("login.ico")
    myAccount.geometry("1000x700")
    myAccount.configure(bg="black")
    myAccount.resizable(False, False)

    #  ============================================== headline added ================================================
    heading_img = PhotoImage(file="incomeAndExpenditure.png")
    heading = Label(myAccount, text="INCOME AND EXPENSES ANALYZER", font=("Copperplate", 32, "bold"),
                    bg="silver", bd=6, relief=RIDGE)
    heading.pack(side=TOP, fill=X, expand=0)
    heading.config(image=heading_img, compound=LEFT)

    # ============================================== different frames are added =========================================
    left_frame = Frame(myAccount, bg="#7C7474", bd=6, relief=SOLID)
    left_frame.place(x=20, y=70, width=250, height=600)

    right_profile_frame = Frame(myAccount, bg="#7C7474", bd=9, relief=SOLID)
    right_profile_frame.place(x=300, y=70, width=670, height=600)



    # ========================== functions with events are defined as buttons are clicked on ===========================
    def myProfile():
        print("My profile")

        myProfile_label = Label(right_profile_frame, text="My Profile", bd=4, bg="yellow", fg="black",
                                font=("Copperplate", 35, "bold"), relief=GROOVE)
        myProfile_label.pack(fill=X, side=TOP)

        myProfile_frame = Frame(right_profile_frame, bg="white")
        myProfile_frame.place(x=10, y=55, width=635, height=518)

    def income():
        print("income")
        income_label = Label(right_profile_frame, text="My Income", bd=4, bg="yellow", fg="black",
                                font=("Copperplate", 35, "bold"), relief=GROOVE)
        income_label.pack(fill=X, side=TOP)

        income_frame = Frame(right_profile_frame, bg="white")
        income_frame.place(x=10, y=55, width=635, height=518)
        right_profile_frame.place_forget()



    # =================================== Buttons with events are defined in left_frame  ============================

    myProfile_button = Button(left_frame, text="My Profile", font=("Times New Roman", 24, "bold"), command=myProfile,
                              highlightbackground="green")
    myProfile_button.grid(row=0, column=0, padx=54, pady=20, ipadx=4, ipady=6)

    income_button = Button(left_frame, text="Income", font=("Times New Roman", 24, "bold"), command=income,
                           highlightbackground="green", fg="black")
    income_button.grid(row=1, column=0, padx=54, pady=20, ipadx=4, ipady=6)

    expenses_button = Button(left_frame, text="Expenses", font=("Times New Roman", 24, "bold"),
                             highlightbackground="green", fg="black")
    expenses_button.grid(row=2, column=0, padx=54, pady=20, ipadx=4, ipady=6)

    setting_button = Button(left_frame, text="Setting", font=("Times New Roman", 24, "bold"),
                            highlightbackground="green")
    setting_button.grid(row=3, column=0, padx=54, pady=20, ipadx=4, ipady=6)

    logout_button = Button(left_frame, text="Log Out", font=("Times New Roman", 24, "bold"),
                            highlightbackground="green")
    logout_button.grid(row=4, column=0, padx=54, pady=20, ipadx=4, ipady=6)

    myAccount.mainloop()
