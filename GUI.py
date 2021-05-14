import tkinter as tk
from tkinter import messagebox

import userClasses as userClass
import computerPartsClasses as comParts
import forums as forum

# Todo: Create and Design Cart
# Todo: Create and Connect Forums Page

# Global Website Attributes
topMenuWebsiteColor = "#002733"
mainMenuWebsiteColor = "#002733"
topMenuSecondaryWebsiteColor = "#2c515c"

currentPageColor = "#00465c"

frameColor = "#002733"
buttonColor = "#00698a"

filterPageColor = "#00465c"

titleFontColor = 'white'
# Used To Obtain Current Page
currentPage = "homePage"

# Main Item List
mainItemList = []
filteredItemList = []

listPage = 0


class TopMenu:
    global topMenuWebsiteColor
    global topMenuSecondaryWebsiteColor
    global mainMenuWebsiteColor
    global titleFontColor

    mainFrame = 0

    mainMenuFrame = 0
    loginRegisterFrame = 0

    # Title Label
    titleLabel = 0
    # Label that displays name
    usernameWelcomeLabel = 0

    cartAmount = 0

    # Buttons for login, register, and cart
    loginButton = 0
    logoutButton = 0
    registerButton = 0
    cartButton = 0

    # Buttons for top menu
    homeButton = 0
    computerPartsButton = 0
    forumsButton = 0
    accountInformationButton = 0

    # Top Menu GUI Attributes
    mainMenuPadX = 80
    loginRegisterPadX = 10

    mainTitleFont = "Arial"
    mainTitleFontSize = 50

    subtitleFont = "Arial"
    subtitleFontSize = 25

    loginButtonFont = "Arial"
    loginButtonFontSize = 15

    def __init__(self, tkRoot):
        self.mainFrame = tk.Frame(tkRoot, bg=topMenuWebsiteColor)
        self.insertWebpageTitle()
        self.insertLoginRegisterButton()
        self.insertDropDownMenus()

    def insertMainFrame(self):
        self.mainFrame.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    def removeMainFrame(self):
        self.mainFrame.place_forget()

    def insertWebpageTitle(self):
        self.titleLabel = tk.Label(self.mainFrame,text="Cook n' Look",fg=titleFontColor,bg=topMenuWebsiteColor,font=(self.mainTitleFont,self.mainTitleFontSize))
        self.titleLabel.place(relx=0.25,rely=0.15)

        self.usernameWelcomeLabel = tk.Label(self.mainFrame,fg=titleFontColor,bg=topMenuWebsiteColor,font=(self.subtitleFont,self.subtitleFontSize))
        self.usernameWelcomeLabel.place(relx=0.5,rely=0.5)
        self.updateWelcomeLabel()

    def insertLoginRegisterButton(self):
        self.loginRegisterFrame = tk.Frame(self.mainFrame,bg=topMenuSecondaryWebsiteColor)
        self.loginRegisterFrame.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.2)
        self.loginButton = tk.Button(self.loginRegisterFrame, text="Sign in",command=lambda: switchPages(currentPage, "loginPage"),font=(self.loginButtonFont, self.loginButtonFontSize))
        self.logoutButton = tk.Button(self.loginRegisterFrame, text="Sign out",command=logUserOut,font=(self.loginButtonFont, self.loginButtonFontSize))
        self.registerButton = tk.Button(self.loginRegisterFrame, text="Register",command=lambda: switchPages(currentPage, "registerPage"),font=(self.loginButtonFont, self.loginButtonFontSize))
        self.cartButton = tk.Button(self.loginRegisterFrame,text="Cart", command=lambda: switchPages(currentPage,"cartPage"),font=(self.loginButtonFont,self.loginButtonFontSize))
        self.cartButton.grid(row=0,column=0,padx=self.loginRegisterPadX)

        self.insertLoginOrLogoutButton()

    def increaseCartQuantity(self):
        self.cartAmount += 1
        self.cartButton['text'] = "("+str(self.cartAmount)+")"+" Cart"

    # Enables and disables login and register button based on if an account is signed in
    def insertLoginOrLogoutButton(self):
        if userClass.currentAccount == 0:
            self.logoutButton.grid_forget()
            self.loginButton.grid(row=0, column=1,padx=self.loginRegisterPadX)
            self.registerButton.grid(row=0, column=2, padx=self.loginRegisterPadX)
        else:
            self.loginButton.grid_forget()
            self.registerButton.grid_forget()
            self.logoutButton.grid(row=0, column=1, padx=self.loginRegisterPadX)

    def insertDropDownMenus(self):
        self.mainMenuFrame = tk.Frame(self.mainFrame,bg=mainMenuWebsiteColor)
        self.mainMenuFrame.place(relx=0,rely=0.7,relwidth=1,relheight=0.3)

        self.homeButton = tk.Button(self.mainMenuFrame,text="Home",command=lambda: switchPages(currentPage, "homePage"),font=(self.subtitleFont,self.subtitleFontSize)).grid(row=0,column=0,padx=self.mainMenuPadX)
        self.computerPartsButton = tk.Button(self.mainMenuFrame,text="Computer Parts",command=lambda: switchPages(currentPage, "computerPartsPage"),font=(self.subtitleFont,self.subtitleFontSize)).grid(row=0,column=1,padx=self.mainMenuPadX)
        self.forumsButton = tk.Button(self.mainMenuFrame,text="Forums",command=lambda: switchPages(currentPage, "forumPage"),font=(self.subtitleFont,self.subtitleFontSize)).grid(row=0,column=2,padx=self.mainMenuPadX)
        self.accountInformationButton = tk.Button(self.mainMenuFrame,text="Account",command=lambda: switchPages(currentPage, "accountPage"),font=(self.subtitleFont,self.subtitleFontSize)).grid(row=0,column=3,padx=self.mainMenuPadX)

    def updateWelcomeLabel(self):
        if userClass.currentAccount == 0:
            self.usernameWelcomeLabel["text"] = "Welcome, Guest!"
        else:
            self.usernameWelcomeLabel["text"] = "Welcome, "+userClass.currentAccount.userName+"!"


