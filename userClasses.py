# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Todo: Fix error where variable names have pauses
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
    def __init__(self,userType,userName,password,warnings,suspended):
        self.userType = userType

        self.userName = userName
        self.password = password

        self.warnings = int(warnings)
        self.suspended = (suspended == 'True')

    # Logic when printing a class
    def __str__(self):
        return self.userType+" | "+self.userName+" | "+self.password+" | "+str(self.warnings)+" | "+str(self.suspended)

    def returnAllVariables(self):
        return list(vars(self).values())


class StoreClerk(RegisteredUser):
    userType = "Store Clerk"


class StoreManager(RegisteredUser):
    userType = "Store Manager"


class ComputerCompany(RegisteredUser):
    userType = "Computer Company"


class DeliveryCompany(RegisteredUser):
    userType = "Delivery Company"


def writeAccountsToFile(userList):
    file = open("userList.txt", "w")
    for user in userList:
        values = user.returnAllVariables()
        for item in values:
            file.write(str(item)+"|")
        file.write("\n")

    file.close()


def readAccounts():
    lst = []
    file = open("userList.txt", "r")

    for line in file:
        userVars = line.split("|")
        # Pops last value since it's the newline ("\n")
        userVars.pop()
        if userVars[0] == "Registered User":
            lst.append(RegisteredUser(*userVars))
        elif userVars[0] == "Store Clerk":
            lst.append(StoreClerk(*userVars))
        elif userVars[0] == "Store Manager":
            lst.append(StoreManager(*userVars))
        elif userVars[0] == "Computer Company":
            lst.append(ComputerCompany(*userVars))
        elif userVars[0] == "Delivery Company":
            lst.append(DeliveryCompany(*userVars))

    file.close()
    return lst


# Only runs code if running straight from script and not from an import
if __name__ == '__main__':
    registeredUserList = readAccounts()

    for userAccount in registeredUserList:
        print(userAccount)
