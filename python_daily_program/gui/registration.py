import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")
root.config(bg="lightblue")

# Heading
tk.Label(root, text="Registration Form", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)

# Labels and Entry fields
tk.Label(root, text="Full Name:", bg="lightblue", font=("Arial", 12)).pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Email:", bg="lightblue", font=("Arial", 12)).pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack()

tk.Label(root, text="Phone Number:", bg="lightblue", font=("Arial", 12)).pack()
phone_entry = tk.Entry(root, width=30)
phone_entry.pack()

tk.Label(root, text="Password:", bg="lightblue", font=("Arial", 12)).pack()
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack()

tk.Label(root, text="Gender:", bg="lightblue", font=("Arial", 12)).pack()
gender_var = tk.StringVar(value="None")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", bg="lightblue").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", bg="lightblue").pack()

# Function to submit form
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    password = password_entry.get()
    gender = gender_var.get()

    if name == "" or email == "" or phone == "" or password == "" or gender == "None":
        messagebox.showwarning("Input Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Registration Successful!\nWelcome, {name}")
        # Clear fields
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        gender_var.set("None")

# Submit button
tk.Button(root, text="Register", command=submit_form, bg="green", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

# Run the GUI
root.mainloop()
