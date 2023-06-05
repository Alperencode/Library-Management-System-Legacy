from tkinter import *
import customtkinter as ctk
FONT_FAM = "Comfortaa"

ctk.set_appearance_mode("dark")

# Initial
app = ctk.CTk()
app.title("Basic GUI")
app.geometry("600x500")
app.resizable(False, False)

# Login function
def Login(username, password):
    pass

# Title
title = ctk.CTkLabel(app, text="Library Book Matching System\nLogin Page", font=(FONT_FAM, 25, "bold"), pady=25).pack()

# User entry
username = StringVar()
username_label = ctk.CTkLabel(app, text="Username:", font=(FONT_FAM, 15)).place(x=180, y=125)
username_entry = ctk.CTkEntry(app, textvariable=username).place(x=275, y=125)

password = StringVar()
password_label = ctk.CTkLabel(app, text="Password:", font=(FONT_FAM, 15)).place(x=180, y=175)
password_entry = ctk.CTkEntry(app, textvariable=password, show='*').place(x=275, y=175)

# Submit button
submit_button = ctk.CTkButton(app, text="Login", command=lambda:(Login(username, password))).place(x=275, y=225)

app.mainloop()