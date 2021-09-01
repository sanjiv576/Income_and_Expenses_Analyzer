"""
This module includes information of income and expenses of the user after login,
which stores, manages, updates and accesses the information as the user provides.
"""
from tkinter import *

myAccount = Tk()
myAccount.title("MY ACCOUNT")
# remaining to change icon
myAccount.iconbitmap("login.ico")
myAccount.geometry("900x700")
myAccount.configure(bg="black")
myAccount.resizable(True, True)

# ========================== headline added ======================================
heading = Label(myAccount, text="INCOME AND EXPENSES ANALYZER", font=("Copperplate", 32, "bold"), bg="silver")
heading.pack(side=TOP, fill=X, expand=0)



myAccount.mainloop()
