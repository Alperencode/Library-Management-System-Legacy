import sys
import re
import customtkinter as ctk
sys.path.append('../Library-Book-Matching-System')
# from database.SQLiteDB import SQLiteDataBase

FONT_FAM = "Comfortaa"


def ValidateEmail(email):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+[a-z]{1,3}$"
    print(type(email))
    print("email:", email)

    if re.match(pat, email):
        return True

    warning = ctk.CTkToplevel()
    warning.title("Warning")
    ctk.CTkLabel(
        warning,
        text="Please enter a valid e-mail\n\nExample: email@example.com",
        font=(FONT_FAM, 20, "bold")).pack(pady=20, padx=20)

    return False


class SignUpUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Initial
        self.title("Sign-Up")
        self.geometry("350x500")
        self.resizable(False, False)

        self.__email = None
        self.__password = None

        self.CreateUI()

    def CreateUI(self):
        # Title
        ctk.CTkLabel(
            self, text="Sign-Up to Library System",
            font=(FONT_FAM, 25, "bold"), pady=25).pack()

        # User entry
        ctk.CTkLabel(self, text="E-mail:", font=(FONT_FAM, 15)).pack(pady=20)
        self.email_entry = ctk.CTkEntry(
            self, placeholder_text="email@example.com")

        self.email_entry.pack()

        ctk.CTkLabel(self, text="Password:", font=(FONT_FAM, 15)).pack(pady=20)
        self.password_entry = ctk.CTkEntry(
            self, placeholder_text="*****", show='*')

        self.password_entry.pack()

        # Submit button
        ctk.CTkButton(
            self, text="Sign-Up",
            command=lambda: (self.SignUp())
            ).pack(pady=50)

    def SignUp(self):
        self.__email = self.email_entry.get()
        self.__password = self.password_entry.get()

        if ValidateEmail(self.__email):
            pass


class LoginUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")

        # Initial
        self.title("Log-in")
        self.geometry("600x500")
        self.resizable(False, False)

        self.__email = None
        self.__password = None

        self.CreateUI()

    def CreateUI(self):
        # Title
        ctk.CTkLabel(
            self, text="Library Book Matching System\nLogin Page",
            font=(FONT_FAM, 25, "bold"), pady=25).pack()

        # User entry
        ctk.CTkLabel(
            self, text="E-mail:", font=(FONT_FAM, 15)
        ).place(x=190, y=125)

        self.email_entry = ctk.CTkEntry(
            self, placeholder_text="email@example.com")
        self.email_entry.place(x=275, y=125)

        ctk.CTkLabel(
            self, text="Password:", font=(FONT_FAM, 15)
        ).place(x=180, y=175)

        self.password_entry = ctk.CTkEntry(
            self, placeholder_text="*****", show='*')
        self.password_entry.place(x=275, y=175)

        # Submit button
        ctk.CTkButton(
            self, text="Login", command=lambda: (self.Login())
        ).place(x=275, y=225)

        # Sign-up button
        ctk.CTkButton(
            self, text="Sign-Up", command=lambda: (self.InitSignUp())
            ).place(x=275, y=275)

    def InitSignUp(self):
        signUpApp = SignUpUI()
        signUpApp.mainloop()

    def Login(self):
        self.__email = self.email_entry.get()
        self.__password = self.password_entry.get()

        if ValidateEmail(self.__email):
            pass


if __name__ == "__main__":
    app = LoginUI()
    app.mainloop()
