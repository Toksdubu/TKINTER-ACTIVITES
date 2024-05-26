import tkinter as tk
from tkinter import messagebox, filedialog

app = tk.Tk()
app.title("Text Editor")
app.geometry('400x300')
current_file = None
unsaved_changes = False

text = tk.Text(app)
text.pack(fill=tk.BOTH, expand=True)

def open_file():
    global current_file, unsaved_changes

    # Check for unsaved changes
    if unsaved_changes:
        response = messagebox.askquestion("Unsaved Changes", "You have unsaved changes. Do you want to continue?")
        if response == "no":
            return

    # Open file dialog to choose a file
    filename = filedialog.askopenfilename()

    if filename:
        try:
            # Open the file
            with open(filename, "r") as file:
                content = file.read()
                text.delete("1.0", tk.END)
                text.insert(tk.END, content)

            # Update current file and unsaved changes status
            current_file = filename
            unsaved_changes = False
        except Exception as e:
            messagebox.showerror("Error", str(e))

def save_file():
    global current_file, unsaved_changes

    # Check if a file is open
    if not current_file:
        messagebox.showerror("Error", "No file is open.")
        return

    try:
        # Save the file
        content = text.get("1.0", tk.END)
        with open(current_file, "w") as file:
            file.write(content)

        # Update unsaved changes status
        unsaved_changes = False
        messagebox.showinfo("Information", "File saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def quit():
    global unsaved_changes

    # Check for unsaved changes
    if unsaved_changes:
        response = messagebox.askquestion("Unsaved Changes", "You have unsaved changes. Do you want to quit without saving?")
        if response == "no":
            return

    app.destroy()

def convert_to_uppercase():
    global unsaved_changes

    # Check if a file is open
    if not current_file:
        messagebox.showerror("Error", "No file is open.")
        return

    try:
        # Convert file contents to uppercase
        content = text.get("1.0", tk.END)
        content = content.upper()
        text.delete("1.0", tk.END)
        text.insert(tk.END, content)

        # Update unsaved changes status
        unsaved_changes = True
        messagebox.showinfo("Information", "File converted to uppercase.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_about():
    messagebox.showinfo("About", "This is a simple text editor application.")
menu_bar = tk.Menu(app)
def show_help():
    messagebox.showinfo("Help", 'For more details please contact the developers\nGmail:z.charlesnudalo6@gmail.com')
menu_bar = tk.Menu(app)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit)
menu_bar.add_cascade(label="File", menu=file_menu)


edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Convert to Uppercase", command=convert_to_uppercase)
menu_bar.add_cascade(label="Edit", menu=edit_menu)


help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help", command=show_help)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="About", menu=help_menu)

app.config(menu=menu_bar)
app.mainloop()