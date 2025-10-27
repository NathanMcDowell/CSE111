import random
import csv


'''This program will generate instructions for building a random dungeons and dragons map.
The first two functions take all the csv files containing the tables and makes the usable 
dictionaries and lists. The lists have the keys for the dictionaries. get_random_key gets 
a random key from the lists. Each gen function uses their own dictionary and list to get a 
random value through get_random_key. Some are more complicated and pass the information 
through another function to get more random values.'''

# Dictionary Indexes
CHANCE_INDEX = 0
RESULT_INDEX = 1
RESULT_TWO_INDEX = 2

# List Indexes
LOW_CHANCE_INDEX = 0
HIGH_CHANCE_INDEX = 1
KEY_INDEX = 2

def read_data_from_csv_into_dictionary(filename, value_count = 1):
    '''Read date from the file poited to by filename and 
    place that data in a dictionary and return it.'''
    dictionary = {}
    with open (filename, 'rt') as filehandle:
        reader = csv.reader(filehandle)
        next(reader)
        if value_count == 1:
            for line in reader:
                dictionary[line[CHANCE_INDEX]] = line[RESULT_INDEX]
        elif value_count == 2:
            for line in reader:
                dictionary[line[CHANCE_INDEX]] = line[RESULT_INDEX], line[RESULT_TWO_INDEX]
    return dictionary

def read_data_from_csv_into_list(filename):
    '''Read date from the file pointed to by filename and 
    place that data in a dictionary and return it.'''
    final_list = []
    with open (filename, 'rt') as filehandle:
        reader = csv.reader(filehandle)
        
        for line in reader:
            final_list.append(line)
    
    return final_list

def get_random_key(percent_lists, die_size):
    '''Intakes a list and how "rolls a die" based on how big die_size is.
    It takes that "roll" and finds which index that number is in, then
    returns it.'''
    num = random.choice(range(1, die_size + 1))
    for list in percent_lists:
        for i in range(int(list[LOW_CHANCE_INDEX]), (int(list[HIGH_CHANCE_INDEX])+1)):
            if num == i:
                chosen = list
    value = chosen[KEY_INDEX]
    return value

def gen_starting_area():
    '''Chooses a starting area. This one is simple, so it doesn't need a list for keys.'''
    starting_area_dict = read_data_from_csv_into_dictionary('dnd_map_generator/dnd_starting_area_d.csv')
    num = str(random.choice(range(1, 11)))
    starting_area = starting_area_dict[num]
    return starting_area

def gen_corridor():
    '''Makes a random corridor. Calls gen_stairs automatically if Stairs (key == 20) is rolled.'''

    corridor_dict = read_data_from_csv_into_dictionary("dnd_map_generator/dnd_corridor_d.csv")
    corridor_list = read_data_from_csv_into_list("dnd_map_generator/dnd_corridor_l.csv")
    
    key = get_random_key(corridor_list, 20)
    if key == "20":
        print(f'Stairs: {gen_stairs()}')
    elif key == "3" or key == "4" or key == "5":
        print(corridor_dict[key])
        print(gen_doors())
    else:
        print(corridor_dict[key])
    
def gen_corridor_size(size_range):
    '''Prints a random corridor size. Intakes if the corridor is a branch off or not. 
    If it is, use a smaller die.'''

    corridor_size_dict = read_data_from_csv_into_dictionary("dnd_map_generator/dnd_corridor_size_d.csv")
    corridor_size_list = read_data_from_csv_into_list("dnd_map_generator/dnd_corridor_size_l.csv")
    
    if size_range == "y":
        die_size = 12
    else:
        die_size = 20
    size_key = get_random_key(corridor_size_list, die_size)
    print(f'Size: {corridor_size_dict[size_key]}')

def gen_stairs():
    '''Returns a random stairs string.'''
    stairs_dict = read_data_from_csv_into_dictionary("dnd_map_generator/dnd_stairs_d.csv")
    stairs_list = read_data_from_csv_into_list("dnd_map_generator/dnd_stairs_l.csv")
    key = get_random_key(stairs_list, 20)
    
    return stairs_dict[key]