class HomePage:
    global currentPageColor
    global frameColor
    mainFrame = 0

    scrollable_frame = 0
    scrollbar = 0

    # GUI Attributes
    titleFontSize = 30
    canvasSize = 300

    # Frame and canvas for bestseller items
    bestSellersFrame = 0
    bestSellersItem1 = 0
    bestSellersItem2 = 0
    bestSellersItem3 = 0

    # Frame and canvas for bestseller items
    recommendedFrame = 0
    recommendedItem1 = 0
    recommendedItem2 = 0
    recommendedItem3 = 0

    def __init__(self, tkRoot):
        self.mainFrame = tk.Frame(tkRoot, bg=currentPageColor)

        canvas = tk.Canvas(self.mainFrame, bg=currentPageColor)

        self.scrollbar = tk.Scrollbar(self.mainFrame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg=currentPageColor)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Section which adds all the features
        self.createMainPage()

    def insertMainFrame(self):
        relativeY = 0.2
        self.mainFrame.place(rely=relativeY,relwidth=1,relheight=1-relativeY)

    def removeMainFrame(self):
        self.mainFrame.place_forget()

    def createMainPage(self):
        bestSellersLabel = tk.Label(self.scrollable_frame,text='Best Sellers',font=("Arial",self.titleFontSize))
        bestSellersLabel.grid(row=0,column=0)

        self.bestSellersFrame = tk.Frame(self.scrollable_frame,bg=frameColor)
        self.bestSellersFrame.grid(row=1,column=0,pady=40)
        self.bestSellersItem1 = tk.Canvas(self.bestSellersFrame,width=self.canvasSize,height=self.canvasSize,bg='black').grid(row=0,column=0,padx=80)
        self.bestSellersItem2 = tk.Canvas(self.bestSellersFrame,width=self.canvasSize,height=self.canvasSize,bg='black').grid(row=0,column=1,padx=80)
        self.bestSellersItem3 = tk.Canvas(self.bestSellersFrame,width=self.canvasSize,height=self.canvasSize,bg='black').grid(row=0,column=3,padx=80)

        recommendedLabel = tk.Label(self.scrollable_frame, text='Recommended Computers', font=("Arial", self.titleFontSize))
        recommendedLabel.grid(row=2, column=0)

        self.recommendedFrame = tk.Frame(self.scrollable_frame, bg=frameColor)
        self.recommendedFrame.grid(row=3, column=0,pady=40)
        self.recommendedItem1 = tk.Canvas(self.recommendedFrame, width=self.canvasSize, height=self.canvasSize, bg='black').grid(row=0, column=0, padx=80)
        self.recommendedItem2 = tk.Canvas(self.recommendedFrame, width=self.canvasSize, height=self.canvasSize, bg='black').grid(row=0, column=1, padx=80)
        self.recommendedItem3 = tk.Canvas(self.recommendedFrame, width=self.canvasSize, height=self.canvasSize, bg='black').grid(row=0, column=3, padx=80)


