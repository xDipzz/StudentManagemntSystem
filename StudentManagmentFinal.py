#MADE BY DEEPAK MAHAJAN B20 EXTC TEC    


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Management System")

def fetch_data():
    conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
    curr = conn.cursor()
    curr.execute("SELECT * FROM data")
    rows = curr.fetchall()
    
    if len(rows) > 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert("", tk.END, values=row)
        conn.commit()
    
    conn.close()

def add_func():
    if rollno.get() == "" or name.get() == "" or class_var.get() == "":
        messagebox.showerror("Error!", "All fields must be filled.")
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                     (rollno.get(), name.get(), class_var.get(), section.get(), dept.get(), contact.get(), father.get(), gender.get(), address.get()))
        conn.commit()
        conn.close()
        fetch_data()

def clear_fields():
    rollno.set("")
    name.set("")
    class_var.set("")
    section.set("")
    dept.set("")
    contact.set("")
    father.set("")
    gender.set("")
    address.set("")

def delete_func():
    selected_item = student_table.selection()
    if not selected_item:
        messagebox.showerror("Error!", "No item selected.")
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        for item in selected_item:
            values = student_table.item(item, 'values')
            curr.execute("DELETE FROM data WHERE Rollno=%s", (values[0],))
            conn.commit()
            student_table.delete(item)
        conn.close()

def search_func():
    # Get the selected search criteria
    search_criteria = search_by.get()
    
    # Get the search keyword
    keyword = search_entry.get()
    
    if keyword == "":
        messagebox.showerror("Error!", "Please enter a search keyword.")
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        if search_criteria == "Name":
            query = "SELECT * FROM data WHERE Name LIKE %s"
        elif search_criteria == "Roll No":
            query = "SELECT * FROM data WHERE Rollno LIKE %s"
        elif search_criteria == "Contact":
            query = "SELECT * FROM data WHERE Contact LIKE %s"
        elif search_criteria == "Father's Name":
            query = "SELECT * FROM data WHERE Father LIKE %s"
        elif search_criteria == "Class":
            query = "SELECT * FROM data WHERE Class LIKE %s"
        elif search_criteria == "Section":
            query = "SELECT * FROM data WHERE Section LIKE %s"
        else:
            messagebox.showerror("Error!", "Invalid search criteria.")
            return
        
        # Execute the query
        curr.execute(query, ('%' + keyword + '%',))
        rows = curr.fetchall()
        
        # Clear the treeview
        student_table.delete(*student_table.get_children())
        
        if len(rows) > 0:
            # Populate the treeview with search results
            for row in rows:
                student_table.insert("", tk.END, values=row)
            conn.commit()
        else:
            messagebox.showinfo("Info", "No matching records found.")
        
        conn.close()

# Title label
title_label = tk.Label(win, text="Student Management System", font=("Arial", 36, "bold"), bd=12, relief=tk.GROOVE, bg="lightgrey")
title_label.pack(side=tk.TOP, fill=tk.X)

# Detail frame
detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Arial", 20), bd=12, relief=tk.GROOVE, bg="lightgrey")
detail_frame.place(x=20, y=90, width=420, height=575)

# Roll No
rollno_lbl = tk.Label(detail_frame, text="Roll No", font=("Arial", 15), bg="lightgrey")
rollno_lbl.grid(row=0, column=0, padx=2, pady=2)

rollno = tk.StringVar()
rollno_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=rollno)
rollno_ent.grid(row=0, column=1, padx=2, pady=2)

# Name
name_lbl = tk.Label(detail_frame, text="Name", font=("Arial", 15), bg="lightgrey")
name_lbl.grid(row=1, column=0, padx=2, pady=2)

name = tk.StringVar()
name_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=name)
name_ent.grid(row=1, column=1, padx=2, pady=2)

# Class
class_lbl = tk.Label(detail_frame, text="Class", font=("Arial", 15), bg="lightgrey")
class_lbl.grid(row=2, column=0, padx=2, pady=2)

class_var = tk.StringVar()
class_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=class_var)
class_ent.grid(row=2, column=1, padx=2, pady=2)

# Section
section_lbl = tk.Label(detail_frame, text="Section", font=("Arial", 15), bg="lightgrey")
section_lbl.grid(row=3, column=0, padx=2, pady=2)

section = tk.StringVar()
section_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=section)
section_ent.grid(row=3, column=1, padx=2, pady=2)

# Department
dept_lbl = tk.Label(detail_frame, text="Department", font=("Arial", 15), bg="lightgrey")
dept_lbl.grid(row=4, column=0, padx=2, pady=2)

dept = tk.StringVar()
dept_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=dept)
dept_ent.grid(row=4, column=1, padx=2, pady=2)

# Contact No
contact_lbl = tk.Label(detail_frame, text="Contact No", font=("Arial", 15), bg="lightgrey")
contact_lbl.grid(row=5, column=0, padx=2, pady=2)

