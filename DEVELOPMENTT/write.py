
import datetime
from read import read_receipt,inventory_data,customer_name,items,return_quantity_list,return_items_id,return_items_name,return_items_days,phone,rem2,day_fine,tot3

# funtion to write the updated data after items are rented   
def deduct_inventory_quantity(inventory_data):
    # Open the 'inventory.txt' file in write mode
    file = open("inventory.txt", "w")
    # Iterate through each key-value pair in the inventory_data dictionary
    for key, value in inventory_data.items():
        # Construct a line of data to write to the file
        line = f"{value['Name']},{value['Brand']},${value['Price']},{value['Quantity']}\n"
        # Write the line to the file
        file.write(line)
    # Close the file
    file.close()

# funtion to write the updated data after items are returned    
def return_inventory_quantity(inventory_data):
    # Open the 'inventory.txt' file in write mode
    file = open("inventory.txt", "w")
    # Iterate through each key-value pair in the inventory_data dictionary
    for key, value in inventory_data.items():
        # make a line of data to write to the file
        line = f"{value['Name']},{value['Brand']},${value['Price']},{value['Quantity']}\n"
        # Write the line to the file
        file.write(line)
    # Close the file
    file.close()


# funtion to print and write a receipt
def receipt(Customer_name,selectedID,amount_list,quantity_list,days_list,PhNumber,isReturned,remaining_amount):
#    to get local date and time 
    _datetime = datetime.datetime.now()
    _date = datetime.datetime.now()
#    getting only 2 digit after decimal
    decimal_two = round(sum(amount_list),2)
#     formatting date and time 
    formatted_datetime = _datetime.strftime("%Y/%m/%d %H:%M:%S")
    formatted_date = _date.strftime("%Y-%m-%d_%S")
#     creating a unique receipt ID 
    receipt_id = f"{formatted_datetime}-{Customer_name}"
    print()
#     printing a receipt including ID,customer name , phone number, item name, brand , quantity,days rented for, returned (true or false), total amount,remaining amount ,date and time of rent
    print(f"------------Receipt #{formatted_date}_{Customer_name}------------")
    print("Customer  :",Customer_name)
    print("Phone number :",PhNumber)
    for i in range(len(selectedID)):
        print("Item ID   :",selectedID[i])
        print("Item name :",inventory_data[selectedID[i]]["Name"])
        print("Brand     :",inventory_data[selectedID[i]]["Brand"])
        print("Quantity  :",quantity_list[i])
        print("Days      :",days_list[i])
        print("Price     :$",round(amount_list[i],2))
        print("-----------------------------------------------------------")
    print("Items Returned :",isReturned)
    print("Remaining Amount : $",remaining_amount)
    print("Total Amount : $",decimal_two)
    print("-----------------------------------------------------------")
    print('                                     ',formatted_datetime)
    print("-----------------------------------------------------------")
    print()
    print()
#     writting a receipt including ID, item name, brand , quantity,days rented for, returned ( false), total amount,remaining amount ,date and time of return
    receipt_filename = f"{Customer_name}_{formatted_date}.txt"  # create the receipt file name
#     opening file with the above created name to write the receipt
    file = open(receipt_filename, "w")
    file.write("-------------------------Receipt--------------------------\n")
    file.write("Receipt ID : "f"{Customer_name}_{formatted_date}"+"\n")
    file.write("Customer  : " + Customer_name + "\n")
    file.write("Phone number  : " +PhNumber+ "\n")
    for i in range(len(selectedID)):
        file.write("Item ID   : " + str(selectedID[i]) + "\n")
        file.write("Item name : " + inventory_data[selectedID[i]]["Name"] + "\n")
        file.write("Brand     : " + inventory_data[selectedID[i]]["Brand"] + "\n")
        file.write("Quantity  : " + str(quantity_list[i]) + "\n")
        file.write("Days      : " + str(days_list[i])+ "\n")
        file.write("Price     : $"+str(round(amount_list[i],2)) + "\n")
        file.write("----------------------------------------------------------\n")
    file.write("Items Returned   :"+str(isReturned)+"\n\n")
    file.write("Remaining Amount : $ "+str(remaining_amount)+ "\n")
    file.write("Total Amount     : $"+str(decimal_two) + "\n")
    file.write("---------------------------------------------------------\n")
    file.write(str('                                     '+(formatted_datetime))+"\n")
    file.write("----------------------------------------------------------\n")
    print()
    
#     prints id of the receipt
    print(f"Receipt saved as '{receipt_filename}'")
    print()
    quantity_list.clear()
    amount_list.clear()
    tot3.clear()
# prints and writes receipt after the items are returned 
def Return_receipt(receipt_id,isReturned,flag_list):
#     sets the value of isReturned to true which indicates the items are returned 
    isReturned = True

# gets the id stored in the list 
    r_id = receipt_id[0]
#  file name 
    receiptID = f"{r_id}.txt"
#     formatted local date time
    _Returndatetime = datetime.datetime.now()
    return_formatted_datetime = _Returndatetime.strftime("%Y/%m/%d %H:%M:%S")
    print()