class LoginPage:
    global currentPageColor

    mainFrame = 0

    usernameLabel = 0
    usernameEntry = 0
    passwordLabel = 0
    passwordEntry = 0
    loginButton = 0

    # Login Page Attributes
    titleFont = "Arial"
    titleFontSize = 60

    subTitleFont = "Arial"
    subTitleFontSize = 30

    def __init__(self, tkRoot):
        self.mainFrame = tk.Frame(tkRoot, bg=currentPageColor)
        self.createLoginPage()

    def insertMainFrame(self):
        relativeY = 0.2
        self.mainFrame.place(rely=relativeY,relwidth=1,relheight=1-relativeY)

    def removeMainFrame(self):
        self.mainFrame.place_forget()

    def createLoginPage(self):
        self.usernameLabel = tk.Label(self.mainFrame,text="Email Address",font=(self.subTitleFont,self.subTitleFontSize))
        self.usernameLabel.place(relx=0.25,rely=0.2)
        self.usernameEntry = tk.Entry(self.mainFrame,font=(self.subTitleFont,self.subTitleFontSize))
        self.usernameEntry.place(relx=0.45,rely=0.2,relwidth=0.25,relheight=0.1)

        self.passwordLabel = tk.Label(self.mainFrame, text="Password",font=(self.subTitleFont,self.subTitleFontSize))
        self.passwordLabel.place(relx=0.25,rely=0.6)
        self.passwordEntry = tk.Entry(self.mainFrame,font=(self.subTitleFont,self.subTitleFontSize))
        self.passwordEntry.place(relx=0.45,rely=0.6,relwidth=0.25,relheight=0.1)

        self.loginButton = tk.Button(self.mainFrame, text="Login",command=self.attemptLoginInformation,font=(self.subTitleFont,self.subTitleFontSize))
        self.loginButton.place(relx=0.4,rely=0.8)

    def attemptLoginInformation(self):
        global topMenu
        global loginPage
        global accountPage
        global homePage

        usernameEntryInput = self.usernameEntry.get()
        passwordEntryInput = self.passwordEntry.get()

        userObject = userClass.getAccount(usernameEntryInput,passwordEntryInput)
        if userObject == 0:
            tk.messagebox.showwarning(title="Uh-oh", message="Wrong Username Or Password")
        else:
            userClass.switchAccounts(userObject)
            topMenu.updateWelcomeLabel()
            accountPage.updateAccountInformation()
            topMenu.insertLoginOrLogoutButton()
            switchPages(currentPage,"homePage")


class RegisterPage:
    global currentPageColor

    mainFrame = 0

    emailAddressLabel = 0
    emailAddressEntry = 0
    usernameLabel = 0
    usernameEntry = 0
    passwordLabel = 0
    passwordEntry = 0
    retypeLabel = 0
    retypeEntry = 0
    balanceLabel = 0
    balanceEntry = 0
    createAccountButton = 0

    # Login Page Attributes
    titleFont = "Arial"
    titleFontSize = 60

    subTitleFont = "Arial"
    subTitleFontSize = 30

    def __init__(self, tkRoot):
        self.mainFrame = tk.Frame(tkRoot, bg=currentPageColor)
        self.createRegisterPage()

    def insertMainFrame(self):
        relativeY = 0.2
        self.mainFrame.place(rely=relativeY,relwidth=1,relheight=1-relativeY)

    def removeMainFrame(self):
        self.mainFrame.place_forget()

    def createRegisterPage(self):
        self.emailAddressLabel = tk.Label(self.mainFrame,text="Email Address",font=(self.subTitleFont,self.subTitleFontSize))
        self.emailAddressLabel.place(relx=0.25,rely=0.05)
        self.emailAddressEntry = tk.Entry(self.mainFrame,font=(self.subTitleFont,self.subTitleFontSize))
        self.emailAddressEntry.place(relx=0.45,rely=0.05,relwidth=0.25,relheight=0.1)

        self.usernameLabel = tk.Label(self.mainFrame,text="Name",font=(self.subTitleFont,self.subTitleFontSize))
        self.usernameLabel.place(relx=0.25,rely=0.2)
        self.usernameEntry = tk.Entry(self.mainFrame,font=(self.subTitleFont,self.subTitleFontSize))
        self.usernameEntry.place(relx=0.45,rely=0.2,relwidth=0.25,relheight=0.1)

        self.passwordLabel = tk.Label(self.mainFrame, text="Password",font=(self.subTitleFont,self.subTitleFontSize))
        self.passwordLabel.place(relx=0.25,rely=0.35)
        self.passwordEntry = tk.Entry(self.mainFrame,font=(self.subTitleFont,self.subTitleFontSize))
        self.passwordEntry.place(relx=0.45,rely=0.35,relwidth=0.25,relheight=0.1)

        self.retypeLabel = tk.Label(self.mainFrame, text="Retype Password",font=(self.subTitleFont,self.subTitleFontSize))
        self.retypeLabel.place(relx=0.25,rely=0.5)
        self.retypeEntry = tk.Entry(self.mainFrame,font=(self.subTitleFont,self.subTitleFontSize))
        self.retypeEntry.place(relx=0.45,rely=0.5,relwidth=0.25,relheight=0.1)

        self.balanceLabel = tk.Label(self.mainFrame, text="Enter a Starting Balance",font=(self.subTitleFont,self.subTitleFontSize))
        self.balanceLabel.place(relx=0.20,rely=0.65)
        self.balanceEntry = tk.Entry(self.mainFrame,font=(self.subTitleFont,self.subTitleFontSize))
        self.balanceEntry.place(relx=0.45,rely=0.65,relwidth=0.25,relheight=0.1)

        self.createAccountButton = tk.Button(self.mainFrame, text="Create Account",command=self.attemptRegisterInformation,font=(self.subTitleFont,self.subTitleFontSize)).place(relx=0.4,rely=0.8)

    def attemptRegisterInformation(self):
        global topMenu
        global registerPage
        global homePage

        emailEntryInput = self.emailAddressEntry.get()
        usernameEntryInput = self.usernameEntry.get()
        passwordEntryInput = self.passwordEntry.get()
        retypeEntryInput = self.retypeEntry.get()
        balanceEntryInput = self.balanceEntry.get()

        # Bool that switches to true once all the inputs are checked
        passesPasswordCheck = False
        passesBalanceCheck = False
        passesEmptyEntryCheck = False

        if passwordEntryInput == retypeEntryInput:
            passesPasswordCheck = True
        if int(balanceEntryInput) > 0:
            passesBalanceCheck = True
        if len(emailEntryInput) > 0 and len(usernameEntryInput) > 0 and len(passwordEntryInput) > 0 and len(retypeEntryInput) > 0 and len(balanceEntryInput) > 0:
            passesEmptyEntryCheck = True

        if passesPasswordCheck and passesBalanceCheck and passesEmptyEntryCheck:
            userClass.createAccount(emailEntryInput, usernameEntryInput, passwordEntryInput, balanceEntryInput)

            if userClass.currentAccount == 0:
                tk.messagebox.showwarning(title="Uh-oh", message="Looks like this email is already taken.")
            else:
                topMenu.updateWelcomeLabel()
                topMenu.insertLoginOrLogoutButton()
                accountPage.updateAccountInformation()
                switchPages(currentPage, "homePage")
        elif not passesPasswordCheck:
            tk.messagebox.showwarning(title="Uh-oh", message="Your passwords do not match.")
        elif not passesBalanceCheck:
            tk.messagebox.showwarning(title="Uh-oh", message="Your balance is not a number above 0.")
        elif not passesEmptyEntryCheck:
            tk.messagebox.showwarning(title="Uh-oh", message="One or more of your fields are empty.")


