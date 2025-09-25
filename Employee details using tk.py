import tkinter as tk
from tkinter import messagebox
import mysql.connector


DB_HOST = "localhost"
DB_USER = "root"       
DB_PASSWORD = "Mohan@13"        
DB_NAME = "employee_db" 

def create_table():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employee_db(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                gender TEXT,
                department TEXT,
                salary REAL
            )
        """)
        conn.commit()
        conn.close()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        

        
def submit_details():
     
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    department = entry_dept.get()
    salary = entry_salary.get()

    if not name or not age or not department or not salary:
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    try:
        
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    
        cur = conn.cursor()
        cur.execute("INSERT INTO employee_db (name, age, gender, department, salary) VALUES (%s, %s, %s, %s, %s)",
            (name, int(age), gender, department, float(salary)))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Employee details saved successfully!")
        clear_form()
        
    except Exception as e:
        messagebox.showerror("Database Error", str(e))


def search_employee():
    id = entry_id.get()
    entry_id.config(state='normal')
    if not id:
        messagebox.showwarning("Input Error", "Please enter Employee ID to search")
        return

    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM employee_db WHERE id = %s", (id,))
        row = cur.fetchone()
        conn.close()

        if row:
           
            entry_name.delete(0, tk.END)
            entry_name.insert(0, row[1])

            entry_age.delete(0, tk.END)
            entry_age.insert(0, row[2])

            gender_var.set(row[3])

            entry_dept.delete(0, tk.END)
            entry_dept.insert(0, row[4])

            entry_salary.delete(0, tk.END)
            entry_salary.insert(0, row[5])

            messagebox.showinfo("Record Found", "Employee details loaded for editing")
        else:
            messagebox.showwarning("Not Found", "No employee found with this ID")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))        
        
def clear_form():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set("Male")
    entry_dept.delete(0, tk.END)
    entry_salary.delete(0, tk.END)


root = tk.Tk()
root.title("Employee Details Form")
root.geometry("350x350")


tk.Label(root, text="Employee Details Form", font=("Georgia", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Employee ID:",state='disabled').grid(row=5, column=0, sticky="w", padx=5, pady=5)
entry_id = tk.Entry(frame, width=25)
entry_id.grid(row=5, column=1)

tk.Label(frame, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_name = tk.Entry(frame, width=25)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Age:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_age = tk.Entry(frame, width=25)
entry_age.grid(row=1, column=1)

tk.Label(frame, text="Gender:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female").grid(row=2, column=1, sticky="e")

tk.Label(frame, text="Department:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
entry_dept = tk.Entry(frame, width=25)
entry_dept.grid(row=3, column=1)

tk.Label(frame, text="Salary:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
entry_salary = tk.Entry(frame, width=25)
entry_salary.grid(row=4, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Submit", command=submit_details, width=10, bg="green", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_form, width=10, bg="red", fg="white").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Edit", command=search_employee, width=10, bg="light blue", fg="white").grid(row=0, column=2, padx=5)


create_table()
root.mainloop()    
