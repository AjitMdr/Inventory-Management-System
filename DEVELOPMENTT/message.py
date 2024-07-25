# docstring which has a welcome message 
def welcome_message():
    """
    ************************************************************************************************************
    *                                       WELCOME TO RENTAL SHOP                                             *
    ************************************************************************************************************ 
    """
# docstring which has message for returning to the home page 
def exit_rent_message():
    """
    ************************************************************************************************************
    *                                  THANK YOU. RETURNED TO HOME PAGE                                        *
    ************************************************************************************************************ 
    """
#  docstring which has message for exiting the store 
def exit_message():
    """
    ************************************************************************************************************
    *                                     THANK YOU. Please Visit Again                                        *
    ************************************************************************************************************ 
    """
# docstring which has message which reads RENT EQUIPMENT
def rent_message():
    '''
       -------------------------------------------------------------------------------------------
      |                                     RENT EQUIPMENTS                                       |
       -------------------------------------------------------------------------------------------
    '''
 # docstring which has message which reads RETURN EQUIPMENT
def return_message():
    '''
       -------------------------------------------------------------------------------------------
      |                                   RETURN EQUIPMENTS                                       |
       -------------------------------------------------------------------------------------------
    '''
# docstring which has message notifying invalid choice
def wrong_choice():
                '''		***************************************************************************************************
                *                Invalid choice! Please choose a valid option (1, 2, or 3).                       *
                ***************************************************************************************************
                   '''
# prints message indicating error 
def error_not_found():
    print()
    print("                   *****************************************************************************")
    print("                                           Error: Receipt not found."                            )               
    print("                   *****************************************************************************")

# prints message indicating invalid input 
def invalid_input():
    print("--------------------------------------------------------------")
    print("        Invalid input. Please enter a valid integer.          ")
    print("--------------------------------------------------------------")
    
# prints message indicatingall items returned 
def return_no_fine():
    print("--------------------------------------------------------------")
    print("                 All Items Returned.Thank You             ")
    print("--------------------------------------------------------------")
# prints message indicating  items returned 
def returned_already():
    print()
    print("                   *****************************************************************************")
    print("                                           ITEMS ALREADY RETURNED"                            )               
    print("                   *****************************************************************************")