# Helper class used by Computer Parts Page Class
class ComputerPartListing:
    global frameColor
    global computerPartsPage

    mainFrame = 0

    # Reference to listing number so code knows which item it needs to bring up
    listingNumber = 0

    # Listing Widgets
    photoCanvas = 0
    itemTitleLabel = 0
    itemCompanyLabel = 0
    itemTypeLabel = 0
    itemPriceLabel = 0
    addToCartButton = 0

    # Listing Attributes
    photoCanvasSize = 200

    listingSubtitleFont = "Arial"
    listingSubtitleFontSize = 20

    listingPriceFont = "Arial"
    listingPriceFontSize = 30

    addToCartButtonFont = "Arial"
    addToCartButtonFontSize = 20

    itemLabelPadXLeft = 10
    itemLabelPadXRight = 300

    def __init__(self, tkRoot):
        self.mainFrame = tk.Frame(tkRoot, bg=frameColor)
        self.createListing()

    def createListing(self):
        self.photoCanvas = tk.Canvas(self.mainFrame,width=self.photoCanvasSize,height=self.photoCanvasSize,bg='black')
        self.itemTitleLabel = tk.Label(self.mainFrame,text="Item Title",font=(self.listingSubtitleFont,self.listingSubtitleFontSize))
        self.itemCompanyLabel = tk.Label(self.mainFrame,text="Item Company",font=(self.listingSubtitleFont,self.listingSubtitleFontSize))
        self.itemTypeLabel = tk.Label(self.mainFrame,text="Item Type",font=(self.listingSubtitleFont,self.listingSubtitleFontSize))
        self.itemPriceLabel = tk.Label(self.mainFrame,text="$ 199.99",font=(self.listingPriceFont,self.listingPriceFontSize))
        self.addToCartButton = tk.Button(self.mainFrame,text="Add To Cart", command=lambda: returnListingNumber(self.listingNumber),font=(self.addToCartButtonFont,self.addToCartButtonFontSize))

        self.photoCanvas.grid(row=0,column=0,rowspan=3,padx=(20,0),pady=20)
        self.itemTitleLabel.grid(row=0,column=1,sticky='NW',padx=(self.itemLabelPadXLeft,self.itemLabelPadXRight),pady=(20,5))
        self.itemCompanyLabel.grid(row=1,column=1,sticky='NW',padx=(self.itemLabelPadXLeft,self.itemLabelPadXRight))
        self.itemTypeLabel.grid(row=2,column=1,sticky='NW',padx=(self.itemLabelPadXLeft,self.itemLabelPadXRight))
        self.itemPriceLabel.grid(row=0,column=2,padx=10)
        self.addToCartButton.grid(row=2,column=2,padx=10)

    def updateListing(self,itemTitle,itemCompany,itemType,itemPrice):
        self.itemTitleLabel['text'] = itemTitle
        self.itemCompanyLabel['text'] = itemCompany
        self.itemTypeLabel['text'] = itemType
        self.itemPriceLabel['text'] = itemPrice


def returnListingNumber(i):
    global computerPartsPage
    global topMenu

    if computerPartsPage != 0:
        comParts.addToCart(computerPartsPage.listToDisplay[(computerPartsPage.listPage * 50) + i])

    topMenu.increaseCartQuantity()


