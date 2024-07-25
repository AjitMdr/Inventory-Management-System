from message import returned_already

inventory_data= {}
items = {}
phone = []
rem2 = []
tot3 = []
return_items_name = []
return_quantity_list = []
return_items_id = []
return_items_days = []
list_item_ = []
returned = []
receipt_id = []
customer_name = []
day_fine = []
def Read_table():
    list1=[]            # initiating a list
    file = open("inventory.txt","r")  # opening a file in read mode
    lines=file.read().splitlines()            # reading lines present in the txt file\
    file.close()
    
    for i in range(0,len(lines)):     # iterating through lines in from the text files
        for j in range(0,4):          # iterating through words in lines 
            DATA=lines[i].split(",")  # splitting the data seperated by "," from lines iterated
            list1.append(DATA[j])            # appending/ading data iterated from .txt file to list
       
    for i in range(len(lines)):              # starting another loop from i to (number of lines - 1)
    # for starting value(index)
        index = i * 4                        # index being the starting point , i * 4 in loop gives values 0,4,8,12,... 
        name = list1[index]                  # name is assinged  the value which we get from list1[index] . for example name = 0th item of list
        brand = list1[index + 1]             # index + 1 increces the value by 1 , which means for first loop its value will be 1, for 2nd loop 5,...
        price = float(list1[index + 2].replace('$', '')) # here $ is replace by " " and for first loop its value will start from 2.
        quantity = int(list1[index + 3])     # for first loop its value will start from 3
        inventory_data[i + 1] = {     # the values above given to name,brand,price,quantity will be stored in the inventory_data dictionary under key 1,2,3,4,...(value of i from for loop)
            'Name': name,
            'Brand': brand,
            'Price': price,
            'Quantity': quantity
                }
    
Read_table()
def print_table():
    #CREATING OF TABLE USING FORMAT
    header_row = "{:<3} {:<30} {:<20} {:<10} {:<8}".format("ID", "Name", "Brand", "Price", "Quantity") #headers and size/" "(spaces). {:<30}= 30 > spaces 
    formatted_rows = []
    for item_id,item_data in inventory_data.items():
        formatted_row = "{:<3} {:<30} {:<20} ${:<8.2f}     {:<8}".format(  #storing price as float with 2 place after decimal and $ sign is added before price 
            item_id, item_data['Name'], item_data['Brand'], item_data['Price'], item_data['Quantity'])
        formatted_rows.append(formatted_row) #adding rows from dictionary in loop
    #printing table header
    print(header_row)
    print('-'*len(header_row))
    print('\n'.join(formatted_rows))
    print('-'*len(header_row))
    print()

customer_names = []
item_list = []

def read_receipt(flag_list):
    """this function is created to read the reciept and show tht data in table format and do some basic calculation."""
    
#   try except are used to check correct data types and if the file is present or not where required in this code   
    try:
#       ID is requested from the user and checke   
        ReceiptID = input("Enter ID of the reciept: ")
#         add the id to list
        receipt_id.append(ReceiptID)
#         open file of id entered
        file = open(f"{ReceiptID}.txt", "r")
        lines = file.read().splitlines()
        print()
#         print a line with rented item written in middle
        print("-" * 35, "RENTED ITEMS", "-" * 35)
        print()
#         print a formatted header
        print("{:<10} {:<30}   {:<20}{:<10}{:<10}".format("Item ID", "Item Name", "Brand", "Quantity", "Days"))
#        print a line to close table
        print("-" * 84)
#        get values from the reciept and seperate only the required value and add it to dictionary and lists as required.
# Strip removes the not selected data, split seperates the data 
        for line in lines:
            if line.startswith("Item ID"):
                items = {}
