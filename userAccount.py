"""
This module includes information of income and expenses of the user after login,
which stores, manages, updates and accesses the information as the user provides.
"""
from tkinter import *
def open_userAccount():
    myAccount = Toplevel()
    myAccount.title("MY ACCOUNT")
    # remaining to change icon
    myAccount.iconbitmap("login.ico")
    myAccount.geometry("800x700")
    myAccount.configure(bg="black")
    myAccount.resizable(True, True)
    left_win = PanedWindow(myAccount, bg="yellow", height=600, width=200)
    left_win.pack(fill=Y, expand=1, side=LEFT)
    top_win = PanedWindow(myAccount, bg="red", height=50, width=600)
    top_win.pack(fill=Y, expand=1, side=TOP)
    center_win = PanedWindow(myAccount, bg="green", height=650)
    center_win.pack(fill=BOTH, expand=True)
    myAccount.mainloop()
