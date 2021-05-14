import computerPartsClasses as comParts
import GUI as gui

registeredUserList = []
mainItemList = []

if __name__ == '__main__':
    # Function that starts gui
    gui.startGUI()

    # Passes this list to the gui
    gui.mainItemList = comParts.readAccounts()

    gui.root.mainloop()
