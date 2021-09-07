"""
This module accepts username and password to signup.
"""
from tkinter import *
from tkinter import messagebox
import sqlite3
#from userAccount import open_userAccount
from adminAccount import open_adminAccount
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


# creating a new window for registration as clicked on 'Don't have an account ?' button
# -----------------------------------Coding for Registration Form starts ----------------------------------
vacant_row = 0
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
        print(selected_gender)
        # checking whether entered information in 'Contact' entry are digits or not
        for check in contact_entry.get():
            if check.isdigit():
                inserted_info = True
            else:
                inserted_info = False
                break

        if f_nam_entry.get() == "" and l_nam_entry.get() == "" and user_name_entry.get() == "" and contact_entry.get() =="" and \
                password_entry.get() == "" and conf_password_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill all boxes.")

        elif f_nam_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill first name box.")

        elif l_nam_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill last name box.")

        elif contact_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill  confirm password box.")

        elif inserted_info is False:
            messagebox.showerror("INVALID!", "Please, insert numbers in contact box.")

        elif user_name_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill  username box.")

        elif password_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill  password box.")

        elif conf_password_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill  confirm password box.")

        # checking password and confirm password match or not
        elif conf_password_entry.get() != password_entry.get():
            messagebox.showerror("INCORRECT PASSWORD! ", "Password and Confirm password do not match. Please, enter again.")

        else:
            messagebox.showinfo("Account Created", "Congratulation! Your account has been created successfully.")

            # Insertion database is here

            # -------------All details are inserted into the table of Database i.e registration_details-------------
            connect_me = sqlite3.connect("Accounts_details_holder.db")
            cu = connect_me.cursor()
            # inserting details into the table
            cu.execute("INSERT INTO registration_details_holder VALUES(:f_name, :l_name, :gender_type,"
                         ":contact_num, :username_entered, :password_entered)", {
                  'f_name':f_nam_entry.get(),
                  'l_name':l_nam_entry.get(),
                  'gender_type':selected_gender,
                  'contact_num':contact_entry.get(),
                  'username_entered':user_name_entry.get(),
                  'password_entered':password_entry.get()
              })

              # filling all entry fields or not
            print("Information are inserted successfully.")
            messagebox.showinfo("Records insertion", "Information have been inserted successfully.")
            connect_me.commit()
            connect_me.close()
            # clearing the entry fields after inserting info
            user_name_entry.delete(0, END)
            l_nam_entry.delete(0, END)
            #selected_gender.delete(0, END)
            contact_entry.delete(0, END)
            user_name_entry.delete(0, END)
            password_entry.delete(0, END)

         # revealing Signup window after creating the account for login
            signUp.deiconify()
            # quitting the Registration Form window after successfully creating account.
            register.destroy()


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
        print(type(username))
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

            password_entry = Entry(my_frame, bd=2, bg="#474747", textvariable=password, show="•", fg="white",
                                   font=("cambria", 16, 'italic'))
            password_entry.grid(row=13, column=1, ipadx=60, ipady=3)

            conf_password_entry = Entry(my_frame, bd=2, bg="#FFD39B", fg="black", textvariable=confirm_password,
                                        show="•", font=("cambria", 16, 'italic'))
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

