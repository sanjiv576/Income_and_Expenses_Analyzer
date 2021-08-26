'''
This module accepts username and password to signup.
'''
from tkinter import *
from tkinter.ttk import Notebook
signUp = Tk()
signUp.title("SIGNUP")
signUp.geometry("840x500")
signUp.iconbitmap("login.ico")
signUp.configure(bg="white")
signUp.resizable(1, 1)

"""tab = Notebook(signUp)
frame1 = Frame(tab, width=500, height=700)
frame2 = Frame(tab)"""

# Note : 433 x 371 pixel image
left_img = PhotoImage(file="login_bg.png")
img_label = Label(signUp, image=left_img)
img_label.place(x=40, y=30)

my_frame = Frame(signUp)
my_frame.place(x=500, y=30, width=300, height=371)
# adding blue color i.e #6964EE in the frame
my_frame.config(bg="#6964EE")
row_num = 0


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

# function creating to hide password


def hide_password():
    password_entry.configure(show="•")
    check_button.configure(command=show_password, text="Show password")

# function creating to show password


def show_password():
    password_entry.configure(show="")
    check_button.configure(command=hide_password, text="Hide password")


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
    password_entry = Entry(my_frame, width=20, font=("Times New Roman", 19, 'italic'),
                           textvariable=password_type, show="")
    password_entry.pack()
    password_entry.insert(0, "Password")
    # on clicking 'tab' key FocusIn allows to enter in password entry
    password_entry.bind("<FocusIn>", clear_password_entry)
    empty()
    check_button = Checkbutton(my_frame, text="Hide password", command=hide_password, bg="#6964EE")
    check_button.pack()

except (ValueError, TypeError) as msg:
    print(type(msg))
    print(msg)

except BaseException as e:
    print(type(e))
    print(e)
else:
    empty()
"""
username_label = Label(my_frame, text="Username", font=("Copperplate", 16, 'bold'))
username_label.pack()"""


"""bg_frame = Label(frame1, image=background_img,)
bg_frame.place(x=0, y=0, relwidth=1, relheight=1)

Label(bg_frame, text="hello").place(x=142, y=78)"""



signUp.mainloop()
