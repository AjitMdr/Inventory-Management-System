# importin all the parameters required for the fomulas used from read 
from read import inventory_data, items,return_quantity_list,return_items_id

# funtion for calculating price of the rented equipments 
def calculate_price(quantity, item_price, days,amount_list):
# price must be calculated for all the items rented per five day
    per_5days = days / 5
# this formula give price for multiple quantity of same type of item times value of per five days.
    price_sameItem_bulk = (quantity * item_price) * per_5days
#     adds the above outcome to a list 
    amount_list.append(price_sameItem_bulk)
# returns value 
    return price_sameItem_bulk


# funtion to calculate the remaining amount after paying advance 
def pay_advance(amount_list,rem2):
# total amount (sum of price of all the selected items per 5 day)
    
    Total =round(sum(amount_list),2)
#     prints total amount 
    print("Total Amount : $",Total)
#     try except to tackle number format  error
    try:
#         # Take the advance payment from the user
        advance = float(input("Please pay some amount (advance): "))
        
        if advance >= Total:
            print("Advance must be less than the total amount.")
            return pay_advance(amount_list, rem2)  # Recur to get a valid advance
        elif advance <= 0:
            print("Amount cannot be negative or zero.")
            return pay_advance(amount_list, rem2)  # Recur to get a valid advance
        else:
            # Calculate the remaining amount
            remaining_amount = Total - advance
            rem2.clear()
            rem2.append(remaining_amount)
            return remaining_amount
    except ValueError:
        print("please enter numeric value")
        pay_advance(amount_list,rem2)
        
def check_item_availability(item_quantity, required_quantity):
    """function to check the availability of items. this funtion compares the quantity entered is valid or
not and compares it to the present quantity and continues the flow if the quantity present is more or equal to the quantity entered """
    if item_quantity < required_quantity:
        print("Sorry, we don't have enough quantity of this item.")
        return False
    elif required_quantity == 0:
        print("Sorry, quantity cannot be zero.")
        return False
    elif required_quantity < 0:
        print("Sorry, quantity cannot be negative.")
        return False
    return True

def deduct_quantity(inventory_data, ID_select, required_quantity, quantity_list):
    """This function takes all the arguments and deducts the entered quantity from the stocks"""
#     calculates the new quantity after deducting the rented quantity
    new_quantity = inventory_data[ID_select]["Quantity"] - required_quantity
#     updates the inventory data with the new quantity
    inventory_data[ID_select]["Quantity"] = new_quantity
#     keeps track ot rented quantity in the quantity_list
    quantity_list.append(required_quantity)

"""This function takes all the arguments and add the returned quantity from the stocks"""
def return_quantity(inventory_data, return_items_id, return_quantity_list):
    for w in range(len(return_items_id)):
#         for loop is to get the number from 0 to the len of the list
        item_id = return_items_id[w]
#         giving values of item id from return_items_id one by one to item_id
        new_quantity = inventory_data[int(item_id)]["Quantity"] + int(return_quantity_list[w])
        inventory_data[int(item_id)]["Quantity"] = new_quantity
#           calculating the new value of quantity after returning the items     




    
