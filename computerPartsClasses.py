import random
import decimal
import time

# region Class Definitions


class StoreItem:
    # Attributes to represent all computer parts
    itemType = ""
    name = ""
    company = ""
    price = 0.0
    priceDisplay = ""
    amountSold = 0

    def __init__(self,itemType,name,company,price,amountSold):
        self.itemType = itemType
        self.name = name
        self.company = company
        self.price = price
        self.priceDisplay = format(self.price, '.2f')
        self.amountSold = amountSold

    def __str__(self):
        return self.itemType + " | " + self.name + " | " + self.company + " | " + str(self.price) + " | "


class CpuItem(StoreItem):
    itemType = "CPU"
    GHz = ""

    def __init__(self,itemType,name,company,price,amountSold,GHz):
        super(CpuItem, self).__init__(itemType,name, company, price,amountSold)
        self.GHz = GHz


class RamItem(StoreItem):
    itemType = "Ram"
    capacity = ""
    speed = ""

    def __init__(self,itemType,name,company,price,amountSold,capacity,speed):
        super(RamItem, self).__init__(itemType,name,company,price,amountSold)
        self.capacity = capacity
        self.speed = speed


class GraphicsCardItem(StoreItem):
    itemType = "GPU"
    graphicsLine = ""

    def __init__(self,itemType,name,company,price,amountSold,graphicsLine):
        super(GraphicsCardItem, self).__init__(itemType,name,company,price,amountSold)
        self.graphicsLine = graphicsLine


class CaseItem(StoreItem):
    itemType = "Case"

    def __init__(self,itemType,name,company,price,amountSold):
        super(GraphicsCardItem, self).__init__(itemType,name,company,price,amountSold)


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


if __name__ == '__main__':
    print("Placeholder")