# function for exiting Signup window as clicked on "EXIT" button.
def exit_signup():
    """
    This function asks confirmation from the user to quit the Signup window.
    :return: None
    """
    response = messagebox.askyesno("Quit", "Do you want to quit ?")
    if response == 1:
        signUp.quit()

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
        open_adminAccount()

    else:

        connetor = sqlite3.connect("Accounts_details_holder.db")
        cur = connetor.cursor()
        query = "Select * from registration_details_holder where username=? and password=?"

        cur.execute(query,(username_entry.get(), password_entry_signup.get()))
        rows = cur.fetchall()
        # checking whether it is empty or not, if empty shows error message , if no allows to login
        if len(rows) > 0:
         messagebox.showinfo("Account Created", "Login has been successfully done")

         # --------------------------------- User account GUI and database are started ------------------------------
         signUp.withdraw()
         myAccount = Toplevel()
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
             finding_oid_value = 1
             # frames are added
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
             income_label = Label(bottomFrame, text="Income", font=("courier", 25, "bold"), fg="yellow", bg="green")
             income_label.grid(row=0, column=0, columnspan=1, padx=50, pady=10)

             spend_label = Label(bottomFrame, text="Expenses", font=("courier", 25, "bold"), fg="yellow",
                                 bg="green")
             spend_label.grid(row=0, column=2, columnspan=1, padx=50, pady=10)

             balance_label = Label(bottomFrame, text="Balance", font=("courier", 25, "bold"), fg="yellow",
                                   bg="green")
             balance_label.grid(row=0, column=4, columnspan=1, padx=50, pady=10)

             # ------------------------- values of respective labels are given ------------------------

             income_value = Label(bottomFrame, text="$" + str(income), font=("courier", 25, "bold"), fg="black",
                                  bg="red")
             income_value.grid(row=1, column=0, columnspan=1, padx=50, pady=10)

             spend_value = Label(bottomFrame, text="$" + str(spend), font=("courier", 25, "bold"), fg="black",
                                 bg="red")
             spend_value.grid(row=1, column=2, columnspan=1, padx=50, pady=10)

             balance_value = Label(bottomFrame, text="$" + str(balance), font=("courier", 25, "bold"), fg="black",
                                   bg="red")
             balance_value.grid(row=1, column=4, columnspan=1, padx=50, pady=10)

             # ------------------------------------ Basic details of the user-------------------------------------
             connect_me = sqlite3.connect("Accounts_details_holder.db")
             cur = connect_me.cursor()
             cur.execute("SELECT password,first_name, last_name, gender, contact, oid FROM registration_details_holder")
             fetch_data = cur.fetchall()
             print(fetch_data)
             # Searching details of the particular user and matching his/her password
             # from the database to fetch his/her other details for showing details on the screen

             for password_search, first_name_search, last_name_search, gender_search, contact_search,oid_search in fetch_data:  # [(username, oid), (username, oid), ..]
                 print(password_search, oid_search)  # (username, oid)

                 if password_search == password_entry_signup.get():
                     first_name_found = first_name_search
                     last_name_found = last_name_search
                     gender_found = gender_search
                     contact_found = contact_search
                     oid_found = oid_search
                     print(first_name_found, last_name_found, gender_found, contact_found, oid_found)
                     break


             # ---------------------Now, details are shoving on the screen------------------

             full_name_show = first_name_found +" "+ last_name_found
             gender_show = gender_found
             contact_show = contact_found
             username_show = username_entry.get()
             oid_show = oid_found

             user_fullName = Label(bottomFrame, text=f"Name : {full_name_show}", font=("courier", 25, "bold"), fg="black",
                                   bg="red")
             user_fullName.grid(row=2, column=0, columnspan=3, padx=50, pady=10, sticky=W)

             user_gender = Label(bottomFrame, text=f"Gender : {gender_show}", font=("courier", 25, "bold"),
                                   fg="black", bg="red")
             user_gender.grid(row=3, column=0, columnspan=3, padx=50, pady=10, sticky=W)

             user_contact = Label(bottomFrame, text=f"Contact : {contact_show}", font=("courier", 25, "bold"),
                                   fg="black", bg="red")
             user_contact.grid(row=4, column=0, columnspan=3, padx=50, pady=10, sticky=W)

             user_username = Label(bottomFrame, text=f"Username : {username_show}", font=("courier", 25, "bold"),
                                   fg="black", bg="red")
             user_username.grid(row=5, column=0, columnspan=3, padx=50, pady=10, sticky=W)

             user_oid = Label(bottomFrame, text=f"Oid number : {oid_show}", font=("courier", 25, "bold"),
                                   fg="black", bg="red")
             user_oid.grid(row=6, column=0, columnspan=3, padx=50, pady=10, sticky=W)

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

         myProfile_button = Button(center_frame, text="My Profile", font=("Times New Roman", 24, "bold"),
                                   command=open_profile_func,
                                   highlightbackground="green")
         myProfile_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

         income_button = Button(center_frame, text="My Income", font=("Times New Roman", 24, "bold"),
                                command=open_income_func,
                                highlightbackground="green", fg="black")
         income_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

         setting_button = Button(center_frame, text="My Setting", font=("Times New Roman", 24, "bold"),
                                 command=open_setting_func,
                                 highlightbackground="green")
         setting_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

         logout_button = Button(center_frame, text="Log Out", font=("Times New Roman", 24, "bold"),
                                highlightbackground="green")
         logout_button.pack(padx=54, pady=20, ipadx=4, ipady=6)

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
    password_entry_signup.configure(show="•")


# function creating to hide password as checked out in check button.
def hide_password():
    """
    This hides password.
    :return: None
    """
    password_entry_signup.configure(show="•")
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
