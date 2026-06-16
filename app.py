import json
import os
import sys

products = {}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_db(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f)

def load_db(filename="data.json"):
    # If file does not exist, create it with empty dict
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump({}, f)
        return {}

    # If file exists but is empty or invalid JSON, reset it
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        with open(filename, "w") as f:
            json.dump({}, f)
        return {}

products = load_db()

def Add_product():
    clear_console()
    try:
        print("=== Add Product ===\n")
        Name = str(input("1-Product Name:")).upper()
        Price = int(input("2-Price:"))
        if Price <0 :
            clear_console()
            print("Price More or equal to 0")
            input("Press Enter to Back to The Menu")
            return
        Quantity = int(input("3-Quantity:"))
        if Quantity <0:
            clear_console()
            print("Quantity need to be equal or more then 0")
            input("Press Enter to Back to The Menu")
            return
        products[Name] = dict(price_value = Price , quantity_value = Quantity)
        clear_console()
        print("Product Added!\n")
        print("*Name:",Name,"\n*Price:",products[Name]["price_value"], "\n*Quantity:",products[Name]["quantity_value"])
        input("Press Enter to Back to The Menu")
    except ValueError:
        print("Invalid Input")    

def View_Products():
    clear_console()
    if not products:
        clear_console()
        print("List Is Empty!")
        input("Press Enter to Back to The Menu")
        return
    print("=== List Of Products ===\n") 
    for i in products:
        print("*Name:",i,"\n*Price:",products[i]["price_value"], "\n*Quantity:",products[i]["quantity_value"],"\n===================")
    input("Press Enter to Back to The Menu")
    
def Search_Product():
    clear_console()
    print("=== Search For Product ===\n")
    if not products:
        print("Nothing in DB")
        return 
    Search = str(input("Name Of Product: ")).upper()
    if Search not in products:
        clear_console()
        print("Product Not In DB!")
        input("Press Enter to Back to The Menu")
        return
    clear_console()
    print("=== Found It!! ===\n")
    print("*Name:",Search,"\n*Price:",products[Search]["price_value"], "\n*Quantity:",products[Search]["quantity_value"])
    input("Press Enter to Back to The Menu")

def Delete_Product():
    clear_console()
    if not products:
        print("Nothing in DB")
        input("Press Enter to Back to The Menu")
        return   
    print("=== Delete Product ===\n")
    Name = str(input("Name Of Prudct:")).upper()
    if Name not in products:
        clear_console()
        print("Product Not In DB!")
        input("Press Enter to Back to The Menu")
        return
    products.pop(Name)
    clear_console()
    print("Product Delete Successfully!!")
    input("Press Enter to Back to The Menu")

def Update_Quantity():
    clear_console()
    if not products:
        print("Nothing in DB")
        input("Press Enter to Back to The Menu")
        return   
    print("=== Update Quantity ===\n")
    Name = str(input("Name Of Prudct:")).upper()
    if Name not in products:
        clear_console()
        print("Product Not In DB!")
        input("Press Enter to Back to The Menu")
        return
    new_value = int(input("New Value of Quantity:"))
    products[Name]["quantity_value"] = new_value
    clear_console()
    print("Product Quantity Edited Successfully!!")
    input("Press Enter to Back to The Menu")

def Sell_Product():
    clear_console()
    if not products:
        print("Nothing in DB")
        input("Press Enter to Back to The Menu")
        return   
    print("=== Sell Product ===\n")
    Name = str(input("Name Of Prudct:")).upper()
    if Name not in products:
        clear_console()
        print("Product Not In DB!")
        input("Press Enter to Back to The Menu")
        return
    num_sell = int(input("How much You Want to Sell:"))
    if num_sell > products[Name]["quantity_value"]:
        print("You Cant Sell That Much You Dont Have Stock!!!")
        input("Press Enter to Back to The Menu")
        return
    else:
       products[Name]["quantity_value"] = products[Name]["quantity_value"] - num_sell

    clear_console()
    print("Product Sell Successfully!!\n")
    print("You Have",products[Name]["quantity_value"], "Remaining\n")
    input("Press Enter to Back to The Menu")




while True:
    clear_console()
    print("=== Inventory Management System ===\n")
    print("1. Add Product\n2. View Products\n3. Search Product\n4. Delete Product\n5. Update Quantity\n6. Sell Product\n7. Quit")
    Choise = int(input())
    if Choise == 1:
        Add_product()
        save_db(products)
    elif Choise == 2:
        View_Products()
    elif Choise == 3:
        Search_Product()
    elif Choise == 4:
        Delete_Product()
        save_db(products)
    elif Choise == 5:
        Update_Quantity()
        save_db(products)
    elif Choise == 6:
        Sell_Product()
        save_db(products)