'''

This is a parking lot creator
if launched standalone, you can create a new parking lot
if this file is launched from parking lot manager, then you can manage created parking lots

'''

# importing os module, for working with directories
import os

# if this file is launched directly
if __name__ == "__main__":

    print("-----------------------------------")
    print("This is a parking lot creator v1.0")
    print("-----------------------------------")

    create_parking_lot = input("Do you want to create a new parking lot? Type 'Yes' or 'No'  ")
    if create_parking_lot == "Yes":
        parking_lot_name = input("What is the name of parking lot?  ")
        number_of_spots = input("How many places should be in this parking lot?  ")
# creating a new directory with your parking lot name
        os.mkdir(parking_lot_name)
# in new directory creating a data file
        url = parking_lot_name + '/' + 'data.txt'
        file = open(url, "w+")
        file.write(str(number_of_spots) + "\n")
# in that file writing a number of parking spots and some info about all the spots
        for spot_index in range(int(number_of_spots)):
            file.write(str(spot_index) + " " + "0" + "\n")
        file.close()

# if this file is launched from another file
else:
# importing time module
    from time import strftime

# creating a parking spot class with index, bool is_used, date and car number
# by default car number and date = 0
    class Parking_spot:
        def __init__(self, index, is_used):
            self.index = index
            self.is_used = is_used
            self.date = 0
            self.number = 0

# parking spot function, that change bool is_used to true and gives parking spot date and car number from input
        def used(self, number, date):
            self.is_used = 1
            self.date = date
            self.number = number

# parking spot function, that clear one parking spot
        def clear(self):
            self.is_used = 0
            self.date = 0
            self.number = 0

# function that shows all directories == all parking lots
    def show_directories():
        dirs = os.listdir()
        print("-------------------------")
        for file in dirs:
            if '.' not in file and '__pycache__' not in file:
                print(file)
        print("-------------------------")

# read data from parking lot data file
    def read_info(name):
        # global variables, they will change not only in function
        global number_of_spots
        global parking_spots
        url = name + "/data.txt"
        data_file = open(url)
        # open data file and read first line with number of spots
        number_of_spots = int(data_file.readline())
        # read other lines and use that data in an object array
        for index in range(number_of_spots):
            line = data_file.readline()
            if line == '\n':
                line = data_file.readline()
            line = line.split(' ')
            number_of_arguments = len(line)
            if number_of_arguments == 2:
                parking_spots.append(Parking_spot(line[0], line[1]))
            if number_of_arguments == 4:
                parking_spots.append(Parking_spot(line[0], line[1]))
                parking_spots[index].used(line[2], line[3])
        # close the data file
        data_file.close()

# save changed information about parking lot
    def write_info(name):
        url = name + '/data.txt'
        data_file = open(url, "w+")
        data_file.write(str(number_of_spots) + "\n")
        for index in range(number_of_spots):
            if int(parking_spots[index].is_used) == 0:
                data_file.write(str(index) + " " + "0" + "\n")
            else:
                data_file.write(str(index) + " " + "1" + " " + str(parking_spots[index].number) + " " + str(parking_spots[index].date) + "\n")
        data_file.close()

# function that calls parking lot class funtion if needed
    def use_spot():
        index = int(input("Which spot do you want to use?  "))
        if int(parking_spots[index].is_used) == 1:
            print("This spot is already used")
        else:
            date = strftime("%H:%M:%S")
            number = input("What is the car number?  ")
            parking_spots[index].used(number, date)

# function that calls parking lot class funtion if needed
    def clear_spot():
        index = int(input("Which spot do you want to clear?  "))
        if int(parking_spots[index].is_used) == 0:
            print("This spot is free")
        else:
            parking_spots[index].clear()

# function that shows used parking lot places
    def show_used():
        for index in range(int(number_of_spots)):
            if int(parking_spots[index].is_used) == 1:
                print(index, " ")

# function that shows free parking lot places
    def show_free():
        for index in range(int(number_of_spots)):
            if int(parking_spots[index].is_used) == 0:
                print(index, " ")


    show_directories()
    parking_lot_name = input("What parking lot you want to manage?  ")
    number_of_spots = 0
    parking_spots = []
    read_info(parking_lot_name)
    task = " "
# ask for task you want to do, if you chose save, after saving program will exit
    while task != "save":
        print("\n")
        task = input("What do you want to do with parking lot? 'use_spot' 'clear_spot' 'save' 'show_used_spots' 'show_free_spots'  ")
        if task == "use_spot":
            use_spot()
        elif task == "show_used_spots":
            show_used()
        elif task == "show_free_spots":
            show_free()
        elif task == "clear_spot":
            clear_spot()
        elif task == "save":
            write_info(parking_lot_name)
        else:
            print("Wrong task")
