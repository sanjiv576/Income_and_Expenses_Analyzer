"""
This module accepts username and password to signup.
"""
from tkinter import *
from tkinter import messagebox


signUp = Tk()
signUp.title("SIGNUP")
signUp.geometry("980x600")
signUp.iconbitmap("login.ico")
signUp.configure(bg="white")
signUp.resizable(1, 1)

# Note : 433 x 371 pixel image
left_img = PhotoImage(file="login_img.png")
img_label = Label(signUp, image=left_img)
img_label.place(x=40, y=30)

my_frame = Frame(signUp)
my_frame.place(x=640, y=30, width=300, height=490)
# adding blue color i.e #6964EE in the frame
my_frame.config(bg="#6964EE")


# creating a new window for registration
# -----------------------------------Coding for Registration Form starts ----------------------------------
vacant_row = 0
def create_my_account():
    """
    This accepts user's full name, gender, username and password as string to create an account for official use.
    :return to : login page
    """
    signUp.withdraw()
    register = Toplevel()
    register.title("Registration Forum")
    register.iconbitmap("agree_0.ico")
    register.geometry("740x749")
    register.configure(bg="#CDC8B1")  # #CDC8B1 = silkcorn color
    '''
    create_image = PhotoImage(file="account_create.png")
    Label(register, image=create_image)
    #create_image.grid(row=1, column=2)

    img_button = Button(register, image=create_image)
    img_button.grid(row=1, column=3)'''

    # frame created to maintain buttons and labels in a systematic arrangement
    my_frame = Frame(register, bg="#CDC8B1")
    my_frame.pack()

    # function for show message

    def show_message():
        if f_nam_entry.get() == "" and l_nam_entry.get() == "" and user_name_entry.get() == "" and \
                password_entry.get() == "" and conf_password_entry.get() == "":
            messagebox.showwarning("Warning Encountered ! ", "Please , fill all boxes.")
        elif f_nam_entry.get() == "":
            messagebox.showwarning("Warning Encountered ! ", "Please , fill first name box.")
        elif l_nam_entry.get() == "":
            messagebox.showwarning("Warning Encountered ! ", "Please , fill last name box.")
        elif user_name_entry.get() == "":
            messagebox.showwarning("Warning Encountered ! ", "Please , fill  username box.")

        elif password_entry.get() == "":
            messagebox.showwarning("Warning Encountered ! ", "Please , fill  password box.")

        elif conf_password_entry.get() == "":
            messagebox.showwarning("Warning Encountered ! ", "Please , fill  confirm password box.")
        elif conf_password_entry.get() != password_entry.get():  # checking password and confirm password match or not
            messagebox.showwarning("Warning Encountered ! ",
                                   "Password and Confirm password do not match. Please, enter again.")
        else:
            messagebox.showinfo("Account Created", "Congratulation! Your account has been created successfully.")
            signUp.deiconify()
            register.destroy()


    # function to show msg for exit window
    def show_quit():
        user_respond = messagebox.askokcancel("Warning !", "Do you want to quit ? ")
        if user_respond == 1:

            register.destroy()

    # function for empty labels

    def empty_row():
        global vacant_row
        if vacant_row <= 30:
            empty_label = Label(my_frame, text="", bg="#CDC8B1")
            empty_label.grid(row=vacant_row)
            vacant_row += 2
    # function created to go back to the previous window
    def previous_window():
        global vacant_row
        vacant_row = 0
        signUp.deiconify()
        register.destroy()
    # labels
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

    # button defined
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
        gender = ["Male", "Female", "Others", "Prefer not to say"]
        indicator = StringVar()
        indicator.set("Male")
        dropper = OptionMenu(my_frame, indicator, *gender)
        dropper.grid(row=7, column=1, ipadx=60, ipady=3)
        dropper.config(bg="#CDC8B1")

    dropDown()


    # entry fields
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

    conf_password_entry = Entry(my_frame, bd=2, bg="#474747", fg="white",
                                show="•", font=("cambria", 16, 'italic'))
    conf_password_entry.grid(row=13, column=1, ipadx=60, ipady=3)

    # Slider added
    def geometry_change():
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
def exit_signup():
    response = messagebox.askyesno("Quit", "Do you want to quit ?")
    if response == 1:
        signUp.quit()


def submit():

    if (username_entry.get() == "Username" and password_entry.get() == "Password") or (username_entry.get() == "" and password_entry.get() == ""):
        messagebox.showwarning("Error", "Please, fill both username and password boxes.")
    elif username_entry.get() == "" or username_entry.get() == "Username":
        messagebox.showerror("Error", "Please, fill username box.")
    elif password_entry.get() == "" or password_entry.get() == "Password":
        messagebox.showerror("Error", "Please, fill password box.")
    else:
        messagebox.showinfo("Signed up", "Provided credentials are correct.")


def empty():
    global row_num
    row_num += 2
    empty_row = Label(my_frame, bg="#6964EE")
    empty_row.pack()


empty()

login_label = Label(my_frame, text="SIGNUP", font=("Copperplate", 32), bg="#6964EE", fg="white", padx=5, pady=3)
login_label.pack()
empty()


# function created to clear the entry on click or tab
def clear_username_entry(event):
    username_entry.delete(0, END)


def clear_password_entry(event):
    password_entry.delete(0, END)
    password_entry.configure(show="•")


# function creating to hide password
def hide_password():
    password_entry.configure(show="•")
    check_button.configure(command=show_password)


# function creating to show password
def show_password():
    password_entry.configure(show="")
    check_button.configure(command=hide_password)

try:
    # adding username entry
    username_type = StringVar()
    username_entry = Entry(my_frame, width=23, font=("Times New Roman", 19, 'italic'), textvariable=username_type)
    username_entry.pack(ipady=4)
    username_entry.insert(0, "Username")
    # on clicking 'tab' key FocusIn allows to enter in username entry
    username_entry.bind("<FocusIn>", clear_username_entry)
    empty()

    # adding password entry
    password_type = StringVar()
    password_entry = Entry(my_frame, width=23, font=("Times New Roman", 19, 'italic'),
                           textvariable=password_type, show="")
    password_entry.pack(ipady=4)
    password_entry.insert(0, "Password")
    # on clicking 'tab' key FocusIn allows to enter in password entry
    password_entry.bind("<FocusIn>", clear_password_entry)
    empty()

    check_button = Checkbutton(my_frame, text="Show password", fg="white", command=show_password, bg="#6964EE",
                              font=("Typewriter", 19))
    check_button.pack()
    """
    login_img = PhotoImage(file="login_128px.png")
    login_button = Button(my_frame, highlightbackground="#6964EE", image=login_img, borderwidth=0, pady=6, padx=0)
    login_button.pack()
    """
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


except (ValueError, TypeError, SyntaxError) as msg:
    print(type(msg))
    print(msg)

except BaseException as e:
    print(type(e))
    print(e)


signUp.mainloop()
