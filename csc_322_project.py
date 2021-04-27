import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("TEST TITLE")
    root.geometry("854x480")

    class Products:
        product_id = ""
        price = 0
        description = ""
        number_sold = 0
        company_name = ""
        def __init__(self,productId,p,d,numb):
            self.product_id = productId
            self.price = p
            self.description = d
            self.number_sold = numb

    class Accounts:
        email = ""
        password = ""
        name = ""
        card_number = 0
        exp_date = 0
        purchases = []
        
        def __init__(self,productId,p,d,numb):
            self.product_id = productId
            self.price = p
            self.description = d
            self.number_sold = numb

    # Background frame everything is contained in
    mainFrame = tk.Frame(root,bg='white')
    mainFrame.place(relwidth=1,relheight=1)

    # Label Canvas
    titleFrame = tk.Frame(mainFrame,bg='grey')
    titleFrame.place(relx=0.25,relwidth=0.50,relheight=0.15)

    # Website Title
    titleText = tk.Label(titleFrame,text="Cook n' Look",font=("Arial", 50))
    titleText.pack()

    # Bounding box for dropdown menu
    dropdownFrame = tk.Frame(mainFrame, bg='grey')
    dropdownFrame.place(relx=0.05,relwidth=0.9,rely=0.15,relheight=0.07)

    # Bounding box for login and register
    loginRegisterFrame = tk.Frame(mainFrame,bg='grey')
    loginRegisterFrame.place(relx=0.8,relwidth=0.15,rely=0.05,relheight=0.09)

    # Bounding box for bestsellers
    bestSellersFrame = tk.Frame(mainFrame,bg='grey')
    bestSellersFrame.place(relx=0.05,rely=0.3,relwidth=0.9,relheight=0.28)

    # Bounding box for recommended
    recommendedFrame = tk.Frame(mainFrame,bg='grey')
    recommendedFrame.place(relx=0.05,rely=0.65,relwidth=0.9,relheight=0.28)

    # Dropdown Buttons
    homeButton = tk.Button(dropdownFrame,text='home')
    homeButton.grid(row=0,column=0,pady=5,padx=5)

    computerPartsButton = tk.Button(dropdownFrame,text='computer parts')
    computerPartsButton.grid(row=0,column=1,pady=5,padx=5)

    # Login Register Buttons
    loginButton = tk.Button(loginRegisterFrame,text='Login')
    loginButton.grid(row=0,column=0,pady=5,padx=5)

    registerButton = tk.Button(loginRegisterFrame,text='Register')
    registerButton.grid(row=0,column=1,pady=5,padx=5)


    ## Saving info from textfiles into objects

    # Products text file contents

    products_txt = open("C:/Users/ID140/Documents/products.txt",'r')
    productsList = []

    for line in products_txt:
        
        data = line.split("+")

        print(data)
        
        product_id = data[0]
        price = data[1]
        description = data[2]
        number_sold = data[3]

        current_product = Products(product_id,price,description,number_sold)
        productsList.append(current_product)

    products_txt.close()

    # Accounts text file contents

    accounts_txt = open("C:/Users/ID140/Documents/accounts.txt",'r')
    accountsList = []

    for line in accounts_txt:
        
        data = line.split("+")

        print(data)
        
        product_id = data[0]
        price = data[1]
        description = data[2]
        number_sold = data[3]

        current_product = Accounts(product_id,price,description,number_sold)
        accountsList.append(current_product)

    accounts_txt.close()



    root.mainloop()





    

    # Cpu
    # Gpu
    # Ram
    # HDD
    # OS
    # Powersupply
    # The Use (Gaming, Business, etc)


    # for loop 
    #
    # if(cpu_dropdown == cpu_list && gpu_dropdown == gpu_list && 
    #
    #
    #
    # filtered list
    #
    #