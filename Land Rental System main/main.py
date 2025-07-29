import read
import operation

running = True

#This is the main loop that keeps the program running until
#it is told to do so.
while running == True:
    try:
        #Opening the property file
        property_file = open("properties.txt", "r")
        land_details = read.read_land(property_file)
        #Printing the welcome message
        operation.welcome_message()
        #Printing all the lands
        read.show_land(land_details)
        #Printing the input message
        operation.input_message()
        option = int(input("Enter your value: "))
        if option == 1:
            #Call the renting proccess
            operation.rent(land_details)
            print("\n")
            #Asking the user if they want to exit the program
            home = input("Type exit or ex to exit the program. \nPress ENTER to go to home screen \n >> ").lower()
            if home == "exit" or home == "ex":
                operation.exit_message()
                running = False
            else:
                property_file.close()
        elif option == 2:
            #Call the returning process
            operation.return_land(land_details)
            #Asking the user if they want to exit the program
            home_return = input("Type exit or ex to exit the program. \nPress ENTER to go to home screen \n >> ").lower()
            if home_return == "exit" or home_return == "ex":
                #Printing the exit message
                operation.exit_message()
                running = False
            else:
                property_file.close()
        elif option == 3:
            #Printing the exit message
            operation.exit_message()
            running = False
        elif option <= 0 or option > 3:
            print("Enter a valid number, 1, 2 or 3 ")
    except(ValueError):
        print("Enter a Number!!")
        #Asking the user if they want to exit the program
        home_return = input("Type exit or ex to exit the program. \nPress ENTER to go to home screen \n >> ").lower()
        if home_return == "exit" or home_return == "ex":
            #Printing the exit message
            operation.exit_message()
            running = False

property_file.close()