class ComputerPartsPage:
    global mainItemList
    global filteredItemList

    global currentPageColor
    global filterPageColor

    mainFrame = 0
    mainCanvas = 0

    scrollable_frame = 0
    scrollbar = 0

    filterFrame = 0

    # GUI Attributes
    titleFont = "Arial"
    titleFontSize = 30
    canvasSize = 300
    listingPadX = 175
    listingPadY = 20

    searchResultsPadX = 20
    searchResultsPadY = 20

    mainFrameRelativeX = 0.2
    mainFrameRelativeY = 0.2

    # Reference List
    listOfItemListings = []
    listToDisplay = []

    # This is used so that the next button would list the next 50 in the filtered item and the last 50

    canPressNext = True

    # Listing widgets
    listPage = 0
    previousButton = 0
    nextButton = 0

    # Filter Objects
    # Price Range
    minPriceEntry = 0
    maxPriceEntry = 0
    # Company Names

    # Check holds the checkbox widget, while checkbox holds the output value of the checkbox
    msiCheck = 0
    msiCheckbox = 0

    aMDCheck = 0
    aMDCheckbox = 0

    intelCheck = 0
    intelCheckbox = 0

    otherEntry = 0

    applyFilterButton = 0
    revertFilterButton = 0

    # Computer Parts
    cpuCheck = 0
    cpuCheckbox = 0

    ramCheck = 0
    ramCheckbox = 0

    gpuCheck = 0
    gpuCheckbox = 0

    casesCheck = 0
    casesCheckbox = 0

    # Filter Object Attributes
    filterPadXLeft = 20
    filterTitlePadY = 20
    filterSubtitlePadY = 10

    priceEntryWidth = 5
    otherEntryWidth = 8
    entryFont = "Arial"
    entryFontSize = 18

    filterTitleFont = "Arial"
    filterTitleFontSize = 30
    filterSubtitleFont = "Arial"
    filterSubtitleFontSize = 20

    def __init__(self, tkRoot):
        self.mainFrame = tk.Frame(tkRoot, bg=currentPageColor)
        self.filterFrame = tk.Frame(tkRoot, bg=filterPageColor)

        self.mainCanvas = tk.Canvas(self.mainFrame, bg=currentPageColor)

        self.scrollbar = tk.Scrollbar(self.mainFrame, orient="vertical", command=self.mainCanvas.yview)
        self.scrollable_frame = tk.Frame(self.mainCanvas, bg=currentPageColor)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.mainCanvas.configure(
                scrollregion=self.mainCanvas.bbox("all")
            )
        )

        self.mainCanvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.mainCanvas.configure(yscrollcommand=self.scrollbar.set)

        self.mainCanvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Initializing Checkbox Variables
        self.msiCheckbox = tk.IntVar()
        self.aMDCheckbox = tk.IntVar()
        self.intelCheckbox = tk.IntVar()

        self.cpuCheckbox = tk.IntVar()
        self.ramCheckbox = tk.IntVar()
        self.gpuCheckbox = tk.IntVar()
        self.casesCheckbox = tk.IntVar()

        # Section which adds all the features
        self.createMainPage()
        self.createFilterPage()

    def insertMainFrame(self):
        self.mainFrame.place(relx=self.mainFrameRelativeX,rely=self.mainFrameRelativeY,relwidth=1-self.mainFrameRelativeX,relheight=1-self.mainFrameRelativeY)
        self.filterFrame.place(relx=0, rely=self.mainFrameRelativeY, relwidth=self.mainFrameRelativeX, relheight=1 - self.mainFrameRelativeY)
        self.updateListings()

    def removeMainFrame(self):
        self.mainFrame.place_forget()
        self.filterFrame.place_forget()

    def createMainPage(self):
        searchResultsLabel = tk.Label(self.scrollable_frame,text='Search Results',font=(self.titleFont,self.titleFontSize))
        searchResultsLabel.grid(row=0,column=0,columnspan=3,sticky='W',padx=self.searchResultsPadX,pady=self.searchResultsPadY)

        # Initializes item listing outline
        for i in range(50):
            self.listOfItemListings.append(ComputerPartListing(self.scrollable_frame))
            self.listOfItemListings[i].listingNumber = i

        # Previous and next buttons
        self.previousButton = tk.Button(self.scrollable_frame,text="Previous",command=self.decreaseListPage,font=(self.titleFont,self.titleFontSize))
        self.previousButton.grid(row=52,column=0,pady=50)
        self.nextButton = tk.Button(self.scrollable_frame,text="Next",command=self.increaseListPage,font=(self.titleFont,self.titleFontSize))
        self.nextButton.grid(row=52,column=1,columnspan=2,pady=50)

    def createFilterPage(self):
        # Initializing Widgets

        # Price Gui Section
        tk.Label(self.filterFrame,text="Price",font=(self.filterTitleFont,self.filterTitleFontSize)).grid(row=0,column=0,columnspan=4,pady=self.filterTitlePadY)
        self.minPriceEntry = tk.Entry(self.filterFrame,width=self.priceEntryWidth,font=(self.entryFont,self.entryFontSize))
        self.minPriceEntry.grid(row=1,column=0,padx=(self.filterPadXLeft,0),pady=self.filterSubtitlePadY)
        tk.Label(self.filterFrame,text="min.",font=(self.filterSubtitleFont,self.filterSubtitleFontSize)).grid(row=1,column=1)
        self.maxPriceEntry = tk.Entry(self.filterFrame,width=self.priceEntryWidth,font=(self.entryFont,self.entryFontSize))
        self.maxPriceEntry.grid(row=1,column=2,padx=(self.filterPadXLeft,0),pady=self.filterSubtitlePadY)
        tk.Label(self.filterFrame,text="max.",font=(self.filterSubtitleFont,self.filterSubtitleFontSize)).grid(row=1,column=3)
        # Company Names Gui Section
        tk.Label(self.filterFrame,text="Company",font=(self.filterTitleFont,self.filterTitleFontSize)).grid(row=2,column=0,columnspan=4,pady=self.filterTitlePadY)
        self.msiCheck = tk.Checkbutton(self.filterFrame,text="Msi",font=(self.filterSubtitleFont,self.filterSubtitleFontSize),variable=self.msiCheckbox).grid(row=3,column=0,padx=(self.filterPadXLeft,0),pady=self.filterSubtitlePadY)
        self.aMDCheck = tk.Checkbutton(self.filterFrame, text="AMD",font=(self.filterSubtitleFont,self.filterSubtitleFontSize),variable=self.aMDCheckbox).grid(row=3,column=2,padx=(self.filterPadXLeft,0),pady=self.filterSubtitlePadY)
        self.intelCheck = tk.Checkbutton(self.filterFrame, text="Intel",font=(self.filterSubtitleFont,self.filterSubtitleFontSize),variable=self.intelCheckbox).grid(row=4,column=0,padx=(self.filterPadXLeft,0))
        self.otherEntry = tk.Entry(self.filterFrame,width=self.otherEntryWidth,font=(self.entryFont,self.entryFontSize)).grid(row=4,column=2,padx=(self.filterPadXLeft,0))
        tk.Label(self.filterFrame,font=(self.filterSubtitleFont,self.filterSubtitleFontSize),text="Other").grid(row=4,column=3)
        # Computer Part Gui Section
        tk.Label(self.filterFrame,text="Computer Part",font=(self.filterTitleFont,self.filterTitleFontSize)).grid(row=5,column=0,columnspan=4,pady=self.filterTitlePadY)
        self.cpuCheck = tk.Checkbutton(self.filterFrame,text="CPU",font=(self.filterSubtitleFont,self.filterSubtitleFontSize),variable=self.cpuCheckbox).grid(row=6,column=0,padx=(self.filterPadXLeft,0),pady=self.filterSubtitlePadY)
        self.ramCheck = tk.Checkbutton(self.filterFrame, text="RAM",font=(self.filterSubtitleFont,self.filterSubtitleFontSize),variable=self.ramCheckbox).grid(row=6,column=2,padx=(self.filterPadXLeft,0),pady=self.filterSubtitlePadY)
        self.gpuCheck = tk.Checkbutton(self.filterFrame, text="GPU",font=(self.filterSubtitleFont,self.filterSubtitleFontSize),variable=self.gpuCheckbox).grid(row=7,column=0,padx=(self.filterPadXLeft,0))
        self.casesCheck = tk.Checkbutton(self.filterFrame, text="Cases",font=(self.filterSubtitleFont,self.filterSubtitleFontSize),variable=self.casesCheckbox).grid(row=7,column=2,padx=(self.filterPadXLeft,0))
        # Apply Filter Revert Buttons
        self.applyFilterButton = tk.Button(self.filterFrame,text="Apply",font=(self.titleFont,self.titleFontSize),command=self.applyFilters).grid(row=8,column=0,columnspan=2,padx=self.filterPadXLeft,pady=self.filterTitlePadY)
        self.revertFilterButton = tk.Button(self.filterFrame,text="Revert",font=(self.titleFont,self.titleFontSize),command=self.revertFilters).grid(row=8,column=2,columnspan=2,padx=self.filterPadXLeft,pady=self.filterTitlePadY)

    def updateListings(self):
        # Allows next button to be pressed unless
        self.canPressNext = True

        if len(filteredItemList) == 0:
            self.listToDisplay = mainItemList
        else:
            self.listToDisplay = filteredItemList

        for index in range(50):
            listingIndex = index + (50 * self.listPage)
            if index >= len(self.listToDisplay) - (50 * self.listPage):
                self.listOfItemListings[index].mainFrame.grid_forget()
                self.canPressNext = False
            else:
                self.listOfItemListings[index].updateListing(self.listToDisplay[listingIndex].name,"Company: "+self.listToDisplay[listingIndex].company,"Computer Part: "+self.listToDisplay[listingIndex].itemType,"$ "+self.listToDisplay[listingIndex].priceDisplay)
                self.listOfItemListings[index].mainFrame.grid(row=index + 1, column=0, columnspan=2, padx=self.listingPadX, pady=self.listingPadY)

    def increaseListPage(self):
        if self.canPressNext:
            self.listPage += 1
        self.updateListings()

        # Automatically scrolls to the top
        self.mainCanvas.yview_moveto(0)

    def decreaseListPage(self):
        if self.listPage > 0:
            self.listPage -= 1
        self.updateListings()

        # Automatically scrolls to the top
        self.mainCanvas.yview_moveto(0)

    def applyFilters(self):
        global filteredItemList

        # Returns the page number to 0
        self.listPage = 0

        # Matching section of filtering
        argumentToApply = [["match",[],[]]]
        if self.msiCheckbox.get() == 1:
            argumentToApply[0][1].append("company")
            argumentToApply[0][2].append("Msi")
        if self.intelCheckbox.get() == 1:
            argumentToApply[0][1].append("company")
            argumentToApply[0][2].append("Intel")
        if self.aMDCheckbox.get() == 1:
            argumentToApply[0][1].append("company")
            argumentToApply[0][2].append("AMD")

        # Pops initial "["match",[],[]]" empty argument if no arguments are given
        if argumentToApply[0][1] == []:
            argumentToApply.pop(0)

        # Range Section
        if len(self.minPriceEntry.get()) != 0 and len(self.maxPriceEntry.get()) != 0:
            argumentToApply.append(["range","price",int(self.minPriceEntry.get()),int(self.maxPriceEntry.get())])

        # Matching section for computer parts
        argumentToApply.append(["match", [], []])
        indexToInsert = len(argumentToApply)-1
        if self.cpuCheckbox.get() == 1:
            argumentToApply[indexToInsert][1].append("itemType")
            argumentToApply[indexToInsert][2].append("CPU")
        if self.ramCheckbox.get() == 1:
            argumentToApply[indexToInsert][1].append("itemType")
            argumentToApply[indexToInsert][2].append("RAM")
        if self.gpuCheckbox.get() == 1:
            argumentToApply[indexToInsert][1].append("itemType")
            argumentToApply[indexToInsert][2].append("GPU")
        if self.casesCheckbox.get() == 1:
            argumentToApply[indexToInsert][1].append("itemType")
            argumentToApply[indexToInsert][2].append("Case")

        # Pops initial "["match",[],[]]" empty argument if no arguments are given
        if argumentToApply[indexToInsert][1] == []:
            argumentToApply.pop(indexToInsert)

        filteredItemList = comParts.generalFilter(mainItemList,argumentToApply)
        self.updateListings()

        # Moves scrollbar back to top
        self.mainCanvas.yview_moveto(0)

    def revertFilters(self):
        global filteredItemList

        filteredItemList.clear()
        self.listPage = 0
        self.updateListings()

        # Moves scrollbar back to top
        self.mainCanvas.yview_moveto(0)


