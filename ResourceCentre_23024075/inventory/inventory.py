from inventory.camera import Camera
from inventory.laptop import Laptop

class Inventory:
    def __init__(self):
        self.cameraList = []
        self.laptopList = []

    def findAsset(self, assetTag):
        foundAsset = None
        for c in self.cameraList:
            currentTag = c.getAssetTag()
            if currentTag == assetTag:
                foundAsset = c
        for c in self.laptopList:
            currentTag = c.getAssetTag()
            if currentTag == assetTag:
                foundAsset = c
        return foundAsset
    
    def addCamera(self, assetTag, description, opticalzoom):
        # Check for correct values
        correct = True
        if len(assetTag) == 0 or len(description) == 0 or opticalzoom < 0:
            correct = False
            error_message = "Incorrect values."

        # Check for existing camera
        if self.findAsset(assetTag) != None:
            error_message = "Asset already exists."

        if correct and self.findAsset(assetTag) == None:
            new_camera = Camera(assetTag, description, opticalzoom)
            self.cameraList.append(new_camera)
            return True
        else:
            print(error_message)
            return False

    def addLaptop(self, assetTag, description, os):
        # Check for correct values
        correct = True
        if len(assetTag) == 0 or len(description) == 0 or len(os) == 0:
            correct = False
            error_message = "Incorrect values."

        # Check for existing laptop
        if self.findAsset(assetTag) != None:
            error_message = "Asset already exists."

        if correct and self.findAsset(assetTag) == None:
            new_laptop = Laptop(assetTag, description, os)
            self.laptopList.append(new_laptop)
            return True
        else:
            print(error_message)
            return False
        
    def getAvailableCamera(self):
        output = ""
        output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "Zoom")
        if len(self.cameraList) == 0:
            output += "There is no camera to display."
        else:
            for i in self.cameraList:
                if i.getIsAvailable() == "Yes":
                    # Refactor (D): Extract duplicate code as __str__()
                    # If __str__() already created, use it.
                    output += str(i)
            
        return output

       def getNotAvailableCamera(self):
        output = ""
        output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "Zoom")
        if len(self.cameraList) == 0:
            output += "There is no camera to display."
        else:
            for i in self.cameraList:
                if i.getIsAvailable() == "No":
                    # Refactor (D): Extract duplicate code as __str__()
                    # If __str__() already created, use it.
                    output += str(i)
            
        return output

    def getAvailableLaptop(self):
        output = ""
        output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        if len(self.laptopList) == 0:
            output += "There is no laptop to display."
        else:
            for i in self.laptopList:
                if i.getIsAvailable() == "Yes":
                    # Refactor (D): Extract duplicate code as __str__()
                    # If __str__() already created, use it.
                    output += str(i)
        return output
        
    def getNotAvailableLaptop(self):
        output = ""
        output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        if len(self.laptopList) == 0:
            output += "There is no laptop to display."
        else:
            for i in self.laptopList:
                if i.getIsAvailable() == "No":
                    # Refactor (D): Extract duplicate code as __str__()
                    # If __str__() already created, use it.
                    output += str(i)
        return output
        
    def loanAsset(self, assetTag, dueDate):
        success = False
        if len(assetTag) > 0 and len(dueDate) > 0:
            # Refactor (C): use findCamera()
            foundAsset = self.findAsset(assetTag)
            if foundAsset != None:
                if foundAsset.getIsAvailable() == "Yes":
                    foundAsset.setIsAvailable(False)
                    foundAsset.setDueDate(dueDate)
                    success = True
        
        return success
        
    def loanCamera(self, assetTag, dueDate):
        return self.loanAsset(assetTag, dueDate)
    
    def loanLaptop(self, assetTag, dueDate):
        return self.loanAsset(assetTag, dueDate)

    def returnAsset(self, assetTag,):
        success = False
        if len(assetTag) > 0:
            # Refactor (C): use findCamera()
            foundAsset = self.findAsset(assetTag)
            if foundAsset != None:
                if foundAsset.getIsAvailable() == "No":
                    foundAsset.setIsAvailable(True)
                    foundAsset.setDueDate("")
                    success = True
                    
        return success
    
    def returnCamera(self, assetTag):
        return self.returnAsset(assetTag)
    
    def returnLaptop(self, assetTag):
        return self.returnAsset(assetTag)
