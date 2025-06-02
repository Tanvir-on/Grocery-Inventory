import pandas as pd
import matplotlib.pyplot as plt
path = "E:\\practice_python\\Untitled spreadsheet - Sheet1 (1).csv"

def create_inventory():
    while True:
        try:
            csv_file = pd.read_csv(path)
            print("creating new inventory list")
            item_name= input("enter item name: ").capitalize()
            item_category_list = [" ","vegetable", "fruit","dairy product","meat","fish","grain","cerals","snacks","beverages","spices","sweers","bakery","frozen food","ice cream","others"]
            item_category_list_input = int(input("1. vegetable 2. fruit 3. dairy product 4. meat 5. fish 6. grain 7. cerals 8. snacks 9. beverages 10. spices 11. sweers 12. bakery 13. frozen food 14. ice cream 15. others"
            "\nplease enter the category number: "))
            if item_category_list_input == 15:
                others = input("enter others category: ")
                item_category_list.append(others)
                item_category = others

            elif item_category_list_input <= len(item_category_list) and item_category_list_input>0:
                item_category =item_category_list[item_category_list_input]
            else:
                print("wrong keyword")
                continue

            item_price = float(input("enter item price: "))
            item_quantity = int(input("enter item quantity: "))
            item_expiry_date = input("enter item expiry date: ")
            item_availability = int(input("enter item availability:if available then press 1 or if not available then press 0:\n enter your choice: "))
            if item_availability == 1:
                item_availability = "available"
            elif item_availability == 0:
                item_availability = "not available"
            else:
                print("please enter a valid number")
                continue
            item = {
                "item_name": item_name,
                "item_price": item_price,
                "item_quantity": item_quantity,
                "item_category": item_category,
                "item_expiry_date": item_expiry_date,
                "item_availability": item_availability
            }
            df = pd.DataFrame(item, index = [0])
            csv_file = pd.concat([csv_file,df], ignore_index= True)
            csv_file.to_csv(path, index = False)
            print("do you want to add again? if yes then press 1 or if no then press 0: ", end= " ")
            input_response =int(input(" "))
            if input_response == 1:
                continue
            elif input_response == 0:
                print("thak you for using the grocery shop inventory system sir!")
                break
            else:
                print("please enter the actual input:- 1 or 0")
        except ValueError:
            print("please enter a valid number")
            continue
def add_item():
    while True:
        try:
            csv_file = pd.read_csv(path)
            print("creating new inventory list")
            item_name= input("enter item name: ").capitalize()
            
            item_category_list = [" ","vegetable", "fruit","dairy product","meat","fish","grain","cerals","snacks","beverages","spices","sweers","bakery","frozen food","ice cream","others"]
            item_category_list_input = int(input("1. vegetable 2. fruit 3. dairy product 4. meat 5. fish 6. grain 7. cerals 8. snacks 9. beverages 10. spices 11. sweers 12. bakery 13. frozen food 14. ice cream 15. others"
            "\nplease enter the category number: "))
            if item_category_list_input == 15:
                others = input("enter others category: ")
                item_category_list.append(others)
                item_category = others

            elif item_category_list_input <= len(item_category_list) and item_category_list_input>0:
                item_category =item_category_list[item_category_list_input]
            else:
                print("wrong keyword")
                continue

            item_price = float(input("enter item price: "))
            item_quantity = int(input("enter item quantity: "))
            item_expiry_date = input("enter item expiry date: ")
            item = {
                "item_name": item_name,
                "item_price": item_price,
                "item_quantity": item_quantity,
                "item_category": item_category,
                "item_expiry_date": item_expiry_date
            }
            df = pd.DataFrame(item, index = [0])
            csv_file = pd.concat([csv_file,df], ignore_index= True)
            csv_file.to_csv(path, index = False)
        except ValueError:
            print("please enter a valid number")
            continue
