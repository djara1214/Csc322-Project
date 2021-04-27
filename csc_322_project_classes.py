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


class Products:
    product_id = ""
    price = 0
    description = ""
    number_sold = 0
