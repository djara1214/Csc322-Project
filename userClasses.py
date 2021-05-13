# File name and location of user list
userListFile = "userList.txt"


class User:
    # User type used to indicate what privileges a user has or doesn't
    userType = "Visitor"


class RegisteredUser(User):
    userType = "Registered User"
    email = ""
    userName = ""
    password = ""

    # Warning and suspension system
    warnings = 0
    suspended = False
    currentBalance = 0

    # Initialization of class
    def __init__(self,userType,email,userName,password,warnings,suspended,balance):
        self.userType = userType

        self.email = email
        self.userName = userName
        self.password = password

        self.warnings = int(warnings)
        self.suspended = (suspended == 'True')
        self.currentBalance = float(balance)

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


# Overwrites all users in file and writes: O(n*k) Runtime (n is # of users and k is # of variables for each user)
def writeAccountsToFile(userList):
    file = open(userListFile, "w")
    for user in userList:
        values = user.returnAllVariables()
        for item in values:
            file.write(str(item)+"|")
        file.write("\n")

    file.close()


# Add a single account to text file: O(1) Runtime
def appendAccountToFile(newUser):
    file = open(userListFile,"a+")
    values = newUser.returnAllVariables()
    for item in values:
        file.write(str(item) + "|")
    file.write("\n")
    file.close()


# Gets all users and converts them to class objects before putting them in a list: O(n) Runtime
def readAccounts():
    lst = []
    file = open(userListFile, "r")

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


# Returns bool based on if account exists: O(n) Runtime
def checkIfAccountExists(email):
    file = open(userListFile,"r")

    for line in file:
        userVars = line.split("|")
        if userVars[1] == email:
            file.close()
            return True

    file.close()
    return False


# Converts list with class variables to class object
def convertToClassObject(userVar):
    if userVar[0] == "Registered User":
        return RegisteredUser(*userVar)
    elif userVar[0] == "Store Clerk":
        return StoreClerk(*userVar)
    elif userVar[0] == "Store Manager":
        return StoreManager(*userVar)
    elif userVar[0] == "Computer Company":
        return ComputerCompany(*userVar)
    elif userVar[0] == "Delivery Company":
        return DeliveryCompany(*userVar)


# Looks for user and returns it
def getAccount(email,password):
    global userListFile

    file = open(userListFile,"r")

    for line in file:
        userVars = line.split("|")
        # Pops the "/n" that is at the end of every line
        userVars.pop()
        if userVars[1] == email and userVars[3] == password:
            file.close()
            return convertToClassObject(userVars)

    file.close()
    # If no account is found, 0 is returned to signal an error that the username or password was incorrect
    return 0


def getAccountWithEmail(email):
    file = open(userListFile,"r")

    for line in file:
        userVars = line.split("|")
        # Pops the "/n" that is at the end of every line
        userVars.pop()
        if userVars[1] == email:
            file.close()
            return convertToClassObject(userVars)

    file.close()
    # If no account is found, 0 is returned to signal an error that the username or password was incorrect
    return 0


def createAccount(email,username,password,balance):
    global currentAccount
    foundAccount = getAccountWithEmail(email)

    # After checking for account, if it is not 0 then it means an account was found
    if foundAccount != 0:
        currentAccount = 0
    else:
        currentAccount = RegisteredUser("Registered User",email,username,password,0,False,balance)
        appendAccountToFile(currentAccount)


def switchAccounts(classObject):
    global currentAccount

    currentAccount = classObject


# Where current account will be stored
currentAccount = 0


def overwriteUser(userInstance):
    file = open(userListFile, 'r')

    # read a list of lines into data
    data = file.readlines()

    file.close()
    for line in range(len(data)):
        values = data[line].split("|")
        if values[1] == userInstance.email:
            print("YES")
            data[line] = ""
            userInstanceVars = userInstance.returnAllVariables()
            for item in userInstanceVars:
                data[line] += (str(item) + "|")
            data[line] += "\n"

    file = open(userListFile, 'w')
    file.writelines(data)


# Only runs code if running straight from script and not from an import
if __name__ == '__main__':

    # Example code for overwriting account
    registeredUser = getAccountWithEmail("test@gmail.com")
    registeredUser.warnings = 0

    overwriteUser(registeredUser)


