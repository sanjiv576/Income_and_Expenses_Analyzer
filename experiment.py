
"""
contact = input("Enter something ")
def check(contact):
    for i in contact:
        a = ord(i)
        if i.isdigit():
            return True
        else:
            return False

print(check(contact))"""
all_records = [('Sanjiv', 'Shrestha', 'Male', 9800000000, 'admin11', 'admin', 1),
               ('Sangit', 'Karki', 'Male', 9800001000, 'sangit', 'sangit123', 2),
               ('Sanjiv', 'Shrestha', 'Male', 9800000000, 'admin12', 'admin', 1)]
all_inputs_lst = {0: "First name : ", 1: "Last name : ", 2: "Gender : ", 3: "Contact : ", 4: "Username : ",
                                      5: "Password", 6: "OID"}
for info in all_records:
     print(info)
     for j in info:
         print(j)
         if info.index(j) == 4 or info.index(j) == 5:
             if info.index(j) == 4:
                 fetched_info = j
             else:
                 l = [fetched_info, j]
                 for check in l:

                 print(l)
                # l.append(j)





"""
from tabulate import *
all_records = [("First Name ", "Last Name", "Gender", "Contact", "Username", "Password", "OID") ,('Sanjiv', 'Shrestha', 'Male', 9800000000, 'admin', 'admin', 1),
               ('Sangit', 'Karki', 'Male', 9800001000, 'sangit', 'sangit123', 2)]
print(tabulate(all_records, headers='firstrow', tablefmt='fancy_grid'))
"""
