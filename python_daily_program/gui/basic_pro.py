from tkinter import *

# Create main window
root = Tk()
root.title("My First Window")   # window title
root.geometry("300x200")        # window size (width x height)

# Create a Label widget
label = Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20) 

# Create a Button widget
button = Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack(pady=10)

# Run the window
root.mainloop()
