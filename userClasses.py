# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class User:
    # User type used to indicate what privileges a user has or doesn't
    userType = "Visitor"

    # Placeholder function to debug and test that children classes have appropriate user type
    @classmethod
    def test_func(cls):
        print("I am a,", cls.userType, "!")


class RegisteredUser(User):
    userType = "Registered User"
    userName = ""
    password = ""

    # Warning and suspension system
    warnings = 0
    suspended = False

    # Initialization of class
    def __init__(self,userName,password):
        self.userName = userName
        self.password = password

    # Logic when printing a class
    def __str__(self):
        return self.userType+" | "+self.userName+" | "+self.password+" | "+str(self.warnings)+" | "+str(self.suspended)


class StoreClerk(RegisteredUser):
    userType = "Store Clerk"


class StoreManager(RegisteredUser):
    userType = "Store Manager"


class ComputerCompany(RegisteredUser):
    userType = "Computer Company"


class DeliveryCompany(RegisteredUser):
    userType = "Delivery Company"


# Only runs code if running straight from script and not from an import
if __name__ == '__main__':

    # Code to test list full of different users
    registeredUserList = []
    for i in range(20):
        registeredUserList.append(RegisteredUser("Tom"+str(i),"password"))
    for user in registeredUserList:
        print(user)