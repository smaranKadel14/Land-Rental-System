import datetime

time = datetime.datetime.now()

def print_write_bill(name, customer_number, address, kitta_numlist, months_renting, total_price, land_dets):
    """Function to print the bill in the shell and write it in the file of renting"""
    print("\n")
    print("-" * 87)
    print(" " * 39 + "Invoice")
    print(time)
    print("-" * 87)
    print("Your Name: " + name)
    print("Your Number: " + str(customer_number))
    print("Your Address: " + address)
    print("-" * 87)
    print("Kitta Number" + " " * (15 - 12) + "Location" + " " * (15 - 8) + "Direction" + " " * (15 - 9) + "Anna" + " " * (15 - 4) + "Price" + " " * (15 - 5) + "Months Rented")
    print("-" * 87)
    x = 0
    for kitta in kitta_numlist:
        for i in range(len(land_dets)):
            if str(kitta) == land_dets[i][0]:
                for j in range(len(land_dets[i])):
                    print(land_dets[i][j].replace("Available", ""), end = " " * (15 - len(land_dets[i][j])))
                print(str(months_renting[x]))
                x += 1
    print("-" * 87)
    print("Total Price:", end = " ")
    final_price = 0
    for price in total_price:
        final_price += price
    print("Rs." + str(final_price))
    print("-" * 87)
    print("\n")
    print("Your Bill has been generated!")

    for i in range(len(kitta_numlist)):
        bill_name = "Rent_" + str(kitta_numlist[i]) + "_" + name + "_" + str(time.date()) + "_" + str(time.hour) + ".txt"
    bill = open(str(bill_name), "w")
    bill.write("-" * 87)
    bill.write("\n")
    bill.write(" " * 39 + "Invoice")
    bill.write("\n")
    bill.write("-" * 87)
    bill.write("\n")
    bill.write(str(time))
    bill.write("\n")
    bill.write("-" * 87)
    bill.write("\n")
    bill.write("Name: " + name)
    bill.write("\n")
    bill.write("Number: " + str(customer_number))
    bill.write("\n")
    bill.write("Address: " + address)
    bill.write("\n")
    bill.write("-" * 87)
    bill.write("\n")
    bill.write("Kitta Number" + " " * (15 - 12) + "Location" + " " * (15 - 8) + "Direction" + " " * (15 - 9) + "Anna" + " " * (15 - 4) + "Price" + " " * (15 - 5) + "Months Rented")
    bill.write("\n")
    a = 0
    for kitta in kitta_numlist:
        for i in range(len(land_dets)):
            if str(kitta) == land_dets[i][0]:
                for j in range(len(land_dets[i])):
                    bill.write(land_dets[i][j].replace("Available", ""))
                    bill.write(" " * (15 - len(land_dets[i][j])))
                bill.write(str(months_renting[a]))
                a += 1
                bill.write("\n")
    bill.write("-" * 87)
    bill.write("\n")
    bill.write("Total Price: " + str(final_price))
    bill.write("\n")
    bill.write("-" * 87)
    bill.write("\n")

def write_availability(kitta):
    """Function to write availability status from available to not available"""
    file_read = open("properties.txt", "r")
    lines = file_read.readlines()
    file_write = open("properties.txt", "w")
    for line in lines:
        single_element = line.strip().split(", ")
        if int(single_element[0]) == kitta:
            file_write.write(single_element[0] + ", " + single_element[1] + ", " + single_element[2] + ", " + single_element[3] + ", " + single_element[4] + ", " + "Not Available" + "\n")
        else:
            file_write.write(line)
    file_read.close()
    file_write.close()

def write_return_availability(kitta):
    """Function to write availability status from not available to available"""
    file_read = open("properties.txt", "r")
    lines = file_read.readlines()
    file_write = open("properties.txt", "w")
    for line in lines:
        single_element = line.strip().split(", ")
        if int(single_element[0]) == kitta:
            file_write.write(single_element[0] + ", " + single_element[1] + ", " + single_element[2] + ", " + single_element[3] + ", " + single_element[4] + ", " + "Available" + "\n")
        else:
            file_write.write(line)
    file_read.close()
    file_write.close()


def return_bill(name, kitta_numlist, months_renting, months_rented, total_price, land_dets):
    """Function to print the bill in the shell and write it in the file of returning"""
    print("\n")
    print("-" * 104)
    print(" " * 32 + "Return Invoice")
    print(time)
    print("-" * 104)
    print("Your Name: " + name)
    print("-" * 104)
    print("Kitta Number" + " " * (15 - 12) + "Location" + " " * (15 - 8) + "Direction" + " " * (15 - 9) + "Anna" + " " * (15 - 4) + "Price" + " " * (15 - 5) + "Months" + " " * (15 - 6) + "Months Rented")
    print("-" * 104)
    x = 0
    for kitta in kitta_numlist:
        for i in range(len(land_dets)):
            if str(kitta) == land_dets[i][0]:
                for j in range(len(land_dets[i])):
                    print(land_dets[i][j].replace("Not Available", ""), end = " " * (15 - len(land_dets[i][j])))
                print(str(months_renting[x]), end = " " * 18)
                print(str(months_rented[x]))
                x += 1
    print("-" * 104)
    print("Total Price:", end = " ")
    final_price = 0
    for price in total_price:
        final_price += price
    print("Rs." + str(final_price))
    print("-" * 104)
    print("\n")
    print("Your Bill has been generated!")

    for i in range(len(kitta_numlist)):
        bill_name = "Return_" + str(kitta_numlist[i]) + "_" + name + "_" + str(time.date()) + ".txt"
    bill = open(bill_name, "w")
    bill.write("-" * 104)
    bill.write("\n")
    bill.write(" " * 49 + "Return Invoice")
    bill.write("\n")
    bill.write("-" * 104)
    bill.write("\n")
    bill.write(str(time))
    bill.write("\n")
    bill.write("-" * 104)
    bill.write("\n")
    bill.write("Name: " + name)
    bill.write("\n")
    bill.write("-" * 104)
    bill.write("\n")
    bill.write("Kitta Number" + " " * (15 - 12) + "Location" + " " * (15 - 8) + "Direction" + " " * (15 - 9) + "Anna" + " " * (15 - 4) + "Price" + " " * (15 - 5) + "Months" + " " * (15 - 6) + "Months Rented")
    bill.write("\n")
    a = 0
    for kitta in kitta_numlist:
        for i in range(len(land_dets)):
            if str(kitta) == land_dets[i][0]:
                for j in range(len(land_dets[i])):
                    bill.write(land_dets[i][j].replace("Not Available", ""))
                    bill.write(" " * (15 - len(land_dets[i][j])))
                bill.write(str(months_renting[a]))
                bill.write(" " * 18)
                bill.write(str(months_rented[a]))
                a += 1
                bill.write("\n")
    bill.write("-" * 104)
    bill.write("\n")
    final_price = 0
    for price in total_price:
        final_price += price    
    bill.write("Total Price: " + str(final_price))
    bill.write("\n")
    bill.write("-" * 104)
    bill.write("\n")    