#                 Create a dictionary for each time
                items["ID"] = line.split(":")[1].strip()
                id__ = items["ID"]
                return_items_id.append(int(id__))
            elif line.startswith("Customer"):
                 name = line.split(":")[1].strip()
                 customer_name.append(name)
            elif line.startswith("Items Returned "):
                items["returned"] = line.split(":")[1].strip().lower()
                returned.append(items["returned"])
            elif line.startswith("Phone number"):
                number = line.split(":")[1].strip()
                phone.append(number)
            elif line.startswith("Remaining Amount"):
                remaining_= line.split(":")[1].strip().replace("$",'')
                items["remaining"] = line.split(":")[1].strip().replace("$",'')
                rem2.append(remaining_)
            elif line.startswith("Total Amount"):
                items["total"] = line.split(":")[1].strip().replace("$",'')
                tot3.append(items["total"])
            elif line.startswith("Item name"):
                items["Name"] = line.split(":")[1].strip()
            elif line.startswith("Brand"):
                items["Brand"] = line.split(":")[1].strip()
            elif line.startswith("Quantity"):
                 items["Quantity"] = line.split(":")[1].strip()
                 q__ = items["Quantity"]
                 return_quantity_list.append(q__)
            elif line.startswith("Days"):
                 items["Days"] = line.split(":")[1].strip()
                 dayy = items["Days"]
                 return_items_days.append(dayy)
                 list_item_.append(items.copy())
                 print("{:<10} {:<30}   {:<20}  {:<10}{:<10}".format(items["ID"], items["Name"], items["Brand"], items["Quantity"], items["Days"]))
        print("-" * 84)
#         give value to remaining_amount after reading and extracting from txt file
        remaining_amount = float(items["remaining"])
# check if the item is already returned 
        if returned[0] == True:
            returned_already()
#            if not returned continue these processes 
        else:
            print()
#             try except to find and handle any exceptions
            try:
                days_return = int(input("Within how many days are you returning the items: "))
#                 ask days from user
                if days_return <= 0:
                    print("Days cannot be negative or zero.")
#                     print message
                    read_receipt(flag_list)
#                     call read_receipt funtion

# check the return days if more calculate fine if not continue normally
                if days_return <= int(items["Days"]):
                    print("Your remaining amount is: $",round(float(items["remaining"]),))
#                     display remaining amount and initiate payment process

# loop for payment process 
                    while remaining_amount > 0:
                        try:
                            paid = float(input("Please pay the remaining amount: "))
#                             ask use to pay
                            (remaining_amount) -= paid
#                             update the remaining amount and handle payment process 
                            if remaining_amount == 0:
                                print("All bills cleared")
#                                 print message 
                                flag_list[0] = True
#                                 set flag_list's first value to True
                            elif remaining_amount < 0:
                                print("Thank you for the tip.")
                                flag_list[0] = True
     #                                 set flag_list's first value to True 
                            elif paid < 0:
                                print("Payment amount cannot be negative ")
                                
                            else:
                                print("Remaining amount to be paid: $", remaining_amount)
                                
                        except ValueError:
                            print("Invalid input. Please enter a valid numeric value.")
                            
                elif days_return < 0:
                    print("Days cannot be negative.")
                else:
                    dayFine = days_return 
                    day_fine.append(dayFine)
                    print()
                    print("Total Amount :$",tot3[0])
                    print()
                    print("A nominal fee has been applied due to the delayed return of the item.")
                    print()
#                     apply fine if the day noted at renting is less than returned days 
                    if days_return > 5:
                        fine = days_return/5 * float(tot3[0]) + float(tot3[0])/10
                    else:
                        fine = days_return * float(tot3[0]) + float(tot3[0])/10
                    print("Total amount with added fine :$",fine)
                    while fine > 0:
                        try:
                            paid = float(input("Please pay the remaining amount :"))
                            fine -= paid
#                             above proces is to pay fine 
#                             check if the fine is 0
                            if fine == 0:
                                print("All bills cleared")
                                #                 print  message
                                flag_list[2] = True
                                #                   set value of flag_list 3rd item to True
                            elif fine < 0:
                                print("Thank you for the tip.")
                                #                 print  message
                                flag_list[2] = True
                             #                   set value of flag_list 3rd item to True
                            elif paid < 0:
                                print("Payment amount cannot be negative ")
                                #                 print error message
                                
                            else:
                                print("Remaining amount to be paid: $", fine)
                                #                 print error message
                        
                        except ValueError:
                            print("Invalid input. Please enter a valid numeric value.")
                            #                 print error message
            except ValueError:
                print("Invalid input for days. Please enter a valid numeric value.")
#                 print error message

    except FileNotFoundError:
       print("The specified file was not found.")
#        print message
#        clear the list values
       receipt_id.clear()
       rem2.clear()