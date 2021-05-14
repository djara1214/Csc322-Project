import random

# region Class Definitions

# File where computer parts database is stored
computerPartsFile = "computerParts.txt"

# List holding all the cart items
userCart = []


class StoreItem:
    # Attributes to represent all computer parts
    itemType = ""
    name = ""
    company = ""
    price = 0.0
    priceDisplay = ""
    amountSold = 0

    def __init__(self,itemType,name,company,price,priceDisplay,amountSold):
        self.itemType = itemType
        self.name = name
        self.company = company
        self.price = float(price)
        self.priceDisplay = format(self.price, '.2f')
        self.amountSold = int(amountSold)

    def __str__(self):
        return self.itemType + " | " + self.name + " | " + self.company + " | " + str(self.price) + " | " + str(self.amountSold)

    def returnAllVariables(self):
        return list(vars(self).values())


class CpuItem(StoreItem):
    itemType = "CPU"
    GHz = ""

    def __init__(self,itemType,name,company,price,priceDisplay,amountSold,GHz):
        super(CpuItem, self).__init__(itemType,name, company, price,priceDisplay,amountSold)
        self.GHz = GHz


class RamItem(StoreItem):
    itemType = "Ram"
    capacity = ""
    speed = ""

    def __init__(self,itemType,name,company,price,priceDisplay,amountSold,capacity,speed):
        super(RamItem, self).__init__(itemType,name,company,price,priceDisplay,amountSold)
        self.capacity = capacity
        self.speed = speed


class GraphicsCardItem(StoreItem):
    itemType = "GPU"
    graphicsLine = ""

    def __init__(self,itemType,name,company,price,priceDisplay,amountSold,graphicsLine):
        super(GraphicsCardItem, self).__init__(itemType,name,company,price,priceDisplay,amountSold)
        self.graphicsLine = graphicsLine


class CaseItem(StoreItem):
    itemType = "Case"

    def __init__(self,itemType,name,company,price,priceDisplay,amountSold):
        super(CaseItem, self).__init__(itemType,name,company,price,priceDisplay,amountSold)

# endregion


# Placeholder function to return random company
def returnRandomCompany():
    randomValue = random.randint(0, 2)
    if randomValue == 0:
        return "Msi"
    elif randomValue == 1:
        return "Intel"
    else:
        return "AMD"


# List where items will be stored
listOfComputerParts = []


# RUNTIME: O(N*A) WHERE A IS THE AMOUNT OF ATTRIBUTES
def matchKeywordsFilter(itemList, attributes=None, keywords=None):
    if (attributes is None or keywords is None) or (len(attributes) != len(keywords)):
        return []

    filteredList = []
    for item in itemList:
        for attribute in range(len(attributes)):
            attributeReturn = getattr(item, attributes[attribute])
            if attributeReturn == keywords[attribute]:
                filteredList.append(item)

    return filteredList


# RUNTIME: O(N)
def rangeFilter(itemList, attribute,lowerBound, upperBound):
    filteredList = []
    for item in itemList:
        attributeReturn = getattr(item, attribute)
        if lowerBound <= attributeReturn <= upperBound:
            filteredList.append(item)

    return filteredList


# Filter than can accept multiple filter parameters
def generalFilter(itemList, filterList):  # Example: itemList, [ ["match",["company"],["AMD"]], ["range", "price", 100, 800] ]
    filteredList = []
    if len(filterList) == 0:
        return itemList
    elif filterList[0][0] == "match":
        attributes = filterList[0][1]
        keywords = filterList[0][2]
        filteredList = matchKeywordsFilter(itemList,attributes,keywords)
        filterList.pop(0)
        return generalFilter(filteredList, filterList)
    elif filterList[0][0] == "range":
        attribute = filterList[0][1]
        lowerBound = filterList[0][2]
        upperBound = filterList[0][3]
        filteredList = rangeFilter(itemList,attribute,lowerBound,upperBound)
        filterList.pop(0)
        return generalFilter(filteredList,filterList)


def readAccounts():
    lst = []
    file = open(computerPartsFile, "r")

    for line in file:
        userVars = line.split("|")
        # Pops last value since it's the newline ("\n")
        userVars.pop()
        if userVars[0] == "CPU":
            lst.append(CpuItem(*userVars))
        elif userVars[0] == "RAM":
            lst.append(RamItem(*userVars))
        elif userVars[0] == "GPU":
            lst.append(GraphicsCardItem(*userVars))
        elif userVars[0] == "Case":
            lst.append(CaseItem(*userVars))

    file.close()
    return lst


# Overwrites all users in file and writes: O(n*k) Runtime (n is # of users and k is # of variables for each user)
def writePartsToFile(partsList):
    file = open(computerPartsFile, "w")
    for user in partsList:
        values = user.returnAllVariables()
        print(values)
        for item in values:
            file.write(str(item)+"|")
        file.write("\n")

    file.close()


def addToCart(itemObject):
    userCart.append(itemObject)


def returnAmountSold(classObject):
    return classObject.amountSold


def returnBestSellers():
    listToReturn = []
    temp = sortComputerList()
    for i in range(3):
        listToReturn.append(temp.pop())
    return listToReturn


def sortComputerList():
    computerParts = readAccounts()
    computerParts.sort(key=returnAmountSold)
    return computerParts


if __name__ == '__main__':

    bestSellers = returnBestSellers()

    for bestSeller in bestSellers:
        print(bestSeller)
