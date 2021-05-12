import random
import decimal

import userClasses as userClass
import computerPartsClasses as comParts
import GUI as gUI

registeredUserList = []
mainItemList = []

if __name__ == '__main__':
    # Retrieves user list from text file
    registeredUserList = userClass.readAccounts()

    # Tests that users were successfully collected by printing them
    for userAccount in registeredUserList:
        print(userAccount)

    # Function that starts gui
    gUI.startGUI()

    # region Insert random items into list
    for i in range(20):
        mainItemList.append(
            comParts.CpuItem("CpuItem" + str(i), comParts.returnRandomCompany(),
                             decimal.Decimal(random.randrange(100, 200000)) / 100,
                             "2.5"))

    for i in range(20):
        mainItemList.append(
            comParts.RamItem("RamItem" + str(i), comParts.returnRandomCompany(),
                             decimal.Decimal(random.randrange(100, 200000)) / 100,
                             "4 Gb", "DDR3"))

    for i in range(20):
        mainItemList.append(
            comParts.GraphicsCardItem("GpuItem" + str(i), comParts.returnRandomCompany(),
                                      decimal.Decimal(random.randrange(100, 200000)) / 100, "RTX 2070"))

    # endregion

    # Passes this list to the gui
    gUI.mainItemList = mainItemList

    gUI.root.mainloop()
