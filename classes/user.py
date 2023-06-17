class User:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def GetEmail(self):
        return self.__email

    def GetPassword(self):
        return self.__password

    def HashPassword(self):
        # Can use md5 here
        pass

    def GetUserInfo(self):
        return {
            "email": self.GetEmail(),
            "password": self.GetPassword()
        }

    def GetUserInfoAsTuple(self):
        return (
            self.GetEmail(),
            self.GetPassword()
        )
