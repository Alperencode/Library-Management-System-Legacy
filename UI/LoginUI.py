import sys
import re
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
sys.path.append('../Library-Book-Matching-System')
# from database.SQLiteDB import SQLiteDataBase

FONT_FAM = "Comfortaa"


def WarningMessage(text):
    CTkMessagebox(
        title="Warning",
        message=text,
        icon="warning", option_1="Retry"
        )


def ValidateEmail(email):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.match(pat, email):
        return True

    WarningMessage("Please enter a valid e-mail\n\nExample: email@example.com")

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

    def GetEmail(self):
        return self.__email

    def GetPassword(self):
        return self.__password

    def SetEmail(self, email):
        self.__email = email

    def SetPassword(self, passwd):
        self.__password = passwd

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
        self.SetEmail(self.email_entry.get())
        self.SetPassword(self.password_entry.get())

        if not (self.GetEmail() or self.GetPassword()):
            WarningMessage("Please enter email and password")
            return

        if ValidateEmail(self.GetEmail()):
            # Create user
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

    def GetEmail(self):
        return self.__email

    def GetPassword(self):
        return self.__password

    def SetEmail(self, email):
        self.__email = email

    def SetPassword(self, passwd):
        self.__password = passwd

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
        self.SetEmail(self.email_entry.get())
        self.SetPassword(self.password_entry.get())

        if not (self.GetEmail() or self.GetPassword()):
            WarningMessage("Please enter email and password")
            return

        if ValidateEmail(self.GetEmail()):
            # Login user
            pass


if __name__ == "__main__":
    app = LoginUI()
    app.mainloop()
