import random
import decimal

import userClasses as userClass
import computerPartsClasses as comParts
import GUI as gui

registeredUserList = []
mainItemList = []

if __name__ == '__main__':
    # Retrieves user list from text file
    registeredUserList = userClass.readAccounts()

    # Tests that users were successfully collected by printing them
    for userAccount in registeredUserList:
        print(userAccount)

    # Function that starts gui
    gui.startGUI()

    # region Insert random items into list
    for i in range(200):
        mainItemList.append(
            comParts.CpuItem("CPU","CpuItem" + str(i), comParts.returnRandomCompany(),
                             decimal.Decimal(random.randrange(100, 200000)) / 100,0,
                             "2.5"))

    for i in range(200):
        mainItemList.append(
            comParts.RamItem("RAM","RamItem" + str(i), comParts.returnRandomCompany(),
                             decimal.Decimal(random.randrange(100, 200000)) / 100,0,
                             "4 Gb", "DDR3"))

    for i in range(200):
        mainItemList.append(
            comParts.GraphicsCardItem("GPU","GpuItem" + str(i), comParts.returnRandomCompany(),
                                      decimal.Decimal(random.randrange(100, 200000)) / 100,0, "RTX 2070"))

    # endregion

    # Passes this list to the gui
    gui.mainItemList = mainItemList

    gui.root.mainloop()
