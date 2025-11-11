import tkinter as tk
from tkinter import messagebox
import sqlite3

# ================== Login Function ==================
def login_user():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Input Error", "Please enter both username and password!")
        return

    try:
        conn = sqlite3.connect("meditrack.db")
        cur = conn.cursor()
        cur.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
        user = cur.fetchone()
        conn.close()

        if user:
            role = user[0]
            messagebox.showinfo("Login Success", f"Welcome {username}! (Role: {role})")
            open_dashboard(role)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ================== Dashboard Window ==================
def open_dashboard(role):
    dash = tk.Toplevel(root)
    dash.title("MediTrack Dashboard")
    dash.geometry("400x300")

    tk.Label(dash, text=f"Logged in as: {role}", font=("Verdana", 12, "bold")).pack(pady=10)

    if role == "Admin":
        tk.Label(dash, text="Admin Controls: Manage Users & View Reports").pack(pady=10)
    elif role == "Receptionist":
        tk.Label(dash, text="Reception Controls: Add Patients, Appointments").pack(pady=10)
    elif role == "Doctor":
        tk.Label(dash, text="Doctor Panel: View Appointments & Add Notes").pack(pady=10)
    else:
        tk.Label(dash, text="Unknown Role").pack(pady=10)

    tk.Button(dash, text="Logout", command=dash.destroy).pack(pady=20)
    tk.Button(dash, text="Patient Management", bg="#3498db", fg="white", command=open_patient_management).pack(pady=10)
    tk.Button(dash, text="Appointment Management", bg="#8e44ad", fg="white", command=open_appointment_management).pack(pady=10)




# ================== Main Login GUI ==================
root = tk.Tk()
root.title("MediTrack Login")
root.geometry("400x250")
root.config(bg="#dff9fb")

tk.Label(root, text="MediTrack Login", font=("Verdana", 16, "bold"), bg="#dff9fb").pack(pady=15)

tk.Label(root, text="Username:", bg="#dff9fb").pack()
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

tk.Label(root, text="Password:", bg="#dff9fb").pack()
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", width=15, bg="#22a6b3", fg="white", command=login_user).pack(pady=20)

