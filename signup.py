"""
This module accepts username and password to signup.
"""
# for GUI design
from tkinter import *
# for messagebox
from tkinter import messagebox
# for database
import sqlite3
# for Treeview
from tkinter import ttk
# for checking whether a file is existing or not
import os.path
# now allowing to access variables and functions which interact strongly with a python interpreter (this is optional)
import sys
# for OTP generation
import random

# using third party library , for installation ===> pip install tkcalendar
from tkcalendar import *

# using third party library, for installation ===> pip install twilio
from twilio.rest import Client

signUp = Tk()
signUp.title("SIGNUP")
# resolution of the window changes
signUp.geometry("980x700")
# inserting icon
signUp.iconbitmap("login.ico")
signUp.configure(bg="white")
# allowing to the user to maximize the window resolution
signUp.resizable(1, 1)
# ------------------------database use for Registration Form begins from here------------------
connector = sqlite3.connect("Accounts_details_holder.db")
cur = connector.cursor()
"""
# creating a table
cur.execute('''CREATE TABLE  IF NOT EXISTS registration_details_holder(
                                                 first_name text,
                                                 last_name text,
                                                 gender text,
                                                 contact integer,
                                                 username text,
                                                 password text)''')
print("Table has been created successfully.")
"""

# ------------------------ different functions for database use begins from here------------------

# Note : 572 x 490 pixel image
left_img = PhotoImage(file="login_img.png")
img_label = Label(signUp, image=left_img)
img_label.place(x=40, y=30)

my_frame = Frame(signUp)
# resolution of frame depends on the size of left_img image because of using place geometry.
my_frame.place(x=640, y=30, width=300, height=650)
# adding blue background color i.e #6964EE in the frame
my_frame.config(bg="#6964EE")

def digit_checker(to_be_check):
    """
    This function accepts data from the users and checks whether provided data are digit or not. If yes, it returns True
    if no, it returns False
    :param to_be_check: int
    :return:Boolean
    """
    length_contact = len(to_be_check.get())
    # knowing the length of inserted data to return Boolean value(i.e True), if all inserted data are digit
    adder = 0
    #print(length_contact)
    for check in to_be_check.get():
        if check.isdigit():
            adder += 1
            #print("adder", adder)
            inserted_info = True

            if length_contact == adder:
                return inserted_info

        else:
            inserted_info = False
            return inserted_info
            break


def clear_entry():
    """
    This function clears username and password entries of signup page.
    :return: None
    """
    username_entry.delete(0, END)
    password_entry_signup.delete(0, END)


