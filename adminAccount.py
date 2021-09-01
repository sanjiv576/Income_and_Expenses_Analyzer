"""
This module administrates Signup details of the users.
"""
from tkinter import *
import sqlite3
def open_adminAccount():
    adminAccount = Toplevel()
    adminAccount.title("Admin")
    adminAccount.geometry("400x300")

    # ------------------------------------- DATABASE -----------------------------
    def show_records():
        connector = sqlite3.connect("Accounts_details_holder.db")
        cur = connector.cursor()
        # showing all recorded information of the users.
        cur.execute("SELECT *, oid FROM registration_details_holder")
        all_records = cur.fetchall()
        print(all_records)
        records_on_win = ""
        try:
            for info in all_records:  # each inserted info in tuple
                records_on_win += str(info[0]) + " " + str(info[1]) + " " + str(info[2]) + " " + str(info[3]) \
                                  + " " + str(info[4]) + " " + str(info[5]) + " oid:" + str(info[6]) + "\n"

        except BaseException as e:
            print(type(e))
            print(e)

        query_label = Label(adminAccount, text=records_on_win)
        query_label.grid(row=4, column=1)
    # ======================= labels are defined ================================
    id_label = Label(adminAccount, text="ID", font=("Copper", 19, "bold"))
    id_label.grid(row=0, column=0)

    # ====================Buttons are defined with events ====================================
    delete_button = Button(adminAccount, text="DELETE", font=("Helvetica", 19, "italic"), padx=3,
                           pady=4, highlightbackground="red", fg="green")
    delete_button.grid(row=1, column=1)
    show_button = Button(adminAccount, text="SHOW ADDED RECORDS ", font=("Helvetica", 19, "italic"),command=show_records,
                         padx=3, pady=4, highlightbackground="yellow", fg="blue")
    show_button.grid(row=2, column=1, ipadx=5, ipady=7)


    # =============================== Entries are added ======================================
    id_entry = Entry(adminAccount, bd=3, width=30)
    id_entry.grid(row=0, column=1)
    adminAccount.mainloop()

"""
 
                for inner in info:  # 0, 1, 2, 3, 4, 5  in tuple
                    all_inputs_lst = {0: "First name : ", 1: "Last name : ", 2: "Gender : ", 3: "Contact : ", 4: "Username : ",
                                      5: "Password", 6: "OID"}
                    for inner_inner, category_name in all_inputs_lst.items():  # 0, 1, 2, 3, 4, 5, 6
                        if info.index[inner] == all_inputs_lst[inner_inner]:
                            print(category_name + str(inner) + "\n")

                print("Finished loop")
                print(info)
                print()
               
                """