contact = tk.StringVar()
contact_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=contact)
contact_ent.grid(row=5, column=1, padx=2, pady=2)

# Father's Name
father_lbl = tk.Label(detail_frame, text="Father's Name", font=("Arial", 15), bg="lightgrey")
father_lbl.grid(row=6, column=0, padx=2, pady=2)

father = tk.StringVar()
father_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=father)
father_ent.grid(row=6, column=1, padx=2, pady=2)

# Gender
gender_lbl = tk.Label(detail_frame, text="Gender", font=("Arial", 15), bg="lightgrey")
gender_lbl.grid(row=7, column=0, padx=2, pady=2)

gender = tk.StringVar()
gender_combobox = ttk.Combobox(detail_frame, textvariable=gender, values=["Male", "Female", "Other"], font=("Arial", 15), state="readonly")
gender_combobox.grid(row=7, column=1, padx=2, pady=2)
gender_combobox.current(0) 

# Address
address_lbl = tk.Label(detail_frame, text="Address", font=("Arial", 15), bg="lightgrey")
address_lbl.grid(row=8, column=0, padx=2, pady=2)

address = tk.StringVar()
address_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=address)
address_ent.grid(row=8, column=1, padx=2, pady=2)

# Button frame
btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=18, y=390, width=350, height=120)

# Add button
add_btn = tk.Button(btn_frame, text="Add", font=("Arial", 13), bd=7, width=15, bg="lightgrey", command=add_func)
add_btn.grid(row=0, column=0, padx=2, pady=2)

# Update button
update_btn = tk.Button(btn_frame, text="Update", font=("Arial", 13), bd=7, width=15, bg="lightgrey")
update_btn.grid(row=0, column=1, padx=3, pady=2)

# Delete button
delete_btn = tk.Button(btn_frame, text="Delete", font=("Arial", 13), bd=7, width=15, bg="lightgrey", command=delete_func)
delete_btn.grid(row=1, column=0, padx=2, pady=2)

# Clear button
clear_btn = tk.Button(btn_frame, text="Clear", font=("Arial", 13), bd=7, width=15, bg="lightgrey", command=clear_fields)
clear_btn.grid(row=1, column=1, padx=3, pady=2)

# Data frame
data_frame = tk.Frame(win, bd=12, bg="lightgrey", relief=tk.GROOVE)
data_frame.place(x=475, y=90, width=810, height=575)


# Search frame
search_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

# Search label
search_lbl = tk.Label(search_frame, text="Search", bg="lightgrey", font=("Arial", 14))
search_lbl.grid(row=0, column=0, padx=12, pady=2)

# Search combobox
search_by = tk.StringVar()
search_combobox = ttk.Combobox(search_frame, textvariable=search_by, font=("Arial", 14), state="readonly")
search_combobox['values'] = ("Name", "Roll No", "Contact", "Father's Name", "Class", "Section")
search_combobox.grid(row=0, column=1, padx=12, pady=2)

# Search entry
search_entry = tk.Entry(search_frame, bd=7, font=("Arial", 15))
search_entry.grid(row=0, column=2, padx=12, pady=2)

# Search button
search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), bd=9, width=14, bg="lightgrey", command=search_func)
search_btn.grid(row=0, column=3, padx=12, pady=2)

# Show all button
showall_btn = tk.Button(search_frame, text="Show All", font=("Arial", 13), bd=9, width=14, bg="lightgrey", command=fetch_data)
showall_btn.grid(row=0, column=4, padx=12, pady=2)

# Main frame
main_frame = tk.Frame(data_frame, bg="lightgrey", bd=11, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

# Vertical scrollbar
y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Horizontal scrollbar
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

# Columns for the treeview
columns = ("Roll No.", "Name", "Class", "Section","Department","Contact ", "Father's Name", "Gender", "Address")

# Treeview
student_table = ttk.Treeview(main_frame, columns=columns, yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

# Configuring scrollbar commands
y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

# Heading for each column
student_table.heading("Roll No.", text="Roll No.")
student_table.heading("Name", text="Name")
student_table.heading("Class", text="Class")
student_table.heading("Section", text="Section")
student_table.heading("Department", text="Department")
student_table.heading("Contact ", text="Contact")
student_table.heading("Father's Name", text="Father's Name")
student_table.heading("Gender", text="Gender")
student_table.heading("Address", text="Address")

student_table['show'] = 'headings'

# Setting column widths
student_table.column("Roll No.", width=100)
student_table.column("Name", width=100)
student_table.column("Class", width=100)
student_table.column("Section", width=100)
student_table.column("Department", width=100)
student_table.column("Contact ", width=100)
student_table.column("Father's Name", width=100)
student_table.column("Gender", width=100)
student_table.column("Address", width=150)

# Packing treeview
student_table.pack(fill=tk.BOTH, expand=True)

fetch_data()

# Running the application
win.mainloop()
