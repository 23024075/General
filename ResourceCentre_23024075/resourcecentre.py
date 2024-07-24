from inventory.inventory import Inventory

class ResourceCenter:
    def __init__(self):
        ## Prepare the data (Inventory list)
        self.inventory = Inventory()

    def display_menu(self):
        choice = -1
        while not 1 <= choice <= 5:
            print("\n==============================================")
            print('RESOURCE CENTRE SYSTEM:')
            print("1. Add item")
            print("2. Display Inventory")
            print("3. Loan item")
            print("4. Return item")
            print("5. Quit")
            choice = int(input("Enter your choice >"))
            if not 1 <= choice <= 5:
                print("Invalid choice, please enter again.\n")
        return choice
        
    def displayHeader(self, message):
            print("")
            print("==============================================")
            print(message)
            print("==============================================")

    def selectItemType(self):
        print("\nItem types:")
        print("1. Digital Camera")
        print("2. Laptop")
        option = int(input("Enter option to select item type >"))
        return option
    
    def main(self):
        # Refactor (A): Extract constants for choice integers
        CHOICE_ADD = 1
        CHOICE_VIEW = 2
        CHOICE_LOAN = 3
        CHOICE_RETURN = 4
        CHOICE_QUIT = 5
        # Refactor (A): Extract constants for option integers
        OPTION_CAMERA = 1
        OPTION_LAPTOP = 2

        #### Menu driven application ####
        # Display menu and obtain menu choices
        choice = self.display_menu()

        while choice != CHOICE_QUIT:

            if choice == CHOICE_ADD:
                # Refactor (B): use printHeader(mesage)
                self.printHeader("Add an item")
                
                # Refactor (B): Extract duplicate codes to selectItemType(),
                # return the option selected.
                # Advance refactoring: error chekcing in selectItemType().
                option = self.selectItemType();

                # TO-DO: Write the code to ADD a camcorder or chrome book.
                if option == OPTION_CAMERA:
                    assetTag = input("Enter asset tag >")
                    description = input("Enter description >")
                    opticalZoom = input("Enter optical zoom >")
                    result = self.inventory.addCamera(assetTag, description, opticalZoom)
                    if result:
                        print("Camera",assetTag,"successfully added.")
                    else:
                        print("Error adding digital camera.")

                elif option == OPTION_LAPTOP:
                    assetTag = input("Enter asset tag >")
                    description = input("Enter description >")
                    os = input("Enter OS >")
                    result = self.inventory.addLaptop(assetTag, description, os)
                    if result:
                        print("Laptop",assetTag,"successfully added.")
                    else:
                        print("Error adding laptop.")
            
            elif choice == CHOICE_VIEW:
                # Refactor (B): Extract duplicate codes to printHeader(message)
                self.printHeader("display available items")
                print(self.inventory.getAvailableCamera())
                print(self.inventory.getAvailableLaptop())

                # TO-DO: Write the code to ADD a camcorder or chrome book.
                
            elif choice == CHOICE_LOAN:
                # Refactor (B): use printHeader(mesage)
                self.printHeader("loan an item")
                
                # Refactor (B): use selectItemType()
                option = self.selectItemType();

                # TO-DO: Write the code to LOAN a camcorder or chrome book
                if option == OPTION_CAMERA:
                    print(self.inventory.getAvailableCamera())
                    assetTag = input("Enter asset tag >")
                    duedate = input("Enter due date >")

                    result = self.inventory.loanCamera(assetTag, duedate)

                    if result:
                        print("Camera",assetTag,"successfully loaned out.")
                    else:
                        print("Error loaning camera.")
                elif option == OPTION_LAPTOP:
                    print(self.inventory.getAvailableLaptop())
                    assetTag = input("Enter asset tag >")
                    duedate = input("Enter due date >")

                    result = self.inventory.loanLaptop(assetTag, duedate)

                    if result:
                        print("Laptop",assetTag,"successfully loaned out.")
                    else:
                        print("Error loaning laptop.")
                else:
                    print("Invalid item type.")
                
            elif choice == CHOICE_RETURN:
                # Refactor (B): use printHeader(mesage)
                self.printHeader("return an item")
                # Refactor (B): use selectItemType()
                option = self.selectItemType();

                # TO-DO: Write the code to RETURN a camcorder or chrome book
                if option == OPTION_CAMERA:
                    # Refactor (F): create and use proper method to display loaned camera.
                    # Don't forget to create a pytest for this new method.
                    print("{:<10}{:<30}{:<10}{:<12}{:<10}".format("AssetTag", 
                          "Description", "Available", "Due Date", "Zoom"))
                    for i in self.inventory.cameraList:
                        if i.getIsAvailable() == "No":
                            print("{:<10}{:<30}{:<10}{:<12}{:<10}".format(i.getAssetTag(), \
                            i.getDescription() , i.getIsAvailable(), i.getDueDate(), i.getOpticalZoom()))

                    assetTag = input("Enter asset tag >")

                    result = self.inventory.returnCamera(assetTag)

                    if result:
                        print("Camera",assetTag,"successfully returned.")
                    else:
                        print("Error returning camera.")
                elif option == OPTION_LAPTOP:
                    # Refactor (F): create and use proper method to display loaned Laptop.
                    # Don't forget to create a pytest for this new method.
                    print("{:<10}{:<30}{:<10}{:<12}{:<10}".format("AssetTag", 
                          "Description", "Available", "Due Date", "OS"))
                    for i in self.inventory.laptopList:
                        if i.getIsAvailable() == "No":
                            print("{:<10}{:<30}{:<10}{:<12}{:<10}".format(i.getAssetTag(), \
                            i.getDescription() , i.getIsAvailable(), i.getDueDate(), i.getOs() ))

                    assetTag = input("Enter asset tag >")

                    result = self.inventory.returnLaptop(assetTag)

                    if result:
                        print("Laptop",assetTag,"successfully returned.")
                    else:
                        print("Error returning laptop.")
                else:
                    print("Invalid item type.")

            else:
                print("Invalid choice.")
            
            choice = self.display_menu()

        print("Good bye.")

if __name__ == "__main__":
    app = ResourceCenter()
    app.main()
