# import the sys module to manipulate python run time
import sys 
# importing all the required funtion,modules,global variables 
import read
from read import inventory_data,list_item_,items,return_quantity_list,customer_name,return_items_id,phone,rem2,return_items_days,read_receipt,receipt_id,day_fine
import operation
from message import welcome_message, exit_rent_message, exit_message, rent_message, return_message, wrong_choice,invalid_input,return_no_fine,error_not_found
from operation import calculate_price,  check_item_availability, deduct_quantity,return_quantity,pay_advance
from write import deduct_inventory_quantity,receipt,Return_receipt,return_inventory_quantity,Return_receipt_fine

# def item_detail():
# calling funtion of read.py
   

#function for return opt

# main function
def main():
    '''main function of MAIN module is the integreal part of this program which sequentially holds the calling of other funtions and calculation to make the program run as intended'''
#     prints welcome message
    print(welcome_message.__doc__)
#     read modules Read_table is being called which reads from the txt file and converts the information to a table format
    read.Read_table()
#     when the conditions are true the loop starts running
    while True:
#         prints choices to choose from
        print(" ")
        print("Choose an option :\n1. Rent Item \n2. Return Item\n3. Exit")
        print(" ")
#         asks user to enter a choice 
        choice = input("Enter your choice (1, 2, or 3): ")
#         runs functions rescpective to choice
        if choice == "1":
            rent_option()
        elif choice == "2":
            return_option()
        elif choice == "3":
            print(" ")
            print(exit_message.__doc__)
            sys.exit()
        else:
#           if choce is other than 1 or 2 or 3 error message is printed
            print(wrong_choice.__doc__)
            
#      initiating variable to store data repectively
# variable to store the current selected Id of item
selected_ID = 0
# variable to store the current entered quantity of the item
quantity=0
# to check the condition to whether run or not to run the loop
isReturned = False
# to store all the selected IDs
selectedID = []
# to store the price of all the selected Ids
amount_list = []
# to store the quantity of all the selected Ids
quantity_list = []
# to store the number of days the item is rented for 
days_list=[]
# variable to store advance amount entered by user 
advance = 0

def return_option():
    """this function is the function handling all the return process step-by-step"""
#     prints return message 
    print()
    print(return_message.__doc__)
    print()
#     rem2 is cleared so the data of one customer doesnot interfere in other customers
    rem2.clear()
# list of flags to decide the flow of program and changing those flags value results in changing the course of program.
    flag_list = [False,False,False]
    flag4 = flag_list[1]
    if flag4 == False:
        read_receipt(flag_list)
    flag5 = flag_list[0]
    flag6 = flag_list[2]
    
    
    if flag5 == True:
#         return_quantity is called which returns the number of quantity to the inventory. maintain stocks 
         return_quantity(inventory_data, return_items_id, return_quantity_list)

#          this function is called to write the updated table in text file 
         return_inventory_quantity(inventory_data)
#          this function is called to print and write the reciept.
         Return_receipt(receipt_id,isReturned,flag_list)

#         prints a line indicating updated table 
         print("_______________________________Updated Table_______________________________")
#          this funtion s called to show the updated table in the shell
         read.print_table()
#          clear the list so new entry can be made with no interference 
         receipt_id.clear()
         return_quantity_list.clear()
#          call the main funtion to return to first interface
         main()
    elif flag6 == True:
        return_quantity(inventory_data, return_items_id, return_quantity_list)
        
#         this function is called to write the updated table in text file 
        return_inventory_quantity(inventory_data)
#         this function is called to print and write the reciept.
        Return_receipt_fine(receipt_id,isReturned,flag_list,day_fine)
        print("_______________________________Updated Table_______________________________")
#     this funtion s called to show the updated table in the shell
        read.print_table()
#          clear the list so new entry can be made with no interference 
        receipt_id.clear()
        return_quantity_list.clear()
 #          call the main funtion to return to first interface
        main()
#         displays exit message
    print(exit_rent_message.__doc__)
    
def rent_option():
    """This funtion holds all the calling of related function to complete the rent process"""
