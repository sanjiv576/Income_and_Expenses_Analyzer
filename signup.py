"""
This module accepts username and password to signup.
"""
from tkinter import *
from tkinter import messagebox


signUp = Tk()
signUp.title("SIGNUP")
# resolution of the window changes
signUp.geometry("980x700")
# inserting icon
signUp.iconbitmap("login.ico")
signUp.configure(bg="white")
# allowing to the user to maximize the window resolution
signUp.resizable(1, 1)

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
    register.geometry("740x749")
    # not allowing to maximize the Registration Form
    register.resizable(0, 0)
    register.configure(bg="#CDC8B1")  # #CDC8B1 = silkcorn color
    '''
    create_image = PhotoImage(file="account_create.png")
    Label(register, image=create_image)
    #create_image.grid(row=1, column=2)

    img_button = Button(register, image=create_image)
    img_button.grid(row=1, column=3)'''

    # frame is created to maintain buttons and labels in a systematic arrangement
    my_frame = Frame(register, bg="#CDC8B1")
    my_frame.pack()
    # function for showing  messages as clicked on 'SUBMIT' button
    def show_message():
        """
        This function alerts the user if he/she gives invalid details or leaves entries empty.
        :return: None
        """
        if f_nam_entry.get() == "" and l_nam_entry.get() == "" and user_name_entry.get() == "" and \
                password_entry.get() == "" and conf_password_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill all boxes.")
        elif f_nam_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill first name box.")
        elif l_nam_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill last name box.")
        elif user_name_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill  username box.")

        elif password_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill  password box.")

        elif conf_password_entry.get() == "":
            messagebox.showwarning("EMPTY! ", "Please , fill  confirm password box.")
        elif conf_password_entry.get() != password_entry.get():  # checking password and confirm password match or not
            messagebox.showerror("INCORRECT PASSWORD! ", "Password and Confirm password do not match. Please, enter again.")
        else:
            messagebox.showinfo("Account Created", "Congratulation! Your account has been created successfully.")
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
    user_name = Label(my_frame, text="Username :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
    username = StringVar()
    user_name.grid(row=9, column=0)
    empty_row()
    password_label = Label(my_frame, text="Password :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
    password = StringVar()
    password_label.grid(row=11, column=0)
    empty_row()
    conf_password_label = Label(my_frame, text="Confirm Password :", bg="#CDC8B1", font=("Times New Roman", 21, 'bold'))
    confirm_password = StringVar()
    conf_password_label.grid(row=13, column=0)
    empty_row()

    # --------------------------------------------buttons are defined along with events--------------------------------
    submit_button = Button(my_frame, text="SUBMIT", highlightbackground="green", command=show_message,
                           font=("Century Gothic", 24, 'bold'))
    submit_button.grid(row=15, column=1, ipadx=18, ipady=3)
    empty_row()
    exit_button = Button(my_frame, text="EXIT", highlightbackground="red", command=show_quit,
                         font=("Century Gothic", 24, 'bold'))
    exit_button.grid(row=17, column=1, ipadx=18, ipady=3, rowspan=2)
    empty_row()
    previous_window_btn = Button(my_frame, text="<<<", highlightbackground="red", command=previous_window,
                         font=("Copper", 24, 'bold'))
    previous_window_btn.grid(row=21, column=1)

    # drop down menu for gender
    def dropDown():
        """
        This function creates drop down menu including Male, Female , Others and Prefer not to say
        :return: string
        """
        gender = ["Male", "Female", "Others", "Prefer not to say"]
        indicator = StringVar()
        indicator.set("Male")
        dropper = OptionMenu(my_frame, indicator, *gender)
        dropper.grid(row=7, column=1, ipadx=60, ipady=3)
        dropper.config(bg="#CDC8B1")
        return indicator

    dropDown()


    # --------------------------------------------Entries are defined-----------------------------------
    f_nam_entry = Entry(my_frame, bg="#474747", fg="white", font=("cambria", 16, 'italic'))
    f_nam_entry.grid(row=3, column=1, ipadx=60, ipady=3)

    l_nam_entry = Entry(my_frame, bd=2, bg="#FFD39B", font=("cambria", 16, 'italic'))
    #  #FFD39B= burlywood1
    l_nam_entry.grid(row=5, column=1, ipadx=60, ipady=3)

    user_name_entry = Entry(my_frame, bd=2, bg="#474747", fg="white", textvariable=username,
                            font=("cambria", 16, 'italic'))
    user_name_entry.grid(row=9, column=1, ipadx=60, ipady=3)

    password_entry = Entry(my_frame, bd=2, bg="#FFD39B", textvariable=password, show="•",
                           font=("cambria", 16, 'italic'))
    password_entry.grid(row=11, column=1, ipadx=60, ipady=3)

    conf_password_entry = Entry(my_frame, bd=2, bg="#474747", fg="white", textvariable=confirm_password,
                                show="•", font=("cambria", 16, 'italic'))
    conf_password_entry.grid(row=13, column=1, ipadx=60, ipady=3)

    # Slider added
    def geometry_change():
        """
        This changes geometry of Registration Form as the user wants.
        :return: None
        """
        register.geometry(str(length_scale.get()) + "x" + str(height_scale.get()))

    empty_row()
    height_scale = Scale(my_frame, from_=100, to=1000, orient=VERTICAL)
    height_scale.grid(row=19, column=3)
    height_scale.set(749)  # this set function shows first geometry of height
    Label(my_frame, text="Height", bg="#CDC8B1").grid(row=20, column=3)
    empty_row()
    length_scale = Scale(my_frame, from_=50, to=1500, orient=HORIZONTAL)
    length_scale.grid(row=19, column=0)
    Label(my_frame, text="Length", bg="#CDC8B1").grid(row=20, column=0)
    length_scale.set(740)  # this shows first geometry of length of the window

    geometry_change_btn = Button(my_frame, text="Change window size", command=geometry_change,
                                 padx=9, pady=9, highlightbackground="yellow")
    geometry_change_btn.grid(row=19, column=1)
    empty_row()
    register.mainloop()
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

    if (username_entry.get() == "Enter Username" and password_entry.get() == "Enter Password") or (username_entry.get() == "" and password_entry.get() == ""):
        messagebox.showwarning("Error", "Please, fill both username and password boxes.")
    elif username_entry.get() == "" or username_entry.get() == "Enter Username":
        messagebox.showerror("Error", "Please, fill username box.")
    elif password_entry.get() == "" or password_entry.get() == "Enter Password":
        messagebox.showerror("Error", "Please, fill password box.")
    else:
        messagebox.showinfo("Signed up", "Provided credentials are correct.")

# for creating empty rows for a systematic management of entries for a better look
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
    password_entry.delete(0, END)
    password_entry.configure(show="•")


# function creating to hide password as checked out in check button.
def hide_password():
    """
    This hides password.
    :return: None
    """
    password_entry.configure(show="•")
    check_button.configure(command=show_password)


# function creating to show password as checked in in check button.
def show_password():
    """
    This shows paswword as checked out in check button.
    :return: None
    """
    password_entry.configure(show="")
    check_button.configure(command=hide_password)

try:

    # adding username label
    username_label = Label(my_frame, text="Username", font=("Cambria", 22, 'bold'), bg="yellow", fg="black")
    username_label.pack(ipadx=2, ipady=2)
    empty()
    # adding username entry
    username_type = StringVar()
    username_entry = Entry(my_frame, width=23, font=("Times New Roman", 19, 'italic'), textvariable=username_type)
    username_entry.pack(ipady=4)
    username_entry.insert(0, "Enter Username")

    # on clicking 'tab' key, FocusIn allows to enter information inside the username entry
    username_entry.bind("<FocusIn>", clear_username_entry)
    empty()

    # adding password label
    password_label = Label(my_frame, text="Password", font=("Cambria", 22, 'bold'), bg="yellow", fg="black")
    password_label.pack(ipadx=2, ipady=2)
    empty()
    # adding password entry
    password_type = StringVar()
    password_entry = Entry(my_frame, width=23, font=("Times New Roman", 19, 'italic'),
                           textvariable=password_type, show="")
    password_entry.pack(ipady=4)
    password_entry.insert(0, "Enter Password")

    # on clicking 'tab' key, FocusIn allows to enter in password entry
    password_entry.bind("<FocusIn>", clear_password_entry)
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

signUp.mainloop()