#     prints the bill with informations including ID,customer name, item name, brand , quantity,days rented for, returned (true), total amount,remaining amount ,date and time of rent
    print(f"===========================Receipt #{receipt_id[0]}===========================")
    print("Customer  :",customer_name[0])
    print("-" * 84)
    for q in range (len(return_items_id)):
        print("Item ID   :",return_items_id[q])
        print("Item name :",inventory_data[return_items_id[q]]["Name"])
        print("Brand     :",inventory_data[return_items_id[q]]["Brand"])
        print("Quantity  :",return_quantity_list[q])
        print("Days      :",return_items_days[q])
        print("-----------------------------------------------------------")
    print("Total Amount:",tot3[0])
    print("Items Returned :",isReturned)
    print("Remaining Amount : $0")
    print("                                     ",return_formatted_datetime)
    print()
    print()
#    set true falue for flag which is used to continue the program to the next step without repeating other unwanted steps 
    flag_list[1] = True
#     writes the bill with informations including ID,customer name, item name, brand , quantity,days rented for, returned (true), total amount,remaining amount ,date and time of rent
    file = open(f"{receipt_id[0]}.txt", "w")
    file.write("\n")
    file.write(f"===========================Receipt #{receiptID}===========================\n")
    file.write(f"Customer  : {customer_name[0]}\n")
    for r in range(len(return_items_id)):
        file.write(f"Item ID   : {return_items_id[r]}\n")
        file.write(f"Item name : {inventory_data[return_items_id[r]]['Name']}\n")
        file.write(f"Brand     : {inventory_data[return_items_id[r]]['Brand']}\n")
        file.write(f"Quantity  : {return_quantity_list[r]}\n")
        file.write(f"Days      : {return_items_days[r]}\n")
        file.write("----------------------------------------------------------\n")
    file.write(f"Total Amount     : ${tot3[0]}\n")
    file.write("\nAll bills cleared")
    file.write("\nRemaining Amount : $ 0\n")
    file.write(f"Items Returned : True\n")
    file.write(f"                                                      {return_formatted_datetime}\n\n")
    file.close()
#     prints the id of receipt
    print("Reciept save as",receipt_id[0],".txt")
    return_items_id.clear()
    tot3.clear()
 #     prints and writes the bill 
def Return_receipt_fine(receipt_id,isReturned,flag_list,day_fine):
    isReturned = True
    r_id = receipt_id[0]
    receiptID = f"{r_id}.txt"
    _Returndatetime = datetime.datetime.now()
    return_formatted_datetime = _Returndatetime.strftime("%Y/%m/%d %H:%M:%S")
    print()
#    prints reciept with informations including ID,fined amount ,customer name, item name, brand , quantity,days rented for, returned (true), total amount,remaining amount ,date and time of rent
    print(f"===========================Receipt #{receipt_id[0]}===========================")
    print()
    print("Customer  :",customer_name[0])
    print("-" * 82)
    for q in range (len(return_items_id)):
        print("SN        :",q+1)
        print("Item ID   :",return_items_id[q])
        print("Item name :",inventory_data[return_items_id[q]]["Name"])
        print("Brand     :",inventory_data[return_items_id[q]]["Brand"])
        print("Quantity  :",return_quantity_list[q])
        print("Day Returned for:",return_items_days[0])
        print("-----------------------------------------------------------")
    print("Fine Amount      :$",(float(tot3[0])*(float(day_fine[0])/5)+(float(tot3[0])/10)-float(tot3[0])))
    print("Total Amount     :$",(float(tot3[0])*(float(day_fine[0])/5)+(float(tot3[0])/10)))
    print("Items Returned   :",isReturned)
    print("Remaining Amount : $0")
    print("                                     ",return_formatted_datetime)
    print()
    print()
#    set true falue for flag which is used to continue the program to the next step without repeating other unwanted steps 
    flag_list[1] = True 
#    writes reciept with informations including ID,fined amount ,customer name, item name, brand , quantity,days rented for, returned (true), total amount,remaining amount ,date and time of rent
    file = open(f"{receipt_id[0]}.txt", "w")
    file.write("\n")
    file.write(f"===========================Receipt #{receiptID}===========================\n")
    file.write(f"Customer  : {customer_name[0]}\n")
    for r in range(len(return_items_id)):
        file.write(f"Item ID   : {return_items_id[r]}\n")
        file.write(f"Item name : {inventory_data[return_items_id[r]]['Name']}\n")
        file.write(f"Brand     : {inventory_data[return_items_id[r]]['Brand']}\n")
        file.write(f"Quantity  : {return_quantity_list[r]}\n")
        file.write(f"Days      : {return_items_days[r]}\n")
        file.write("----------------------------------------------------------\n")
    file.write(f"Total Amount     : ${tot3[0]}\n")
    file.write("Total Amount with fine :$"+str(float(tot3[0])*(float(day_fine[0])/5)+float(tot3[0])/10)+"\n")
    file.write("\nAll bills cleared")
    file.write("\nRemaining Amount : $ 0\n")
    file.write(f"Items Returned : True\n")
    file.write(f"                                                      {return_formatted_datetime}\n\n")
    file.close()
#     prints the id of receipt
    print("Reciept saved as",receipt_id[0])
    return_items_id.clear()
    tot3.clear()