#     print rent message
    print(" ")
    print(rent_message.__doc__)
    print(" ")
#     call the function to display table
    read.print_table()
#     calculate the number of item present in the store
    NoOfitemInShop = len(inventory_data)
#     ask customer name and storing it in a variable
    Customer_name = input("Please enter your name : ")
#     if the customer name is empty ask the name again
    if Customer_name == '':
        rent_option()
    name = Customer_name
# ask phone number to the user and if the number is empty repeat the process 
    PhNumber = input("Please enter phone number : ")
    if PhNumber == '':
        rent_option()
    rem2.clear()
    
    def rent_item():
#"""this function is to ask the series of question to user to carry out rent process """
#         Boolean values to check whether ro run or stop the program
            flag1 = True
            flag2 = True
            isTrue = True
#             continuing when isTrue is True
            while isTrue:
#continuing if flag2 and flag1 is true 
                    while flag1:
                        while flag2:
#                             Try except to hangle any exceptions 
                            try:
#                                 ask the id with the user 
                                ID_select = int(input("Mr/Mrs. " + Customer_name +" Please Select ID of the required Item : "))
#                                 check if the ID entered is present in store or not
                                if ID_select > NoOfitemInShop :
#                                     display error if not present
                                    print("Sorry we don't have item with",ID_select,"ID.")
                                    print()
#                                     stop the loop
                                    flag1 = False
#                                     repeat rent_item funtion 
                                    rent_item()
#                                 check if the ID is 0 or negative 
                                elif ID_select < 0 :
#                                     if yes print error 
                                    print("ID cannot be negative .")
                                    print()
#                                     stop the loop and repeat rent_item
                                    flag1 = False
                                    rent_item()
#                                if the entries are correct then continue 
                                else:
#                                     this holds the value of required quantity entered by customer 
                                    required_quantity = int(input("Please enter the required quantity : "))
#                                     this function check if the item is available or not using property of nested dictionary
                                    if check_item_availability(inventory_data[ID_select]["Quantity"], required_quantity):
#                                         this functions deducts the quantity rented from the stocks 
                                        deduct_quantity(inventory_data, ID_select, required_quantity, quantity_list)
#                                         the id selected is added to a list 
                                        selectedID.append(ID_select)
#                                         boolean to mantain flow
                                        flag7 = True
#                                         number of days is stored in days
                                        days = int(input("How many days do you want this item for : "))
                                        while flag7:
#                                             continue when flag7 is true 
                                            if days <=0:
                                                print("Days cannot be 0 or less than 0.")
                                                flag7 = False
                                            else:
                                                # Calculate price and manage inventory by using related functions 
                                                price_sameItem_bulk = calculate_price(required_quantity, inventory_data[ID_select]["Price"], days,amount_list)
                                                days_list.append(days)
                                                    
                                                deduct_inventory_quantity(inventory_data)
                                
                                                another_item = (input("Do you want to rent other items ? Enter 'n' to exit and 'y' to continue : ").lower())
                                                if another_item == 'n':
                                                    # calculate remaining amount, display and write receip and update table and display updated table 
                                                    remaining_amount = pay_advance(amount_list,rem2)
                                                    print()
                                                    receipt(Customer_name,selectedID,amount_list,quantity_list,days_list,PhNumber,isReturned,remaining_amount)
                                                    
                                                    print(exit_rent_message.__doc__) 
                                                    print()
                                                    print()
                                                    print("_______________________________Updated Table_______________________________")
                                                    read.print_table()
                                                    print()
                                                    print()
                                                    selectedID.clear()
                                                    quantity_list.clear()            
                                                    main()  
                                                else:
                                                    print()
                                                    print()
                                                    print("_______________________________Updated Table_______________________________")
                                                    print()
                                                    read.print_table()
                                                    print()
                                                    rent_item()
                                        
                            except ValueError:
#                                 print error if value entered is wrong format
                                print()
                                invalid_input()
                                print()
#     call rent_item funtion
    rent_item()
#     call main() funtion
main()