# creating a new window for registration as clicked on 'Don't have an account ?' button
# -----------------------------------Coding for Registration Form starts ----------------------------------
vacant_row = 0
# for OTP generation
otp = ""
def create_my_account():
    """
    This accepts user's full name, gender, username and password as string to create an account for official use.
    :return to : login page
    """
    # hiding signup window
    signUp.withdraw()
    # new window is created and displayed from here
    register = Toplevel()
    register.title("Registration Form")
    register.iconbitmap("agree_0.ico")
    register.geometry("740x800")
    # not allowing to maximize the Registration Form
    register.resizable(0, 0)
    register.configure(bg="#CDC8B1")  # #CDC8B1 = silkcorn color

    # =================================== GUI of Registration Form begins =====================================
    # frame is created to maintain buttons and labels in a systematic arrangement
    my_frame = Frame(register, bg="#CDC8B1")
    my_frame.pack()
    # function for showing  messages as clicked on 'SUBMIT' button
    def show_message():
        """
        This function alerts the user if he/she gives invalid details or leaves entries empty.
        :return: None
        """
        selected_gender = indicator.get()
        #print(selected_gender)
        # checking whether entered information in 'Contact' entry are digits or not
        result = digit_checker(contact_entry)
        #print("Contact_entry result is : ", result)

        # now checking length of the contact is equal to ten or not
        contact_length = len(str(contact_entry.get()))
        #print(contact_length)

        if f_nam_entry.get() == "" and l_nam_entry.get() == "" and user_name_entry.get() == "" and contact_entry.get() == "" and \
                password_entry.get() == "" and conf_password_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill all boxes.")

        elif f_nam_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill first name box.")

        elif l_nam_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill last name box.")

        elif selected_gender == "Choose options":
            messagebox.showerror("Invalid", "Please, choose gender.")

        elif contact_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please, fill contact box.")

        elif result is False:
            messagebox.showerror("INVALID!", "Please, insert numbers in contact box.")

        elif contact_length < 10:
            messagebox.showwarning("Wrong Entry", "Digits of contact number is lesser than 10.")

        elif contact_length > 10:
            messagebox.showwarning("Wrong Entry", "Digits of contact number is greater than 10.")

        elif user_name_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill  username box.")

        elif password_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill  password box.")

        elif conf_password_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill  confirm password box.")

        # checking password and confirm password match or not
        elif conf_password_entry.get() != password_entry.get():
            messagebox.showerror("INCORRECT PASSWORD! ",
                                 "Password and Confirm password do not match. Please, enter again.")

        else:
            messagebox.showinfo("OTP Sent",
                                "OTP has been sent to the provided contact number. Please, check on your mobile phone.")

            otp_win = Toplevel()
            otp_win.geometry("600x400")


            def for_verify():
                """
                This function checks whether inserted OTP code is correct or not,
                if correct, it allows to create account successfully.
                :return: None
                """
                if user_otp.get() == otp:
                    messagebox.showinfo("OTP Verified", "Your account has been verified.")
                    user_otp.delete(0, END)

                    messagebox.showinfo("Account Created",
                                        "Congratulation! Your account has been created successfully.")

                    # Insertion database is here

                    # -------------All details are inserted into the table of Database i.e registration_details----
                    connect_me = sqlite3.connect("Accounts_details_holder.db")
                    cu = connect_me.cursor()
                    # inserting details into the table
                    cu.execute("INSERT INTO registration_details_holder VALUES(:f_name, :l_name, :gender_type,"
                               ":contact_num, :username_entered, :password_entered)", {
                                   'f_name': f_nam_entry.get(),
                                   'l_name': l_nam_entry.get(),
                                   'gender_type': selected_gender,
                                   'contact_num': contact_entry.get(),
                                   'username_entered': user_name_entry.get(),
                                   'password_entered': password_entry.get()
                               })

                    # filling all entry fields or not
                    print("Information are inserted successfully.")
                    #messagebox.showinfo("Records insertion", "Information have been inserted successfully too.")
                    connect_me.commit()
                    connect_me.close()

                    # clearing the entry fields after inserting info
                    user_name_entry.delete(0, END)
                    l_nam_entry.delete(0, END)
                    # selected_gender.delete(0, END)
                    contact_entry.delete(0, END)
                    user_name_entry.delete(0, END)
                    password_entry.delete(0, END)

                    # revealing Signup window after creating the account for login
                    signUp.deiconify()
                    # quitting OTP window
                    otp_win.destroy()
                    # quitting the Registration Form window after successfully creating account.
                    register.destroy()

                elif user_otp.get() != otp:
                    messagebox.showerror("No verification", "Provided OTP is incorrect. Try again or resend the code.")
                    user_otp.delete(0, END)

                else:
                    pass

            def send_code():
                """
                This function generates 6-digit random OTP code for verification
                :return: None
                """
                try:
                    global otp
                    otp = ""
                    for i in range(4):
                        otp += str(random.randint(0, 9))

                    print("Your OTP is :", otp)
                    # account_sid and auth_token are given by twilio website after registration on there
                    account_sid = 'AC29bd93b06b1cb826f1016e60caf42404'
                    auth_token = '34cb83be0bf2d2fbb29b6636fd4cfe2f'
                    client = Client(account_sid, auth_token)
                    # Note: for verification --> contact number of Nepal country is only valid so, +977 is
                    message_send = client.messages.create(
                        body="Dear "+str(f_nam_entry.get())+","+"Your OTP code is: " + str(otp) + "\n From Income and Expenses Analyzer",
                        from_="+18787887310",
                        to="+977" + str(contact_entry.get())
                    )

                except (AttributeError, NameError, SyntaxError, TypeError, ValueError, BaseException) as guide_msg:
                    print(guide_msg)
                    print(type(guide_msg))


            def resend_code():
                """
                This function resends OTP code by calling send_code after showing message.
                :return: None
                """
                messagebox.showinfo("OTP Resent", "New OTP has been sent. Please, check on your mobile phone.")
                send_code()


            send_code()
            info_label = Label(otp_win, text="Enter your OTP code for verification ", font=("times", 24, "bold"))
            info_label.pack(padx=20, pady=20)
            user_otp = Entry(otp_win, font=("times", 20, "italic"), bd=5, relief=SUNKEN)
            user_otp.pack(padx=20, pady=20)

            send_btn = Button(otp_win, text="Verify", font=("times", 24, "bold"), command=for_verify,
                              highlightbackground="green")
            send_btn.pack(padx=20, pady=20, ipadx=8, ipady=8)

            resend_btn = Button(otp_win, text="Resend Code", font=("times", 24, "bold"), command=resend_code,
                                highlightbackground="yellow")
            resend_btn.pack(padx=20, pady=20, ipadx=8, ipady=8)
            otp_win.mainloop()


    # function to show messages for exit window as clicked on 'EXIT' button.
    def show_quit():
        """
        This function asks confirmation from the user to exit the Registration Form window.
        :return: None
        """
        user_respond = messagebox.askokcancel("Warning !", "Do you want to quit ? ")
        if user_respond == 1:
            register.destroy()


    # function for empty labels
    def empty_row():
        """
        This function creates empty rows for a proper arrangement of each entry for a better look.
        :return: integer
        """
        # changing value of vacant_row in each call/invoking the function
        global vacant_row
        if vacant_row <= 30:
            empty_label = Label(my_frame, text="", bg="#CDC8B1")
            empty_label.grid(row=vacant_row)
            vacant_row += 2
            return vacant_row


    # function created to go back to the previous window as clicked on '<<<' button.
    def previous_window():
        """
        This returns Registration Form window to previous Signup window.
        :return: None
        """
        clear_entry()
        """
        username_entry.delete(0, END)
        password_entry_signup.delete(0, END)
        """
        global vacant_row
        # assigning the value of vacant_row as 0 because after visiting Registration Form the value of it changes so,
        # its value is made 0 to execute vacant_row <= 30 again from 0
        vacant_row = 0
        # revealing Signup window
        signUp.deiconify()
        # hiding Registration Form
        register.destroy()


    # --------------------------------------------labels are defined-------------------------------------------
    try:
        empty_row()
        heading_label = Label(my_frame, text="CREATE AN ACCOUNT", font=("copperplate", 32, 'bold'),
                              bg="#CDC8B1", fg="green")
        heading_label.grid(row=1, column=1)
        # rows = 2, 3 are left for empty for future use
        empty_row()
        f_name = Label(my_frame, text="First Name :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
        f_name.grid(row=3, column=0)
        empty_row()
        l_name = Label(my_frame, text="Last Name :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
        l_name.grid(row=5, column=0)
        empty_row()
        gender_label = Label(my_frame, text="Gender :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
        gender_label.grid(row=7, column=0)
        empty_row()
        contact_label = Label(my_frame, text="Contact :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
        contact_label.grid(row=9, column=0)
        empty_row()
        user_name = Label(my_frame, text="Username :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
        username = StringVar()
        #print(type(username))
        user_name.grid(row=11, column=0)
        empty_row()
        password_label = Label(my_frame, text="Password :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
        password = StringVar()
        password_label.grid(row=13, column=0)
        empty_row()
        conf_password_label = Label(my_frame, text="Confirm Password :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
        confirm_password = StringVar()
        conf_password_label.grid(row=15, column=0)
        empty_row()
    except (AttributeError, NameError, SyntaxError, TypeError, ValueError) as guide:
        print(guide.__class__)
        print(guide)
    finally:
        # --------------------------------------------buttons are defined along with events-----------------------
        submit_button = Button(my_frame, text="SUBMIT", highlightbackground="green", command=show_message,
                               font=("Century Gothic", 24, 'bold'))
        submit_button.grid(row=17, column=1, ipadx=18, ipady=3)
        empty_row()
        exit_button = Button(my_frame, text="EXIT", highlightbackground="red", command=show_quit,
                             font=("Century Gothic", 24, 'bold'))
        exit_button.grid(row=19, column=1, ipadx=18, ipady=3, rowspan=2)
        empty_row()
        previous_window_btn = Button(my_frame, text="<<<", highlightbackground="red", command=previous_window,
                             font=("Copper", 24, 'bold'))
        previous_window_btn.grid(row=23, column=1)

        # ---------------------------------drop down menu for gender selection--------------------------------------

        gender = ["Male", "Female", "Others", "Prefer not to say"]
        indicator = StringVar()
        indicator.set("Choose options")
        dropper = OptionMenu(my_frame, indicator, *gender)
        dropper.grid(row=7, column=1, ipadx=60, ipady=3)
        dropper.config(bg="#CDC8B1")

        # --------------------------------------------Entries are defined-----------------------------------
        try:
            f_nam_entry = Entry(my_frame, bg="#474747", fg="white", font=("cambria", 16, 'italic'))
            f_nam_entry.grid(row=3, column=1, ipadx=60, ipady=3)

            l_nam_entry = Entry(my_frame, bd=2, bg="#FFD39B", font=("cambria", 16, 'italic'))
            #  #FFD39B= burlywood1
            l_nam_entry.grid(row=5, column=1, ipadx=60, ipady=3)
            contact_entry = Entry(my_frame, bg="#474747", fg="white", font=("cambria", 16, 'italic'))
            contact_entry.grid(row=9, column=1, ipadx=60, ipady=3)
            user_name_entry = Entry(my_frame, bd=2, bg="#FFD39B", fg="black", textvariable=username,
                                    font=("cambria", 16, 'italic'))
            user_name_entry.grid(row=11, column=1, ipadx=60, ipady=3)

            password_entry = Entry(my_frame, bd=2, bg="#474747", textvariable=password, show="???", fg="white",
                                   font=("cambria", 16, 'italic'))
            password_entry.grid(row=13, column=1, ipadx=60, ipady=3)

            conf_password_entry = Entry(my_frame, bd=2, bg="#FFD39B", fg="black", textvariable=confirm_password,
                                        show="???", font=("cambria", 16, 'italic'))
            conf_password_entry.grid(row=15, column=1, ipadx=60, ipady=3)
        except (NameError, AttributeError, ValueError) as e:
            print(e.__class__)
            print(e)
        else:

            # -----------------------------------------Slider added------------------------------------
            def geometry_change():
                """
                This changes geometry of Registration Form as the user wants.
                :return: None
                """
                register.geometry(str(length_scale.get()) + "x" + str(height_scale.get()))

            empty_row()
            height_scale = Scale(my_frame, from_=100, to=1000, orient=VERTICAL)
            height_scale.grid(row=21, column=3)
            height_scale.set(800)  # this set function shows first geometry of height
            Label(my_frame, text="Height", bg="#CDC8B1").grid(row=20, column=3)
            empty_row()
            length_scale = Scale(my_frame, from_=50, to=1500, orient=HORIZONTAL)
            length_scale.grid(row=21, column=0)
            Label(my_frame, text="Length", bg="#CDC8B1").grid(row=20, column=0)
            length_scale.set(740)  # this shows first geometry of length of the window

            geometry_change_btn = Button(my_frame, text="Change window size", command=geometry_change,
                                         padx=9, pady=9, highlightbackground="yellow")
            geometry_change_btn.grid(row=21, column=1)
            empty_row()
            register.mainloop()

            # committing changes and closing


# -----------------------------------Coding for Registration Form ends ----------------------------------

row_num = 0
# for storing data of a user from profile page
fetched_income = 0
fetched_expenses = fetched_balance = 0
# for changing each value after adding or subtracting in balance as income and spend cases
income = spend = balance = 0
# only for opening once
income_fetch_first = expense_fetch_first = balance_fetch_first = 0

# function for exiting Signup window as clicked on "EXIT" button.
def exit_signup():
    """
    This function asks confirmation from the user to quit the Signup window.
    :return: None
    """
    response = messagebox.askyesno("Quit", "Do you want to quit ?")
    if response == 1:
        signUp.destroy()

# function for submitting details as clicked on "LOGIN" button.
def submit():
    """
    This shows warnings, error and information as the user provides details.
    :return:None
    """

    if (username_entry.get() == "Enter Username" and password_entry_signup.get() == "Enter Password") or (username_entry.get() == "" and password_entry_signup.get() == ""):
        messagebox.showwarning("Error", "Please, fill both username and password boxes.")
    elif username_entry.get() == "" or username_entry.get() == "Enter Username":
        messagebox.showerror("Error", "Please, fill username box.")
    elif password_entry_signup.get() == "" or password_entry_signup.get() == "Enter Password":
        messagebox.showerror("Error", "Please, fill password box.")
    elif username_entry.get() == "admin" and password_entry_signup.get() == "admin":
        signUp.withdraw()

        # ------------------ GUI for AdminAccount starts from here-----------------------
        adminAccount = Toplevel()
        adminAccount.title("Admin")
        adminAccount.geometry("1400x800")

        heading_title = Label(adminAccount, text="Registered account details", font=("Copperplate", 19, "bold"), padx=3,
                              bd=3,
                              pady=4, bg="red", fg="black")
        heading_title.pack(fill=X)
        # ----------------------------- frames are added ------------------------------
        frame1 = Frame(adminAccount)
        frame1.pack()
        frame2 = Frame(adminAccount, height=250, width=400, bg="white")
        frame2.pack()

        def open_logout():
            """
            This function asks to quit or not
            :return: None
            """
            user_respond_for_quit = messagebox.askyesnocancel("Log out", "Do you want to log out ?")
            if user_respond_for_quit == 1:
                clear_entry()
                signUp.deiconify()
                adminAccount.destroy()

        def delete_account():
            """
            This function deletes account of the users by accepting oid number.
            :return: None
            """
            connector = sqlite3.connect("Accounts_details_holder.db")
            cur = connector.cursor()
            cur.execute("DELETE from registration_details_holder WHERE oid=" + id_entry.get())
            print("Account has been deleted successfully.")
            messagebox.showinfo("Deletion",
                                "An account has been deleted successfully. Please, log out and resign in to view changes.")
            id_entry.delete(0, END)
            connector.commit()
            connector.close()

        # ------------------------------------- DATABASE -----------------------------
        connector = sqlite3.connect("Accounts_details_holder.db")
        cur = connector.cursor()
        # showing all recorded information of the users.
        cur.execute("SELECT *, oid FROM registration_details_holder")
        # retrieving all stored information
        all_records = cur.fetchall()
        # print(all_records)

        headings_list = ["First Name", "Last Name", "Gender", "Contact", "Username", "Password", "Oid"]
        # using Treeview to show information in a proper manner.
        table = ttk.Treeview(frame1, columns=headings_list, show='headings', height=28)
        for arrange in headings_list:
            table.heading(arrange, text=arrange)
        table.pack(side=LEFT)
        for serial_num, (firstName, lastName, gender, contact, userName, password, oid_num) in enumerate(all_records,
                                                                                                         start=1):
            table.insert("", "end", values=(firstName, lastName, gender, contact, userName, password, oid_num))

        # =============================== Entries are added ======================================

        id_entry = Entry(frame2, bd=3, width=30)
        id_entry.grid(row=0, column=1, padx=20, pady=15)

        # ----------------- for deleting any suspicious account that violates any policies  ----------------------------
        id_label = Label(frame2, text="ID", font=("Times new roman", 25, "bold"))
        id_label.grid(row=0, column=0)

        # button with event is added
        delete_button = Button(frame2, text="Delete", highlightbackground="green", font=("Cambria", 25, "bold"),
                               command=delete_account, fg="blue")
        delete_button.grid(row=1, column=0, padx=10, pady=15, columnspan=4, ipadx=9, ipady=8)

        # for log out
        logout_button = Button(frame2, text="Log out", highlightbackground="green", font=("Cambria", 25, "bold"),
                               command=open_logout, fg="blue")
        logout_button.grid(row=2, column=0, padx=10, pady=15, columnspan=4, ipadx=9, ipady=8)
        """
        # --------------------------- Scroll bar is added --------------------------
        scrollbar_y = Scrollbar(frame1, orient=VERTICAL, command=table.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        """
        adminAccount.mainloop()
                     # ------------------ GUI for AdminAccount ends here-----------------------

    else:

        connetor = sqlite3.connect("Accounts_details_holder.db")
        cur = connetor.cursor()
        query = "Select * from registration_details_holder where username=? and password=?"

        cur.execute(query,(username_entry.get(), password_entry_signup.get()))
        rows = cur.fetchall()
        # checking whether it is empty or not, if empty shows error message , if no allows to login
        if len(rows) > 0:
             messagebox.showinfo("Account Created", "Login has been successfully done")
             # this is again assigned because to stop error

             # --------------------------------- User account GUI and database are started ------------------------------
             signUp.withdraw()
             myAccount = Toplevel()
             myAccount.title("MY ACCOUNT")
             myAccount.iconbitmap("see.ico")
             myAccount.geometry("700x650")
             myAccount.configure(bg="black")
             myAccount.resizable(False, False)

             def read_my_files():
                 # files are created to save values of income , spend and balance

                 with open(str(password_entry_signup.get() + "_income.txt"), "r+") as income_file:
                     income_file.seek(0)
                     stored_income_value = income_file.read()
                     # print("Income from reading txt : ", stored_income_value)

                 global fetched_income

                 fetched_income = stored_income_value
                 # print("Your income after reading txt file is : ", fetched_income)

                 with open(str(password_entry_signup.get() + "_expenses.txt"), "r+") as expenses_file:
                     stored_expenses_value = expenses_file.read()
                     # print("Expenses from reading txt : ", stored_expenses_value)
                 global fetched_expenses
                 fetched_expenses = stored_expenses_value

                 with open(str(password_entry_signup.get() + "_balance.txt"), "r+") as balance_file:
                     stored_balance_value = balance_file.read()
                     # print("Balance from reading txt  : ", stored_balance_value)

                 global fetched_balance
                 fetched_balance = stored_balance_value

             # now checking whether a file is existing or not. if yes it is True, if not False.
             # This only runs when a new account is created and using for the first time.
             # here how it works, not(...) and not(..) and not(..) ====> not(False) and not(False) and not(False)
             # ====> True and True and True

             if not(os.path.isfile(str(password_entry_signup.get() + "_income.txt"))) and\
                     not(os.path.isfile(str(password_entry_signup.get() + "_expenses.txt"))) and\
                     not(os.path.isfile(str(password_entry_signup.get() + "_balance.txt"))):
                 #print("This is creating files for new ones.")
                 # To create 3 different files of the user for once time so, a+ mode is used.
                 with open(str(password_entry_signup.get() + "_income.txt"), "a+") as f:
                     f.write("0")

                 with open(str(password_entry_signup.get() + "_expenses.txt"), "a+") as file:
                     file.write("0")

                 with open(str(password_entry_signup.get() + "_balance.txt"), "a+") as file:
                     file.write("0")

             # Note 1: pasted
             read_my_files()

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
                 profile_win.resizable(0, 0)

                 # ----------------------------  frames are added ------------------

                 topFrame = Frame(profile_win, bg="yellow")
                 topFrame.place(x=10, y=10, width=680, height=80)
                 bottomFrame = Frame(profile_win, bg="white")
                 bottomFrame.place(x=10, y=100, width=680, height=490)
                 def back_func():
                     """
                     This function returns to the previous page i.e My account by exiting current page.
                     :return: None
                     """
                     myAccount.deiconify()
                     profile_win.destroy()

                 #  ================================= headline added ======================================

                 heading_img = PhotoImage(file="profile.png")
                 heading = Label(topFrame, text="MY PROFILE", font=("Copperplate", 32, "bold"),
                                 bg="green", fg="yellow", bd=6, relief=RIDGE)
                 heading.pack(side=TOP, fill=X, expand=0)
                 heading.config(image=heading_img, compound=LEFT)

                 # Note 1: file read and cut from here
                 read_my_files()
                 # ----------------------- labels are defined -----------------------
                 income_label = Label(bottomFrame, text="Income", font=("courier", 25, "bold"), fg="yellow", bg="green")
                 income_label.grid(row=0, column=0, columnspan=1, padx=50, pady=10)

                 spend_label = Label(bottomFrame, text="Expenses", font=("courier", 25, "bold"), fg="yellow",
                                     bg="green")
                 spend_label.grid(row=0, column=2, columnspan=1, padx=50, pady=10)

                 balance_label = Label(bottomFrame, text="Balance", font=("courier", 25, "bold"), fg="yellow",
                                       bg="green")
                 balance_label.grid(row=0, column=4, columnspan=1, padx=50, pady=10)

                 # ------------------------- values of respective labels are given ------------------------

                 income_value = Label(bottomFrame, text="$" + str(fetched_income), font=("courier", 25, "bold"), fg="black",
                                      bg="white")
                 income_value.grid(row=1, column=0, columnspan=1, padx=50, pady=10)

                 spend_value = Label(bottomFrame, text="$" + str(fetched_expenses), font=("courier", 25, "bold"), fg="black",
                                     bg="white")
                 spend_value.grid(row=1, column=2, columnspan=1, padx=50, pady=10)

                 balance_value = Label(bottomFrame, text="$" + str(fetched_balance), font=("courier", 25, "bold"), fg="black",
                                       bg="white")
                 balance_value.grid(row=1, column=4, columnspan=1, padx=50, pady=10)

                 # ------------------------------------ Basic details of the user-------------------------------------
                 connect_me = sqlite3.connect("Accounts_details_holder.db")
                 cur = connect_me.cursor()
                 cur.execute("SELECT username, password,first_name, last_name, gender, contact, oid FROM registration_details_holder")
                 fetch_data = cur.fetchall()
                 #print(fetch_data)
                 # Searching details of the particular user and matching his/her password
                 # from the database to fetch his/her other details for showing details on the screen

                 for username_search, password_search, first_name_search, last_name_search, gender_search, contact_search,oid_search in fetch_data:  # [(username, oid), (username, oid), ..]
                     #print(username_search, password_search, oid_search)  # (username, oid)

                     if username_search == username_entry.get() and password_search == password_entry_signup.get():
                         first_name_found = first_name_search
                         last_name_found = last_name_search
                         gender_found = gender_search
                         contact_found = contact_search
                         oid_found = oid_search
                         print(first_name_found, last_name_found, gender_found, contact_found, oid_found)
                         break

                 connect_me.commit()
                 connect_me.close()

                 # ---------------------Now, details are shoving on the screen------------------
                 global full_name_show, gender_show, contact_show, username_show, oid_show

                 full_name_show = first_name_found +" "+ last_name_found
                 gender_show = gender_found
                 contact_show = contact_found
                 username_show = username_entry.get()
                 oid_show = oid_found

                 user_fullName = Label(bottomFrame, text=f"Name : {full_name_show}", font=("courier", 25, "bold"), fg="black",
                                       bg="white")
                 user_fullName.grid(row=2, column=0, columnspan=3, padx=50, pady=10, sticky=W)

                 user_gender = Label(bottomFrame, text=f"Gender : {gender_show}", font=("courier", 25, "bold"),
                                       fg="black", bg="white")
                 user_gender.grid(row=3, column=0, columnspan=3, padx=50, pady=10, sticky=W)

                 user_contact = Label(bottomFrame, text=f"Contact : {contact_show}", font=("courier", 25, "bold"),
                                       fg="black", bg="white")
                 user_contact.grid(row=4, column=0, columnspan=3, padx=50, pady=10, sticky=W)

                 user_username = Label(bottomFrame, text=f"Username : {username_show}", font=("courier", 25, "bold"),
                                       fg="black", bg="white")
                 user_username.grid(row=5, column=0, columnspan=3, padx=50, pady=10, sticky=W)

                 user_oid = Label(bottomFrame, text=f"Oid number : {oid_show}", font=("courier", 25, "bold"),
                                       fg="black", bg="white")
                 user_oid.grid(row=6, column=0, columnspan=3, padx=50, pady=10, sticky=W)

                 # button with event
                 back_button = Button(bottomFrame, text="BACK", font=("times new roman", 25, "bold"),
                                      command=back_func, highlightbackground="white", fg="black")
                 back_button.grid(row=7, column=1, columnspan=3, padx=50, pady=10)

                 profile_win.mainloop()

             def open_income_func():
                 """
                 This function continues to next module by hiding this module and  calling another function within it.
                 :return: None
                 """
                 myAccount.withdraw()
                 #  ----------------------- GUI for income is started ---------------------
                 income_win = Toplevel()
                 income_win.title("MY INCOME")
                 income_win.iconbitmap("income.ico")
                 income_win.geometry("700x700")
                 income_win.configure(bg="black")
                 income_win.resizable(0, 0)

                 def adding_budget():
                     """
                     This function checks whether provided values are digit (numeric data type except complex) or not.
                     IF not, shows error message.
                     IF they are digit , then only function allows to add all provided values and save in txt file.
                     :return: float
                     """
                     # Now, checking  whether provided each word or letter of each entry is digit or not.
                     # all entries are kept in list data structure to traverse each letter and entry, where outer loop
                     # traverses each entry and inner loop traverses each word and checks it is digit or not.

                     entries_fields = [salary_entry.get(), poultry_farming_entry.get(),
                                       animal_husbandy_entry.get(), vegetable_farming_entry.get(),
                                       shops_entry.get(), house_rent_entry.get(), others_entry.get()]
                     stoping_outer_loop = 0
                     for checking_each_entry in entries_fields:
                         if stoping_outer_loop == 1:
                             break
                         for checking_each_letter in checking_each_entry:
                             if checking_each_letter.isdigit():
                                 inserted_in_numbers = True
                             else:
                                 inserted_in_numbers = False
                                 stoping_outer_loop += 1
                                 break

                     if salary_entry.get() == "" and poultry_farming_entry.get() == "" and\
                             vegetable_farming_entry.get() == "" and house_rent_entry.get() == "" and \
                             animal_husbandy_entry.get() == "" and shops_entry.get() == "" and others_entry.get() == "":

                         messagebox.showerror("Empty", "All boxes are empty.")

                     # now, allowing digits only
                     elif inserted_in_numbers is False:
                         messagebox.showerror("Invalid", "Please, insert budget in numbers only.")

                     elif salary_entry.get() == "":
                         messagebox.showerror("Empty", "Salary box is empty. Please, insert it.")

                     elif poultry_farming_entry.get() == "":
                         messagebox.showerror("Empty", "Poultry Farming box is empty. Please, insert it.")

                     elif animal_husbandy_entry.get() == "":
                         messagebox.showerror("Empty", "Animal husbandry box is empty. Please, insert it.")

                     elif house_rent_entry.get() == "":
                         messagebox.showerror("Empty", "House rent box is empty. Please, insert it.")

                     elif others_entry.get() == "":
                         messagebox.showerror("Empty", "Others box is empty. Please, insert it.")

                     elif vegetable_farming_entry.get() == "":
                         messagebox.showerror("Empty", "Vegetable Farming box is empty. Please, insert it.")

                     elif shops_entry.get() == "":
                         messagebox.showerror("Empty", "Shop box is empty. Please, insert it.")

                     else:
                         total_income = float(salary_entry.get()) + float(poultry_farming_entry.get()) + \
                                        float(animal_husbandy_entry.get()) + float(vegetable_farming_entry.get()) + \
                                        float(shops_entry.get()) + float(others_entry.get()) + float(house_rent_entry.get())

                         #print("Total income is : ", total_income)

                         # clearing the entry fields after inserting info
                         salary_entry.delete(0, END)
                         poultry_farming_entry.delete(0, END)
                         vegetable_farming_entry.delete(0, END)
                         house_rent_entry.delete(0, END)
                         animal_husbandy_entry.delete(0, END)
                         shops_entry.delete(0, END)
                         others_entry.delete(0, END)

                         #read_my_files()

                         global income_fetch_first, income, fetched_income, balance, balance_fetch_first

                         if income_fetch_first == 0 and balance_fetch_first == 0:

                             # fetching previous stored income value after opening first

                             #print("fetched_income after adding budget for the first time : ", fetched_income)

                             income = total_income + float(fetched_income)
                             fetched_income = 0
                             #print("income after adding buddget for the first time : ", income)

                             # changing value of income_fetch_first because not to run this instead this , run else block
                             income_fetch_first += 1
                             #print("icome_fetch_first = ", income_fetch_first)

                             # maintaining balance after adding budget
                             # fetching previous stored balance after opening first
                             #print("fetched_balance after adding budget for the first time : ", balance)
                             balance = total_income + float(fetched_balance)
                             #print("balance after adding budget for the first time : ", balance)
                             # changing value of balance_fetch_first because not to run this instead this , run else block
                             balance_fetch_first += 1
                             #print("balance_fetched_first = ", balance_fetch_first)

                         else:
                             # adding new budget in previous stored income after opening more than first
                             income += total_income
                             #print("income after adding budget more than for the first time = ", income)
                             fetched_income = 0


                             # maintaining balance after adding budget
                             # adding balance in previous stored income after opening more than first
                             balance += total_income
                             #print("balance after adding budget more than for the first time = ", balance)

                         # overwriting the value of income by new value in created file
                         with open(str(password_entry_signup.get()+"_income.txt"), "w+") as income_file:
                             income_file.write(str(income))
                         """"
                         # maintaining balance after adding budget
                         global balance, balance_fetch_first
                         if balance_fetch_first == 0:
                             # fetching previous stored balance after opening first
                             balance += total_income + float(fetched_balance)

                             # changing value of balance_fetch_first because not to run this instead this , run else block
                             balance_fetch_first += 1

                         else:
                             # adding balance in previous stored income after opening more than first
                             balance += total_income

                         """
                         with open(str(password_entry_signup.get() + "_balance.txt"), "r+") as balance_file:
                             balance_file.write(str(balance))

                         messagebox.showinfo("Total Budget", "Your recent added budget is $" + str(total_income) +
                               ", total income is $" + str(income) + " and your new balance is $" + str(balance) + ". Thank You!")



                 def go_back():
                     """
                     This function returns the previous page.
                     :return: None
                     """

                     myAccount.deiconify()
                     income_win.destroy()
                 # ----------------------------  frames are added ------------------

                 topFrame2 = Frame(income_win, bg="yellow")
                 topFrame2.place(x=10, y=10, width=680, height=80)
                 bottomFrame2 = Frame(income_win, bg="white")
                 bottomFrame2.place(x=10, y=100, width=680, height=590)

                 #  ================================= headline added ======================================
                 heading_img = PhotoImage(file="income.png")
                 heading = Label(topFrame2, text="MY INCOME", font=("Copperplate", 32, "bold"),
                                 bg="green", fg="yellow", bd=6, relief=RIDGE)
                 heading.pack(side=TOP, fill=X, expand=0)
                 heading.config(image=heading_img, compound=LEFT)

                 # ----------------------------- labels are added -------------------------------
                 instruction = "Please, insert your budget (only in numbers) from the following sectors :"

                 instruction_label = Label(bottomFrame2, text=instruction, font=("times new roman", 22, "italic"),
                                      fg="black", bg="white")
                 instruction_label.grid(row=0, column=0, columnspan=2, padx=2, pady=10, sticky=W)

                 salary_label = Label(bottomFrame2, text="Salary :", font=("times new roman", 20, "bold"),
                                       fg="black", bg="white")
                 salary_label.grid(row=1, column=0, padx=2, pady=10, sticky=W)

                 poultry_farming_label = Label(bottomFrame2, text="Poultry Farming :", font=("times new roman", 20, "bold"),
                                     fg="black", bg="white")

                 poultry_farming_label.grid(row=2, column=0, padx=2, pady=10, sticky=W)

                 vegetable_farming_label = Label(bottomFrame2, text="Vegetable Farming :", font=("times new roman", 20, "bold"),
                                      fg="black", bg="white")
                 vegetable_farming_label.grid(row=3, column=0, padx=2, pady=10, sticky=W)

                 house_rent_label = Label(bottomFrame2, text="House Rent :", font=("times new roman", 20, "bold"),
                                               fg="black", bg="white")

                 house_rent_label.grid(row=4, column=0, padx=2, pady=10, sticky=W)

                 animal_husbandy_label = Label(bottomFrame2, text="Animal Husbandry :", font=("times new roman", 20, "bold"),
                                               fg="black", bg="white")

                 animal_husbandy_label.grid(row=5, column=0, padx=2, pady=10, sticky=W)

                 shops_label = Label(bottomFrame2, text="Shops :",
                                                 font=("times new roman", 20, "bold"),
                                                 fg="black", bg="white")
                 shops_label.grid(row=6, column=0, padx=2, pady=10, sticky=W)

                 others_label = Label(bottomFrame2, text="Others :", font=("times new roman", 20, "bold"),
                                          fg="black", bg="white")

                 others_label.grid(row=7, column=0, padx=2, pady=10, sticky=W)

                 # -------------------------- entries are added ------------------------------

                 salary_entry = Entry(bottomFrame2, font=("cambria", 20, "italic"), width=20, bd=3,
                                      fg="black", bg="white")
                 salary_entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)

                 poultry_farming_entry = Entry(bottomFrame2, font=("cambria", 20, "italic"), width=20, bd=3,
                                     fg="black", bg="white")
                 poultry_farming_entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

                 vegetable_farming_entry = Entry(bottomFrame2, font=("cambria", 20, "italic"), width=20, bd=3,
                                      fg="black", bg="white")
                 vegetable_farming_entry.grid(row=3, column=1, padx=2, pady=10, sticky=W)

                 house_rent_entry = Entry(bottomFrame2, font=("cambria", 20, "italic"), width=20, bd=3,
                                               fg="black", bg="white")
                 house_rent_entry.grid(row=4, column=1, padx=2, pady=10, sticky=W)

                 animal_husbandy_entry = Entry(bottomFrame2, font=("cambria", 20, "italic"), width=20, bd=3,
                                               fg="black", bg="white")
                 animal_husbandy_entry.grid(row=5, column=1, padx=2, pady=10, sticky=W)

                 shops_entry = Entry(bottomFrame2, font=("cambria", 20, "italic"), width=20, bd=3,
                                                 fg="black", bg="white")
                 shops_entry.grid(row=6, column=1, padx=2, pady=10, sticky=W)

                 others_entry = Entry(bottomFrame2, font=("cambria", 20, "italic"), width=20, bd=3,
                                          fg="black", bg="white")
                 others_entry.grid(row=7, column=1, padx=2, pady=10, sticky=W)

                 # ------------------ button with event is defined -----------------

                 add_button = Button(bottomFrame2, text="Add budget", font=("times new roman", 24, "bold"),
                                     command=adding_budget, fg="black", highlightbackground="green")
                 add_button.grid(row=8, column=1, padx=65, pady=10, ipadx=2, ipady=2, sticky=W)

                 back_btn = Button(bottomFrame2, text="BACK", font=("times new roman", 24, "bold"), command=go_back,
                                     fg="black", highlightbackground="green")
                 back_btn.grid(row=9, column=1, padx=90, pady=10, ipadx=2, ipady=2, sticky=W)

                 income_win.mainloop()

             def open_expenses_func():
                 """
                 This function continues to next module by hiding this module and  calling another function within it.
                 :return: None
                 """
                 myAccount.withdraw()
                 #  ----------------------- GUI for expenses is started ---------------------
                 expenses_win = Toplevel()
                 expenses_win.title("MY EXPENSES")
                 expenses_win.iconbitmap("expenses.ico")
                 expenses_win.geometry("700x700")
                 expenses_win.configure(bg="black")
                 expenses_win.resizable(0, 0)

                 def go_previous():
                     """
                     This function returns the previous page.
                     :return: None
                     """

                     myAccount.deiconify()
                     expenses_win.destroy()
                 def save_expenses():
                     """
                     This function saves expenditure of the user as float.
                     :return: None
                     """
                     # checking whether entered information in 'price' entry are digits or not
                     price_result = digit_checker(price_entry)

                     if price_entry.get() == "":
                         messagebox.showerror("Empty", "Price box is empty. Please , fill it.")

                     elif price_result is False:
                         messagebox.showerror("Invalid", "Please , insert digits only in it.")

                     else:

                         # -------- as a whole maintaining balance after adding expenses budget so, subtracting now --------
                         read_my_files()

                         global balance
                         # now checking whether a file is existing or not. if yes it is True, if not False.

                         #if os.path.isfile(str(password_entry_signup.get() + "_income.txt")):
                         balance = float(fetched_balance) # to read previous

                         # now , balance stored in new variable because just to show warning if balance is low
                         current_balance = balance

                         balance -= float(price_entry.get())
                         #print(f"Your balance after spending : {balance}")
                         # checking balance is lesser than 0 , if yes show warning , if no do calcaulation
                         if balance >= 0:
                             global spend, expense_fetch_first

                             if expense_fetch_first == 0:

                                spend = float(price_entry.get()) + float(fetched_expenses)
                                expense_fetch_first += 1

                             else:
                                 spend += float(price_entry.get())
                                 #print("after spending = ", spend)
                             with open(str(password_entry_signup.get() + "_expenses.txt"), "w+") as expenses_file:
                                 expenses_file.write(str(spend))

                             with open(str(password_entry_signup.get() + "_balance.txt"), "r+") as balance_file:
                                 balance_file.write(str(balance))
                             messagebox.showinfo("Expenses", "Your recent expenditure is $" + price_entry.get() +
                                                 ", total expenditure is $" + str(spend) +
                                                 " and your new balance is $" + str(balance) + " Thank you !")
                         else:
                             # inserted price is added with existed balance because to make balance after subtracting
                             balance += float(price_entry.get())
                             messagebox.showwarning("No balance", "Sorry, no enough money. Your current balance is $"
                                                    + str(current_balance))

                         price_entry.delete(0, END)




                 # ----------------------------  frames are added ------------------

                 topFrame3 = Frame(expenses_win, bg="yellow")
                 topFrame3.place(x=10, y=10, width=680, height=80)
                 bottomFrame3 = Frame(expenses_win, bg="white")
                 bottomFrame3.place(x=10, y=100, width=680, height=220)
                 bottomFrame3_another = Frame(expenses_win, bg="white")
                 bottomFrame3_another.place(x=10, y=320, width=680, height=365)

                 #  ================================= headline added ======================================
                 heading_img = PhotoImage(file="expenses.png")
                 heading = Label(topFrame3, text="MY EXPENSES", font=("Copperplate", 32, "bold"),
                                 bg="green", fg="yellow", bd=6, relief=RIDGE)
                 heading.pack(side=TOP, fill=X, expand=0)
                 heading.config(image=heading_img, compound=LEFT)


                 # --------------------------label in bottomFrame3 is defined --------------------------------
                 category_items = "Please, choose the only one category at a time :"
                 category_label = Label(bottomFrame3, text=category_items, font=("times new roman", 24, "italic"),
                                           fg="black", bg="white")
                 category_label.pack(padx=2, pady=10, anchor=W)

                 # --------------- for radiobuttons, category is written twice as text and value respectively------------
                 categories_options = [("Education", "Education"), ("Shopping", "Shopping"),
                                       ("Transportation", "Transportation"), ("Foods", "Foods"),
                                       ("Clothing", "Clothing"), ("Entertainment", "Entertainment")]

                 chosen_option = StringVar()
                 chosen_option.set("Education")

                 for options, opt_value in categories_options:
                     make_radiobutton = Radiobutton(bottomFrame3, text=options, variable=chosen_option, value=opt_value)
                     make_radiobutton.pack(padx=2, pady=2, anchor=W)

                 # ------------------ labels are defined in bottomFrame3_another ----------------------

                 price_label = Label(bottomFrame3_another, text="Price :", font=("Times", 20, "bold"),
                                      fg="black", bg="white")
                 price_label.grid(row=0, column=0, padx=2, pady=10, sticky=W)

                 date_label = Label(bottomFrame3_another, text="Date :", font=("times", 20, "bold"),
                                               fg="black", bg="white")

                 date_label.grid(row=1, column=0, padx=2, pady=10, sticky=W)

                 # -------------------- entries are defined ----------------------------------
                 price_entry = Entry(bottomFrame3_another, font=("times", 20, "italic"), width=20, bd=3,
                                      fg="black", bg="white")
                 price_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W, columnspan=3)

                 # -------- addding Spinboxes from tkcalendar library ---------------------
                 year = Spinbox(bottomFrame3_another, from_=2020, to=2025, state="readonly",
                                font=("times", 20), width=10, justify=CENTER)
                 year.grid(row=1, column=1, padx=2, pady=10, sticky=W)

                 month = Spinbox(bottomFrame3_another, from_=1, to=12, state="readonly",
                                 font=("times", 20), width=6, justify=CENTER)
                 month.grid(row=1, column=2, padx=2, pady=10, sticky=W)

                 day = Spinbox(bottomFrame3_another, from_=1, to=28, state="readonly",
                                font=("times", 20), width=6, justify=CENTER)
                 day.grid(row=1, column=2, padx=2, pady=10, sticky=E)

                 # ----------------- buttons with event ------------------------
                 save_button = Button(bottomFrame3_another, text="Save", font=("times new roman", 24, "bold"),
                                     command=save_expenses, fg="black", highlightbackground="green")
                 save_button.grid(row=2, column=2, padx=125, pady=10, ipadx=4, ipady=2, sticky=W, columnspan=2)

                 previous_btn = Button(bottomFrame3_another, text="BACK", font=("times new roman", 24, "bold"),
                                       command=go_previous, fg="black", highlightbackground="green")
                 previous_btn.grid(row=3, column=2, padx=120, pady=10, ipadx=2, ipady=2, sticky=W, columnspan=3)
                 expenses_win.mainloop()

             def open_setting_func():
                 """
                 This function continues to next module by hiding this module and  calling another function within it.
                 :return: None
                 """

                 myAccount.withdraw()
                 #  ----------------------- GUI for setting is started ---------------------
                 setting_win = Toplevel()
                 setting_win.title("MY SETTING")
                 setting_win.iconbitmap("setting.ico")
                 setting_win.geometry("700x600")
                 setting_win.configure(bg="black")
                 setting_win.resizable(0, 0)

                 # ----------------------------  frames are added ------------------

                 topFrame4 = Frame(setting_win, bg="yellow")
                 topFrame4.place(x=10, y=10, width=680, height=80)
                 bottomFrame4 = Frame(setting_win, bg="white")
                 bottomFrame4.place(x=10, y=100, width=680, height=490)

                 def delete_my_account():
                     sure = messagebox.askyesno("Account delete", "Do you want to delete the account ?")
                     if sure == 1:

                         connection = sqlite3.connect("Accounts_details_holder.db")
                         cur = connection.cursor()

                         cur.execute("SELECT username, password,oid FROM registration_details_holder")
                         fetch_data = cur.fetchall()
                         # print(fetch_data)
                         # Searching details of the particular user and matching his/her username and  password
                         # from the database to fetch his/her other details for showing details on the screen

                         for username_search, password_search, oid_search in fetch_data:  # [(username, oid), (username, oid), ..]
                             # print(username_search, password_search, oid_search)

                             if username_search == username_entry.get() and password_search == password_entry_signup.get():
                                 actual_oid = oid_search
                                 # print(type(actual_oid))
                                 break
                         cur.execute("DELETE from registration_details_holder WHERE oid=" + str(actual_oid))
                         print("Account has been deleted successfully.")
                         messagebox.showinfo("Account deletion", "Your account has been deleted successfully.")
                         connection.commit()
                         connection.close()

                         setting_win.destroy()
                         sys.exit()

                 def change_my_password():
                     """
                     This function allows to change password only if proved username and old password are matched with database.
                     :return: None
                     """
                     # checking whether entered oid number in entry are digits or not

                     oid_result = digit_checker(using_oid_entry)

                     #print(type(using_oid_entry.get()))

                     # ------------------ retrieving data from database -----------------------
                     connect_me = sqlite3.connect("Accounts_details_holder.db")
                     cur = connect_me.cursor()
                     cur.execute("SELECT username, password, oid FROM registration_details_holder")
                     fetch_data = cur.fetchall()
                     #print(fetch_data)
                     # Searching details of the particular user and matching his/her password and username
                     # from the database to fetch his/her other details for showing details on the screen

                     for username_search, password_search, oid_search in fetch_data:
                         #print(username_search, password_search, oid_search)

                         if username_search == username_entry.get() and password_search == password_entry_signup.get():
                             actual_oid = oid_search

                             #print(type(actual_oid))
                             break

                     connect_me.commit()
                     connect_me.close()

                     if again_username_entry.get() == "Enter your username" and \
                             again_password_entry.get() == "Enter your old password" and \
                             again_new_password_entry.get() == "Enter your new password" and \
                             again_confirm_password_entry.get() == "Confirm your password" and \
                             using_oid_entry.get() == "Enter your oid number":

                         messagebox.showerror("Empty", "All boxes are empty")

                     elif again_username_entry.get() == "Enter your username" or again_username_entry.get() == "":
                         messagebox.showwarning("Empty", "Username box is empty. Please, insert your username.")

                     elif again_password_entry.get() == "Enter your old password" or again_password_entry.get() == "":
                         messagebox.showwarning("Empty", "Old password box is empty. Please, insert your old password.")

                     elif again_new_password_entry.get() == "Enter your new password" or again_new_password_entry.get() == "":
                         messagebox.showwarning("Empty", "New password box is empty. Please, insert your new password.")

                     elif again_confirm_password_entry.get() == "Confirm your password" or again_confirm_password_entry.get() == "":
                         messagebox.showwarning("Empty",
                                                "Confirm password box is empty. Please, insert your confirm password.")

                     elif using_oid_entry.get() == "Enter your oid number" or using_oid_entry.get() == "":
                         messagebox.showwarning("Empty",
                                                "Oid number box is empty. Please, insert your oid number.")

                     elif again_new_password_entry.get() != again_confirm_password_entry.get():
                         messagebox.showerror("Invalid", "New password and Confirm password do not match.")

                     elif again_username_entry.get() != username_entry.get():
                         messagebox.showerror("Invalid",
                                                "Your username does not match with our database. Please, insert it again.")

                     elif again_password_entry.get() != password_entry_signup.get():
                         messagebox.showerror("Invalid",
                                                "Your password does not match with our database. Please, insert it again.")
                     elif oid_result is False:
                         messagebox.showerror("Invalid oid", "Please , insert in digits only.")

                     # changing data type of using_oid_entry from str to int for copmarison as data type of actual_oid is int
                     elif int(using_oid_entry.get()) != actual_oid:
                         messagebox.showerror("Invalid oid", "Inserted oid number does not match.")

                     else:
                         #print("working")

                         # ------------ retrieving all data of this user only ---------------------
                         connector = sqlite3.connect("Accounts_details_holder.db")
                         cur = connector.cursor()
                         cur.execute("SELECT * FROM registration_details_holder WHERE oid=" + str(actual_oid))
                         one_user_records = cur.fetchall()
                         print(one_user_records)

                         # --------------------updating password of the user-------------
                         cur.execute("""UPDATE registration_details_holder SET password = :new_password WHERE oid = :oid""",
                                     {'new_password' : again_confirm_password_entry.get(), 'oid' : using_oid_entry.get()})

                         connector.commit()
                         connector.close()

                         messagebox.showinfo("Password Changed", "Your password has been changed successfully.")

                         again_username_entry.delete(0, END)
                         again_password_entry.delete(0, END)
                         again_new_password_entry.delete(0, END)
                         again_confirm_password_entry.delete(0, END)
                         using_oid_entry.delete(0, END)
                         clear_entry()

                         signUp.deiconify()
                         setting_win.destroy()
                         myAccount.destroy()



                 # function created to clear the entry on click or tab
                 def clear_again_username_entry(event):
                     """
                     This clears the username entry on clicking the entry or tab key.
                     :param event: int
                     :return: None
                     """
                     again_username_entry.delete(0, END)

                 def clear_again_password_entry(event):
                     """
                     This clears the old password entry on clicking the entry or tab key.
                     :param event: int
                     :return: None
                     """
                     again_password_entry.delete(0, END)
                     again_password_entry.configure(show="???")

                 def clear_again_new_password_entry(event):
                     """
                     This clears the new password entry on clicking the entry or tab key.
                     :param event: int
                     :return: None
                     """
                     again_new_password_entry.delete(0, END)
                     again_new_password_entry.configure(show="???")

                 def clear_again_confirm_password_entry(event):
                     """
                     This clears the confirm password entry on clicking the entry or tab key.
                     :param event: int
                     :return: None
                     """
                     again_confirm_password_entry.delete(0, END)
                     again_confirm_password_entry.configure(show="???")

                 def clear_using_oid_entry(event):
                     """
                     This clears the confirm password entry on clicking the entry or tab key.
                     :param event: int
                     :return: None
                     """
                     using_oid_entry.delete(0, END)


                 def back_to_myAccount():
                     """
                     This function returns to the previous page i.e My account by exiting current page.
                     :return: None
                     """
                     myAccount.deiconify()
                     setting_win.destroy()

                 #  ================================= headline added ======================================

                 heading_img4 = PhotoImage(file="setting.png")
                 heading4 = Label(topFrame4, text="MY SETTING", font=("Copperplate", 32, "bold"),
                                 bg="green", fg="yellow", bd=6, relief=RIDGE)
                 heading4.pack(side=TOP, fill=X, expand=0)
                 heading4.config(image=heading_img4, compound=LEFT)

                 # ----------------- labels are defined --------------------

                 again_username_label = Label(bottomFrame4, text="Username :", font=("ai bayan ", 20, "bold"),
                                      fg="black", bg="white")
                 again_username_label.grid(row=0, column=0, padx=2, pady=10, sticky=W)

                 again_password_label = Label(bottomFrame4, text="Old password:", font=("ai bayan", 20, "bold"),
                                               fg="black", bg="white")

                 again_password_label.grid(row=1, column=0, padx=2, pady=10, sticky=W)

                 again_new_password_label = Label(bottomFrame4, text="New password :",
                                                 font=("ai bayan", 20, "bold"), fg="black", bg="white")
                 again_new_password_label.grid(row=2, column=0, padx=2, pady=10, sticky=W)

                 again_confirm_password_label = Label(bottomFrame4, text="Confirm password :", font=("ai bayan", 20, "bold"),
                                          fg="black", bg="white")

                 again_confirm_password_label.grid(row=3, column=0, padx=2, pady=10, sticky=W)

                 using_oid_label = Label(bottomFrame4, text="Oid number :",
                                                      font=("ai bayan", 20, "bold"), fg="black", bg="white")

                 using_oid_label.grid(row=4, column=0, padx=2, pady=10, sticky=W)

                 # -------------------- entries are defined  with functions-----------------------------
                 again_username_type = StringVar()
                 again_username_entry = Entry(bottomFrame4, font=("cambria", 18, "italic"), width=20, bd=3,
                                      textvariable=again_username_type, fg="black", bg="white")
                 again_username_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)
                 again_username_entry.insert(0, "Enter your username")
                 # on clicking 'tab' key, FocusIn allows to enter in password entry
                 again_username_entry.bind("<FocusIn>", clear_again_username_entry)


                 again_password_type = StringVar()
                 again_password_entry = Entry(bottomFrame4, font=("cambria", 18, "italic"), width=20, bd=3,
                                               textvariable=again_password_type, fg="black", bg="white")
                 again_password_entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)
                 again_password_entry.insert(0, "Enter your old password")
                 again_password_entry.bind("<FocusIn>", clear_again_password_entry)


                 again_new_password_type = StringVar()
                 again_new_password_entry = Entry(bottomFrame4, font=("cambria", 18, "italic"), width=20, bd=3,
                                                textvariable=again_new_password_type, fg="black", bg="white")
                 again_new_password_entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)
                 again_new_password_entry.insert(0, "Enter your new password")
                 again_new_password_entry.bind("<FocusIn>", clear_again_new_password_entry)


                 again_confirm_password_type = StringVar()
                 again_confirm_password_entry = Entry(bottomFrame4, font=("cambria", 18, "italic"), width=20, bd=3,
                                          textvariable=again_confirm_password_type, fg="black", bg="white")
                 again_confirm_password_entry.grid(row=3, column=1, padx=2, pady=10, sticky=W)

                 again_confirm_password_entry.insert(0, "Confirm your password")
                 again_confirm_password_entry.bind("<FocusIn>", clear_again_confirm_password_entry)


                 using_oid_entry = Entry(bottomFrame4, font=("cambria", 18, "italic"), width=20, bd=3,
                                                      fg="black", bg="white")
                 using_oid_entry.grid(row=4, column=1, padx=2, pady=10, sticky=W)

                 using_oid_entry.insert(0, "Enter your oid number")
                 using_oid_entry.bind("<FocusIn>", clear_using_oid_entry)

                 # -------------------------- buttons with event are define ------------------------------

                 password_change_btn = Button(bottomFrame4, text="Change password", font=("times new roman", 24, "bold"),
                                     command=change_my_password, fg="black", highlightbackground="green")
                 password_change_btn.grid(row=5, column=1, padx=34, pady=10, ipadx=2, ipady=2, sticky=W)

                 delete_my_ac_btn = Button(bottomFrame4, text="Delete My Account", command=delete_my_account,
                                    font=("times new roman", 24, "bold"), fg="black", highlightbackground="green")
                 delete_my_ac_btn.grid(row=6, column=1, padx=30, pady=10, ipadx=2, ipady=2, sticky=W)

                 back_change_btn = Button(bottomFrame4, text="BACK", font=("times new roman", 24, "bold"),
                                              command=back_to_myAccount, fg="black", highlightbackground="green")
                 back_change_btn.grid(row=7, column=1, padx=65, pady=10, ipadx=2, ipady=2, sticky=W)

             def forLogout():
                 """
                 This function asks for log out or not from myAccount to signUp.
                 :return: None
                 """
                 response_user = messagebox.askyesno("Log out", "Do you want to Log out ?")
                 if response_user == 1:
                     global income_fetch_first, balance_fetch_first, expense_fetch_first
                     income_fetch_first = balance_fetch_first = expense_fetch_first = 0

                     clear_entry()
                     signUp.deiconify()
                     myAccount.destroy()

             def dateToday():
                 """
                 This function shows today date as clicked on 'Date Today' button.
                 :return: None
                 """
                 DateEntry(center_frame, width=10).pack()


             #  ============================================== headline added ====================================
             heading_img = PhotoImage(file="incomeAndExpenditure.png")
             heading = Label(myAccount, text="INCOME AND EXPENSES ANALYZER", font=("Copperplate", 32, "bold"),
                             bg="silver", bd=6, relief=RIDGE)
             heading.pack(side=TOP, fill=X, expand=0)
             heading.config(image=heading_img, compound=LEFT)

             # ======================================== different frames are added ===============================
             center_frame = Frame(myAccount, bg="#7C7474", bd=6, relief=SOLID)
             center_frame.place(x=180, y=70, width=330, height=550)

             # ================================ Buttons with events are defined in center frame =====================

             myProfile_button = Button(center_frame, text="My Profile", font=("Times New Roman", 24, "bold"),
                                       command=open_profile_func, highlightbackground="green")
             myProfile_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

             income_button = Button(center_frame, text="My Income", font=("Times New Roman", 24, "bold"),
                                    command=open_income_func, highlightbackground="green", fg="black")
             income_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

             expenses_button = Button(center_frame, text="My Expenses", font=("Times New Roman", 24, "bold"),
                                    command=open_expenses_func, highlightbackground="green", fg="black")

             expenses_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

             setting_button = Button(center_frame, text="My Setting", font=("Times New Roman", 24, "bold"),
                                     command=open_setting_func,highlightbackground="green")
             setting_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

             logout_button = Button(center_frame, text="Log Out", font=("Times New Roman", 24, "bold"),
                                   command=forLogout, highlightbackground="green")
             logout_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

             date_button = Button(center_frame, text="Date Today", font=("Times New Roman", 24, "bold"),
                                    command=dateToday, highlightbackground="green")
             date_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

             myAccount.mainloop()

        else:
            messagebox.showerror("Error", "Invalid username and password.")


# for creating empty rows for a systematic management of entriews for a better look
def empty():
    """
    This creates empty spaces.
    :return:None
    """
    global row_num
    row_num += 2
    empty_row = Label(my_frame, bg="#6964EE")
    empty_row.pack()

# Labels
empty()
login_label = Label(my_frame, text="SIGNUP", font=("Copperplate", 32), bg="#6964EE", fg="white", padx=5, pady=3)
login_label.pack()
empty()


# function created to clear the entry on click or tab
def clear_username_entry(event):
    """
    This clears the username entry on clicking the entry or tab key.
    :param event: int
    :return: None
    """
    username_entry.delete(0, END)


def clear_password_entry(event):
    """
    This clears the password entry on clicking the entry or tab key.
    :param event: int
    :return: None
    """
    password_entry_signup.delete(0, END)
    password_entry_signup.configure(show="???")


# function creating to hide password as checked out in check button.
def hide_password():
    """
    This hides password.
    :return: None
    """
    password_entry_signup.configure(show="???")
    check_button.configure(command=show_password)


# function creating to show password as checked in in check button.
def show_password():
    """
    This shows paswword as checked out in check button.
    :return: None
    """
    password_entry_signup.configure(show="")
    check_button.configure(command=hide_password)

try:

    # ------------------------------------------- adding username label-------------------------------------------
    username_label = Label(my_frame, text="Username", font=("Cambria", 22, 'bold'), bg="yellow", fg="black")
    username_label.pack(ipadx=2, ipady=2)
    empty()
    # -------------------------------------------adding username entry-------------------------------------------
    username_type = StringVar()
    username_entry = Entry(my_frame, width=23, font=("Times New Roman", 19, 'italic'), textvariable=username_type)
    username_entry.pack(ipady=4)
    username_entry.insert(0, "Enter Username")

    # on clicking 'tab' key, FocusIn allows to enter information inside the username entry
    username_entry.bind("<FocusIn>", clear_username_entry)
    empty()

    # -------------------------------------------adding password label-------------------------------------------
    password_label = Label(my_frame, text="Password", font=("Cambria", 22, 'bold'), bg="yellow", fg="black")
    password_label.pack(ipadx=2, ipady=2)
    empty()
    # -------------------------------------------adding password entry-------------------------------------------
    password_type = StringVar()
    password_entry_signup = Entry(my_frame, width=23, font=("Times New Roman", 19, 'italic'),
                           textvariable=password_type, show="")
    password_entry_signup.pack(ipady=4)
    password_entry_signup.insert(0, "Enter Password")

    # on clicking 'tab' key, FocusIn allows to enter in password entry
    password_entry_signup.bind("<FocusIn>", clear_password_entry)
    empty()

except (AttributeError, NameError, ValueError, TypeError, SyntaxError) as msg:
    print(type(msg))
    print(msg)

else:
    # -------------------------------buttons with event are added-----------------------------------------
    check_button = Checkbutton(my_frame, text="Show password", fg="white", command=show_password, bg="#6964EE",
                              font=("Typewriter", 19))
    check_button.deselect()
    check_button.pack()

finally:

        empty()
        login_button = Button(my_frame, text="LOGIN", command=submit, highlightbackground="green",
                              font=("Phosphate", 32), padx=5, pady=2)
        login_button.pack()
        empty()
        noAccount_button = Button(my_frame, text="Don't have an account ?", highlightbackground="black", fg="white",
                            command=create_my_account, font=("courier", 17, "bold"), padx=10, pady=8)
        noAccount_button.pack()
        empty()
        exit_button = Button(my_frame, text="EXIT", font=("Phosphate", 30, "bold"), command=exit_signup,
                             highlightbackground="red", padx=4)
        exit_button.pack()

        # committing changes
        connector.commit()
        # closing connection between database and above created table
        connector.close()
signUp.mainloop()