def gen_chamber():
    CHAMBER_TYPE_INDEX = 0
    CHAMBER_SIZE_INDEX = 1
    '''Randomly gets a size and shape for the chamber, then gets the number of exits.'''
    
    chamber_dict = read_data_from_csv_into_dictionary("dnd_map_generator/dnd_chamber_d.csv", 2)
    chamber_list = read_data_from_csv_into_list("dnd_map_generator/dnd_chamber_l.csv")

    key = get_random_key(chamber_list, 20)
    
    print(chamber_dict[key][CHAMBER_TYPE_INDEX])
    
    exit_count = int(gen_chamber_exits(int(chamber_dict[key][CHAMBER_SIZE_INDEX])))
    door_count, corridor_count = gen_exit_types(exit_count)
    
    # Makes the plurality correct in the print.
    door_plural, corridor_plural = "s", "s"
    if door_count == 1:
        door_plural = ""
    if corridor_count == 1:
        corridor_plural = ""
    
    if door_count == 0 and corridor_count == 0:
        print("No exits.")
    else:
        print(f'Exits: {door_count} door{door_plural} and {corridor_count} 10ft long corridor{corridor_plural}')

    door_type_list = []
    for door in range(0, door_count):
        door_type_list.append(gen_doors())
    print(", ".join(door_type_list))

def gen_chamber_exits(chamber_size):
    '''Intakes the size of the chamber it is making exits for and uses that information
    to know which size index to use. Bigger chambers have more exits.'''
    
    chamber_exits_dict = read_data_from_csv_into_dictionary("dnd_map_generator/dnd_chamber_exits_d.csv", 2)
    chamber_exits_list = read_data_from_csv_into_list("dnd_map_generator/dnd_chamber_exits_l.csv")
    key = get_random_key(chamber_exits_list, 20)
    if chamber_size == 1:
        return chamber_exits_dict[key][0]
    if chamber_size == 2:
        return chamber_exits_dict[key][1]
    
def gen_exit_types(exit_count):
    '''Intakes the number of exits (from gen_chamber_exits) and determines how many are doors vs. corridors.'''
    door_count = 0
    corridor_count = 0
    for exit in range(0, exit_count):
        one_or_two = random.choice(range(1, 3))
        if one_or_two == 1:
            door_count += 1
        elif one_or_two == 2:
            corridor_count += 1
    return door_count, corridor_count

def gen_doors():
    '''Gets a random door type.'''
    door_type_dict = read_data_from_csv_into_dictionary("dnd_map_generator/dnd_door_type_d.csv")
    door_type_list = read_data_from_csv_into_list("dnd_map_generator/dnd_door_type_l.csv")
    
    key = get_random_key(door_type_list, 20)
    return door_type_dict[key]

def gen_beyond_door():
    '''Returns a beyond the door. Calls stairs if that key (19) is rolled.'''
    beyond_door_dict = read_data_from_csv_into_dictionary("dnd_map_generator/dnd_beyond_door_d.csv")
    beyond_door_list = read_data_from_csv_into_list("dnd_map_generator/dnd_beyond_door_l.csv")
    
    key = get_random_key(beyond_door_list, 20)
    if key == "19":
        return f'Stairs: {gen_stairs()}'
    else:
        return beyond_door_dict[key]


def main():
    ''''''
    running = True
    while running:
        ''''''
        print()
        print("#0 Quit")
        print("#1 Starting area")
        print("#2 Corridor")
        print("#3 Corridor size")
        print("#4 Chamber")
        print("#5 Beyond a door")
        print("#6 Other")
        print("What would you like to generate?")
        called_gen = input("#")
        print()
        if called_gen == "0":
            running = False
            print("You have quit.")
        elif called_gen == "1":
            
            print(gen_starting_area())
        elif called_gen == "2":
            gen_corridor()

        elif called_gen == "3":
            size_range = input("Branch off corridor? (y/n) ")
            gen_corridor_size(size_range)

        elif called_gen == "4":
            gen_chamber()
        
        elif called_gen == "5":
            ''''''
            print(gen_beyond_door())

        elif called_gen == "6":
            print("#0 Back")
            print("#1 Doors")
            print("#2 Stairs")
            print("What would you like to generate?")
            called_gen = input("#")
            if called_gen == "1":
                print(gen_doors())
            elif called_gen == "2":
                print(gen_stairs())
        
        else:
            print("Enter a valid number")


if __name__ == '__main__':
    main()