#=========================patient management================================
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# ========== Function to Open Patient Management ==========
def open_patient_management():
    win = tk.Toplevel(root)
    win.title("Patient Management - MediTrack")
    win.geometry("600x400")
    win.config(bg="#ecf0f1")

    # ---------- Add Patient ----------
    tk.Label(win, text="Add New Patient", font=("Verdana", 14, "bold"), bg="#ecf0f1").pack(pady=10)

    frame = tk.Frame(win, bg="#ecf0f1")
    frame.pack(pady=5)

    tk.Label(frame, text="Name:", bg="#ecf0f1").grid(row=0, column=0, sticky='e', padx=5, pady=5)
    tk.Label(frame, text="DOB:", bg="#ecf0f1").grid(row=1, column=0, sticky='e', padx=5, pady=5)
    tk.Label(frame, text="Contact:", bg="#ecf0f1").grid(row=2, column=0, sticky='e', padx=5, pady=5)
    tk.Label(frame, text="Address:", bg="#ecf0f1").grid(row=3, column=0, sticky='e', padx=5, pady=5)
    tk.Label(frame, text="History:", bg="#ecf0f1").grid(row=4, column=0, sticky='e', padx=5, pady=5)

    name_entry = tk.Entry(frame, width=30)
    dob_entry = tk.Entry(frame, width=30)
    contact_entry = tk.Entry(frame, width=30)
    address_entry = tk.Entry(frame, width=30)
    history_entry = tk.Entry(frame, width=30)

    name_entry.grid(row=0, column=1, pady=5)
    dob_entry.grid(row=1, column=1, pady=5)
    contact_entry.grid(row=2, column=1, pady=5)
    address_entry.grid(row=3, column=1, pady=5)
    history_entry.grid(row=4, column=1, pady=5)

    # ---------- Add Patient Function ----------
    def add_patient():
        name = name_entry.get()
        dob = dob_entry.get()
        contact = contact_entry.get()
        address = address_entry.get()
        history = history_entry.get()

        if name == "" or contact == "":
            messagebox.showwarning("Input Error", "Name and Contact are required!")
            return

        try:
            conn = sqlite3.connect("meditrack.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO patients (name, dob, contact, address, history) VALUES (?, ?, ?, ?, ?)",
                        (name, dob, contact, address, history))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Patient added successfully!")
            show_patients()
            name_entry.delete(0, 'end')
            dob_entry.delete(0, 'end')
            contact_entry.delete(0, 'end')
            address_entry.delete(0, 'end')
            history_entry.delete(0, 'end')
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    tk.Button(win, text="Add Patient", bg="#27ae60", fg="white", command=add_patient).pack(pady=10)

    # ---------- View Patients ----------
    tk.Label(win, text="Patient List", font=("Verdana", 12, "bold"), bg="#ecf0f1").pack(pady=5)
    tree = ttk.Treeview(win, columns=("ID", "Name", "Contact", "History"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Contact", text="Contact")
    tree.heading("History", text="History")
    tree.pack(fill="both", expand=True, pady=5)

    def show_patients():
        for i in tree.get_children():
            tree.delete(i)

        conn = sqlite3.connect("meditrack.db")
        cur = conn.cursor()
        cur.execute("SELECT p_id, name, contact, history FROM patients")
        rows = cur.fetchall()
        conn.close()

        for row in rows:
            tree.insert("", "end", values=row)

    show_patients()

#===============================appoinmnets & dr assignment=====================
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime

# ========== Appointment Management ==========
def open_appointment_management():
    win = tk.Toplevel(root)
    win.title("Appointment Management - MediTrack")
    win.geometry("700x450")
    win.config(bg="#f1f2f6")

    tk.Label(win, text="Book Appointment", font=("Verdana", 14, "bold"), bg="#f1f2f6").pack(pady=10)

    frame = tk.Frame(win, bg="#f1f2f6")
    frame.pack(pady=5)

    tk.Label(frame, text="Patient ID:", bg="#f1f2f6").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(frame, text="Doctor ID:", bg="#f1f2f6").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(frame, text="Date & Time:", bg="#f1f2f6").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(frame, text="Reason:", bg="#f1f2f6").grid(row=3, column=0, padx=5, pady=5)
    tk.Label(frame, text="Charges:", bg="#f1f2f6").grid(row=4, column=0, padx=5, pady=5)

    pid_entry = tk.Entry(frame, width=30)
    did_entry = tk.Entry(frame, width=30)
    datetime_entry = tk.Entry(frame, width=30)
    reason_entry = tk.Entry(frame, width=30)
    charges_entry = tk.Entry(frame, width=30)

    pid_entry.grid(row=0, column=1, pady=5)
    did_entry.grid(row=1, column=1, pady=5)
    datetime_entry.grid(row=2, column=1, pady=5)
    reason_entry.grid(row=3, column=1, pady=5)
    charges_entry.grid(row=4, column=1, pady=5)

    # ========== Add Appointment ==========
    def add_appointment():
        pid = pid_entry.get()
        did = did_entry.get()
        dt = datetime_entry.get()
        reason = reason_entry.get()
        charges = charges_entry.get()

        if pid == "" or did == "" or reason == "":
            messagebox.showwarning("Missing Data", "Please fill all required fields!")
            return

        if dt == "":
            dt = datetime.now().strftime("%Y-%m-%d %H:%M")

        try:
            charges = float(charges) if charges else 0.0
        except:
            messagebox.showerror("Error", "Invalid charge amount!")
            return

        try:
            conn = sqlite3.connect("meditrack.db")
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO appointments (patient_id, doctor_id, datetime, reason, status, charges)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (pid, did, dt, reason, "Scheduled", charges))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Appointment booked successfully!")
            show_appointments()

            pid_entry.delete(0, 'end')
            did_entry.delete(0, 'end')
            datetime_entry.delete(0, 'end')
            reason_entry.delete(0, 'end')
            charges_entry.delete(0, 'end')

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    tk.Button(win, text="Book Appointment", bg="#2ecc71", fg="white", command=add_appointment).pack(pady=10)

    # ========== Appointment Table ==========
    tk.Label(win, text="Appointments List", font=("Verdana", 12, "bold"), bg="#f1f2f6").pack(pady=5)
    tree = ttk.Treeview(win, columns=("ID", "Patient", "Doctor", "DateTime", "Reason", "Status", "Charges"), show="headings")
    for col in ("ID", "Patient", "Doctor", "DateTime", "Reason", "Status", "Charges"):
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True, pady=5)

    def show_appointments():
        for i in tree.get_children():
            tree.delete(i)

        conn = sqlite3.connect("meditrack.db")
        cur = conn.cursor()
        cur.execute("SELECT a_id, patient_id, doctor_id, datetime, reason, status, charges FROM appointments")
        rows = cur.fetchall()
        conn.close()

        for row in rows:
            tree.insert("", "end", values=row)

    show_appointments()


root.mainloop()
