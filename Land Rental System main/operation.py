import read
import write
import operation



def welcome_message():
    """Welcome Message"""
    print(
"""
                                  ------------------------------------------------------------------
                                                  Welcome to Techno Property Nepal!
                                  ------------------------------------------------------------------
""")
    
def input_message():
    """Input Message"""
    print(
"""Enter (1) to Rent Lands
Enter (2) to Return Lands
Enter (3) to Exit
""")
    
def exit_message():
    """Welcome Message"""
    print(
"""
                               ------------------------------------------------------------------
                                            Thank you for visiting Techno Property Nepal!
                               ------------------------------------------------------------------
""")
    
def kitta_check(kitta_inp, land_dets):
    """Function to check if kitta is in the land and it is available"""
    for i in range(len(land_dets)):
        if str(kitta_inp) == land_dets[i][0] and land_dets[i][5].strip() == "Available":
            return True


def kitta_price(kitta_inp, months, land_dets):
    """Function to Return price of the kitta"""
    for i in range(len(land_dets)):
        if str(kitta_inp) in land_dets[i][0]:
            return int(land_dets[i][4]) * int(months)
        
def charge_price(kitta, months, months_greater, land_dets):
    """Function to calculate the charge is necessary"""
    charge_percent = 0.1
    extra_months = months_greater - months
    for i in range(len(land_dets)):
        if str(kitta) in land_dets[i][0]:
            price = int(land_dets[i][4]) * int(months)
            extra_months_price = int(land_dets[i][4]) * extra_months
            charge =  extra_months_price * charge_percent
            finalprice = int(price) + int(charge)
    
    return int(finalprice)


def return_kitta_check(return_kitta, land_dets):
    """Function to check if kitta is in the system and check its availability status"""
    for i in range(len(land_dets)):
        if str(return_kitta) == land_dets[i][0] and land_dets[i][5] == "Not Available":
            return True


def rent(land_details):
    """Function to rent lands"""
    total_price = []
    months_renting = []
    kitta_numlist = []
    read.show_available_land(land_details)
    renting = True
    while renting == True:
        property_file_repeat = open("properties.txt", "r")
        land_details_repeat = read.read_land(property_file_repeat)
        try:
            #Taking kitta number as input from user
            kitta_num = int(input("Enter the kitta number of the land you want to rent: "))
            if kitta_check(kitta_num, land_details_repeat) == True :
                #Taking months as input from user
                months =int(input("How many months would you like to rent?: "))
                #Writing the availability status in the file
                write.write_availability(kitta_num)
                price = kitta_price(kitta_num, months, land_details)
                total_price.append(price)
                months_renting.append(months)
                kitta_numlist.append(kitta_num)
                continue_ = input("Do you want to rent more land (y/n): ").lower()
                if continue_ == "y" or continue_ == "yes":
                    renting = True
                elif continue_ == "n" or continue_ == "no":
                    renting = False
                else:
                    renting = False
                property_file_repeat.close()
            else:
                print("Enter a valid kitta number!")
        except:
            print("Enter a number")

    customer_details = True
    while customer_details:
        try:
            name = input("Enter your name: ")
            customer_number = int(input("Enter your number: ")) 
            address = input("Enter your address: ")
            #Printing out the invoice in the shell and in the file
            write.print_write_bill(name, customer_number, address, kitta_numlist, months_renting, total_price, land_details)
            break
        except:
            print("Enter a correct value!")
        
def return_land(land_details):
    """Function to return lands"""
    final_return_price = []
    months_rented = []
    months_ = []
    return_kitta_numlist = []
    returning = True
    while returning == True:
        property_file_repeat = open("properties.txt", "r")
        land_details_repeat = read.read_land(property_file_repeat)
        try:
            #Taking kitta number as input from user
            return_kitta = int(input("Enter the kitta number you want to return: "))
            if operation.return_kitta_check(return_kitta, land_details_repeat) == True:
                #Taking kitta number as input from user
                months_rent = int(input("Enter the months you wanted to rent this kitta: "))
                #Taking kitta number as input from user
                months_rented_inp = int(input("Enter the number of months you rented this kitta: "))
                write.write_return_availability(return_kitta)
                months_.append(months_rent)
                months_rented.append(months_rented_inp)
                return_kitta_numlist.append(return_kitta)
                #Writing the availability status in the file
                if months_rent > months_rented_inp:
                    return_price = kitta_price(return_kitta, months_rent, land_details)
                    final_return_price.append(return_price)
                else:
                    return_price = charge_price(return_kitta, months_rent, months_rented_inp, land_details)
                    final_return_price.append(return_price)
                property_file_repeat.close() 
                continue_ = input("Do you want to return more lands?(y/n): ")
                if continue_ == "y" or continue_ == "yes":
                    returning = True
                elif continue_ == "n" or continue_ == "no":
                    returning = False
                else:
                    returning = False
            else:
                print("Enter a valid kitta number!")
        except(ValueError):
            print("Enter a number!!")
    name = input("Enter your name: ")
    #Printing the bill in the shell and in the file
    write.return_bill(name, return_kitta_numlist, months_, months_rented, final_return_price, land_details)