def delete_item():
    csv_file = pd.read_csv(path)
    while True:
            try:
                print("deleting item")
                row_number = int(input("enter the row number of the item you want to delete: "))-1
                if row_number<= len(csv_file) and row_number>=0:
                    item_list = [ "item_name", "item_price", "item_quantity", "item_category", "item_expiry_date"]
                    user_input = int(input("1. item_name 2. item_price 3. item_quantity 4. item_category 5. item_expiry_date\nenter your choice:  "))-1
                    if user_input <= len(item_list) and user_input >=0:
                        update_item = " "
                        csv_file.loc[row_number,item_list[user_input]] = update_item
                        csv_file.to_csv(path,index= False)
                        print("deleted successfully")
                        break          
            except ValueError:
                print("please enter a valid number")
                continue   
def update_item():
    csv_file = pd.read_csv(path)
    while True:
            try:
                print("updating item")
                row_number = int(input("enter the row number of the item you want to update: "))-1
                if row_number<= len(csv_file) and row_number>=0:
                    item_list = [ "item_name", "item_price", "item_quantity", "item_category", "item_expiry_date"]
                    user_input = int(input("1. item_name 2. item_price 3. item_quantity 4. item_category 5. item_expiry_date: "))-1
                    if user_input <= len(item_list) and user_input >=0:
                        update_item = input(" Enter the new value: ")
                        csv_file.loc[row_number,item_list[user_input]] = update_item
                        print("update successfully")
                        csv_file.to_csv(path,index= False)
                        break          
            except ValueError:
                print("please enter a valid number")
                continue

def view_inventory():
    try:
        print("showing charts")
        csv_file = pd.read_csv(path)
        print(csv_file)
    except ValueError:
        print("please Enter a valid number")
def clear_inventory():
    while True:
        csv_file = pd.read_csv(path)
        try:
            print("clearing inventory")
            item_list = [ "item_name", "item_price", "item_quantity", "item_category", "item_expiry_date"]
            csv_file = pd.DataFrame(columns= item_list)
            csv_file.to_csv(path, index= False)
            print(" cleared succefully")
            break
        except ValueError:
            print("please enter a valid number")
            continue
def clear_list_of_item():
    csv_file = pd.read_csv(path)
    try:
        print("clearing list of item")
        input_row_number = int( input("enter the row number of the item you want to clear: "))-1
        if input_row_number <= len(csv_file):
            csv_file = csv_file.drop(input_row_number)
            csv_file.to_csv(path, index= False)
            print("cleared successfully")


    except ValueError:
        print("please enter a valid number")
def clear_any_particular_item():
    csv_file = pd.read_csv(path)
    try:
        print("clearing any particular item")
        input_item_name = input("enter the item name?:   ").strip().capitalize()
        csv_file["input_item_name"] = csv_file["item_name"].str.capitalize()
        if input_item_name in csv_file["input_item_name"].values:
            csv_file =csv_file[csv_file["input_item_name"] != input_item_name]
            csv_file.drop("input_item_name", inplace=True,axis=1)
            csv_file.to_csv(path, index = False)
            print("cleared successfully")
        else:
            print("item not found")

    except ValueError:
        print("please enter a valid number")

def plot_graph():
    csv_file = pd.read_csv(path)
    try:
        print("showing charts")

        plt.bar(csv_file["item_name"], csv_file["item_quantity"], color = "green" ,width= 0.5)
        
        plt.tight_layout()
        plt.xlabel("item name")
        plt.ylabel("item quantity")
        plt.title("item price chart")
        plt.show()
    except ValueError:
        print("please enter a valid number")

while True:
    try:
        print("Welcome to Grocery Shop Inventory System!")
        input_values = int(input(""" 
1. Create new inventory list
2. Add item
3. Delete item
4. Update item
5. View inventory
6. Clear inventory
7. clear list of item
8. clear any particular item  
9. Plot graph                     
10. Exit 
please enter your choice number:  """))
        if input_values ==1 :
            create_inventory()
        elif input_values == 2:
            add_item()
        elif input_values == 3:
            delete_item()
        elif input_values == 4:
            update_item()
        elif input_values ==5:
            view_inventory()
        elif input_values ==6:
            clear_inventory()
        elif input_values ==7:
            clear_list_of_item()
        elif input_values ==8:
            clear_any_particular_item()
        elif input_values ==9:
            plot_graph()            
        elif input_values ==10:
            print("Thank you for using the grocery shop inventory system sir!")
            break
        else:
            print("enter a valid number")
            continue
    except ValueError:
        print("please enter a valid number")
        continue
