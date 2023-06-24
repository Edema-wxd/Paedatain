from tkinter import *

# import openpyxl


# TODO: Save the new data to python list
# TODO: Open excel file and append and save the new data
# TODO: Validate closing and saving of data to excel sheet


# UI SETUP

window = Tk()
window.title("Paelon data entry")
window.config(padx=50, pady=50, bg="white")

# LABELS
name_label = Label(text="Patient Name:", bg="white")
name_label.grid(column=0, row=0)

temp_label = Label(text="Temperature:", bg="white")
temp_label.grid(column=0, row=1)

# BLANK SPACE
blank_label = Label(text="", bg="white")
blank_label.grid(column=0, row=2)

# DATA ENTRY

patient_name = Entry(width=27)
patient_name.grid(column=1, row=0, columnspan=2)
patient_name.focus()

temp = Entry(width=27)
temp.grid(column=1, row=1, columnspan=2)

# BUTTONS

next_data = Button(text="Next data", width=40)
next_data.grid(column=1, row=3, columnspan=2)

save_data = Button(text="End", width=15)
save_data.grid(column=0, row=3)

window.mainloop()
