def read_land(land_file):
    """Function to read lands from txt file and store it in a 2d list and return the list"""
    land_details = []
    for row in land_file.readlines():
        row = row.replace("\n", " ").rstrip().split(", ")
        land_details.append(row)
    return land_details

def show_land(land_details):
    """Function to display the lands"""
    print("Kitta Number" + " " * (15 - 12) + "Location" + " " * (15 - 8) + "Direction" + " " * (15 - 9) + "Anna" + " " * (15 - 4) + "Price" + " " * (15 - 5) + "Availability")
    print("-" * 88)
    for i in range(len(land_details)):
        for j in range(len(land_details[i])):
            print(land_details[i][j], end = " " * (15 - len(land_details[i][j])))
        print("\n")
    
def show_available_land(land_details):
    """Function to display all available lands"""
    available_land = []
    print("-" * 88)
    print(" " * 33 + "All Available Lands")
    print("-" * 88)
    print("Kitta Number" + " " * (15 - 12) + "Location" + " " * (15 - 8) + "Direction" + " " * (15 - 9) + "Anna" + " " * (15 - 4) + "Price" + " " * (15 - 5) + "Availability")
    print("-" * 88)
    for line in land_details:
        if "Available" in line:
            available_land.append(line)
                
    for i in range(len(available_land)):
        for j in range(len(available_land[i])):
            print(available_land[i][j], end = " " * (15 - len(available_land[i][j])))
        print("\n")
        