class AccountPage:
    global currentPageColor
    global frameColor
    mainFrame = 0

    scrollable_frame = 0
    scrollbar = 0

    # Page Variables
    emailLabel = 0
    userNameLabel = 0
    warningsLabel = 0
    currentBalanceLabel = 0
    # GUI Attributes
    titleFont = "Arial"
    titleFontSize = 30
    canvasSize = 300
    accountInfoPaddingY = 20

    def __init__(self, tkRoot):
        self.mainFrame = tk.Frame(tkRoot, bg=currentPageColor)

        canvas = tk.Canvas(self.mainFrame, bg=currentPageColor)

        self.scrollbar = tk.Scrollbar(self.mainFrame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg=currentPageColor)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Section which adds all the features
        self.createMainPage()

    def insertMainFrame(self):
        relativeY = 0.2
        self.mainFrame.place(rely=relativeY,relwidth=1,relheight=1-relativeY)

    def removeMainFrame(self):
        self.mainFrame.place_forget()

    def createMainPage(self):
        accountInfoLabel = tk.Label(self.scrollable_frame,text="Account Information",font=(self.titleFont,self.titleFontSize))
        accountInfoLabel.grid(row=0,column=0)

        tk.Label(self.scrollable_frame,text="Email: ",font=(self.titleFont,self.titleFontSize)).grid(row=1,column=1,pady=self.accountInfoPaddingY)
        self.emailLabel = tk.Label(self.scrollable_frame,text="",font=(self.titleFont,self.titleFontSize))
        self.emailLabel.grid(row=1,column=2,pady=self.accountInfoPaddingY)

        tk.Label(self.scrollable_frame, text="Name: ", font=(self.titleFont, self.titleFontSize)).grid(row=2,column=1,pady=self.accountInfoPaddingY)
        self.userNameLabel = tk.Label(self.scrollable_frame,text="",font=(self.titleFont,self.titleFontSize))
        self.userNameLabel.grid(row=2,column=2,pady=self.accountInfoPaddingY)

        tk.Label(self.scrollable_frame, text="Warnings: ", font=(self.titleFont, self.titleFontSize)).grid(row=3,column=1,pady=self.accountInfoPaddingY)
        self.warningsLabel = tk.Label(self.scrollable_frame,text="",font=(self.titleFont,self.titleFontSize))
        self.warningsLabel.grid(row=3,column=2,pady=self.accountInfoPaddingY)

        tk.Label(self.scrollable_frame, text="Current Balance: ", font=(self.titleFont, self.titleFontSize)).grid(row=4,column=1,pady=self.accountInfoPaddingY)
        self.currentBalanceLabel = tk.Label(self.scrollable_frame,text="",font=(self.titleFont,self.titleFontSize))
        self.currentBalanceLabel.grid(row=4,column=2,pady=self.accountInfoPaddingY)

    def updateAccountInformation(self):
        if userClass.currentAccount != 0:
            self.emailLabel['text'] = userClass.currentAccount.email
            self.userNameLabel['text'] = userClass.currentAccount.userName
            self.warningsLabel['text'] = str(userClass.currentAccount.warnings)
            self.currentBalanceLabel['text'] = "$ "+str(format(userClass.currentAccount.currentBalance, '.2f'))
        else:
            self.emailLabel['text'] = ""
            self.userNameLabel['text'] = ""
            self.warningsLabel['text'] = ""
            self.currentBalanceLabel['text'] = ""


