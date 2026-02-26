import tkinter as tk

def clear_entry_field(entry_widget):
    """Deletes all characters in the entry box."""
    entry_widget.delete(0, tk.END) # Deletes from index 0 to the end

# --- Example Implementation ---
root = tk.Tk()
root.title("Main Form")
root.geometry("500x300")

# 1. Create the Entry widget
lblFrPerson = tk.LabelFrame(root, text = "Personal Information")
lblFrPerson.pack(pady=10)

# 2. Add some default text for testing
brand_bg = "blue"
brand_fg = "white"

lblFirst = tk.Label(lblFrPerson, text = "*First Name:", bg = brand_bg, fg = brand_fg)
lblFirst.grid(column = 0, row = 0, padx = 5, pady = 5)

entFirst = tk.Entry(lblFrPerson)
entFirst.grid(column = 1, row = 0, padx = 5, pady = 5)


lblLast = tk.Label(lblFrPerson, text = "*Last Name:", bg = brand_bg, fg = brand_fg)
lblLast.grid(column = 0, row = 1, padx = 5, pady = 5)

entLast = tk.Entry(lblFrPerson)
entLast.grid(column = 1, row = 1, padx = 5, pady = 5)


lblEmail = tk.Label(lblFrPerson, text = "Email:")
lblEmail.grid(column = 0, row = 2, padx = 5, pady = 5)

entEmail = tk.Entry(lblFrPerson)
entEmail.grid(column = 1, row = 2, padx = 5, pady = 5)


lblPhone = tk.Label(lblFrPerson, text = "Phone:")
lblPhone.grid(column = 0, row = 3, padx = 5, pady = 5)

entPhone = tk.Entry(lblFrPerson)
entPhone.grid(column = 1, row = 3, padx = 5, pady=5)


# 3. Create a Button that calls the clear function
#    A lambda is used to pass the specific widget as an argument
def displayData():
    print("First Name:", entFirst.get())
    print("Last Name:", entLast.get())
    print("Email:", entEmail.get())
    print("Phone:", entPhone.get())

def Clear():
    clear_entry_field(entFirst)
    clear_entry_field(entLast)
    clear_entry_field(entEmail)
    clear_entry_field(entPhone)



fraButtons = tk.Frame(lblFrPerson)
fraButtons.grid(column = 0, row = 4, columnspan = 2, pady = 10)

btnS = tk.Button(fraButtons, text = "Submit", width = 5, command = displayData)
btnS.pack(side=tk.LEFT, padx = 5)

btnR = tk.Button(fraButtons, text = "Reset", width = 5, command = Clear)
btnR.pack(side=tk.LEFT, padx = 5)

btnQ = tk.Button(fraButtons, text = "Quit", width = 5, command = root.destroy)
btnQ.pack(side=tk.LEFT, padx = 5)


root.mainloop()