class ForumPage:
    global currentPageColor
    global frameColor
    mainFrame = 0

    scrollable_frame = 0
    scrollbar = 0

    # Page Variables
    forumPage = 1
    forumComments = []
    listOfWidget = []

    row = 0
    previousButton = 0
    nextButton = 0

    # GUI Attributes
    titleFont = "Arial"
    titleFontSize = 30
    canvasSize = 300
    accountInfoPaddingY = 20

    def __init__(self, tkRoot):
        self.mainFrame = tk.Frame(tkRoot, bg=currentPageColor)

        canvas = tk.Canvas(self.mainFrame, bg=currentPageColor)

        self.scrollbar = tk.Scrollbar(self.mainFrame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg=currentPageColor)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=self.scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Section which adds all the features
        self.createMainPage()

    def insertMainFrame(self):
        relativeY = 0.2
        self.mainFrame.place(rely=relativeY,relwidth=1,relheight=1-relativeY)

    def removeMainFrame(self):
        self.mainFrame.place_forget()

    def createMainPage(self):
        self.showMessages()
        self.placeButtons()

    def showMessages(self):
        forum.AddComments(self.forumPage)
        self.row = 0
        for comment in forum.commentList:
            self.listOfWidget.append(tk.Label(self.scrollable_frame,text=comment.name,font=(self.titleFont,self.titleFontSize)))
            self.listOfWidget[len(self.listOfWidget)-1].grid(row=self.row,column=0)
            self.listOfWidget.append(tk.Label(self.scrollable_frame,text=comment.comment,font=(self.titleFont,self.titleFontSize)))
            self.listOfWidget[len(self.listOfWidget)-1].grid(row=self.row,column=1)

            self.row += 1

    def placeButtons(self):
        self.previousButton = tk.Button(self.scrollable_frame,text="Previous Chat",command=self.decrementChat,font=(self.titleFont,self.titleFontSize))
        self.previousButton.grid(row=self.row,column=0)
        self.nextButton = tk.Button(self.scrollable_frame,text="Next Chat",command=self.incrementChat,font=(self.titleFont,self.titleFontSize))
        self.nextButton.grid(row=self.row,column=1)

        self.row += 1

    def incrementChat(self):
        self.clearMessages()
        self.forumPage += 1
        self.showMessages()

    def decrementChat(self):
        self.clearMessages()
        self.forumPage -= 1
        self.showMessages()

    def clearMessages(self):
        for widget in self.listOfWidget:
            widget.destroy()
        self.listOfWidget = []


def switchPages(openedPage, desiredPage):
    global currentPage

    removeCode = openedPage+".removeMainFrame()"
    insertCode = desiredPage+".insertMainFrame()"

    exec(removeCode)
    exec(insertCode)

    currentPage = desiredPage


def logUserOut():
    global topMenu
    global accountPage

    userClass.currentAccount = 0
    topMenu.insertLoginOrLogoutButton()
    topMenu.updateWelcomeLabel()
    accountPage.updateAccountInformation()


# Global Website Variables
root = tk.Tk()
# Creates instances of all pages
topMenu = TopMenu(root)
homePage = HomePage(root)
loginPage = LoginPage(root)
registerPage = RegisterPage(root)
accountPage = AccountPage(root)
computerPartsPage = ComputerPartsPage(root)
forumPage = ForumPage(root)


def startGUI():
    global root
    global topMenu
    global homePage
    global loginPage
    global registerPage
    global computerPartsPage

    root.title("TEST TITLE")
    root.geometry("854x480")

    # Sets up main page
    homePage.insertMainFrame()
    topMenu.insertMainFrame()
