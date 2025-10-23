import random
import csv


'''This program will generate instructions for building a random dungeons and dragons map.'''
# Dictionary Indexes
CHANCE_INDEX = 0
RESULT_INDEX = 1
RESULT_TWO_INDEX = 2

# List Indexes
LOW_CHANCE_INDEX = 0
HIGH_CHANCE_INDEX = 1
KEY_INDEX = 2

#

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
    '''Read date from the file poited to by filename and 
    place that data in a dictionary and return it.'''
    final_list = []
    with open (filename, 'rt') as filehandle:
        reader = csv.reader(filehandle)
        
        for line in reader:
            final_list.append(line)
    
    return final_list

def get_random_key(percent_lists, die_size):
    num = random.choice(range(1, die_size + 1))
    for list in percent_lists:
        for i in range(int(list[LOW_CHANCE_INDEX]), (int(list[HIGH_CHANCE_INDEX])+1)):
            if num == i:
                chosen = list
    value = chosen[KEY_INDEX]
    return value

def gen_starting_area():
    '''Chooses a starting area.'''
    starting_area_dict = read_data_from_csv_into_dictionary('dnd_map_generator/dnd_starting_area_d.csv')
    num = str(random.choice(range(1, 11)))
    starting_area = starting_area_dict[num]
    return starting_area

def gen_corridor():
    '''Makes a random corridor.
    Optional parameter that decides if the hallway size is predefined.'''
    corridor_dict = read_data_from_csv_into_dictionary("dnd_map_generator/dnd_corridor_d.csv")
    corridor_list = read_data_from_csv_into_list("dnd_map_generator/dnd_corridor_l.csv")
    
    key = get_random_key(corridor_list, 20)
    print(corridor_dict[key])
    
def gen_corridor_size(size_range):
    corridor_size_dict = read_data_from_csv_into_dictionary("dnd_map_generator/dnd_corridor_size_d.csv")
    corridor_size_list = read_data_from_csv_into_list("dnd_map_generator/dnd_corridor_size_l.csv")
    
    if size_range == "y":
        die_size = 12
    else:
        die_size = 20
    size_key = get_random_key(corridor_size_list, die_size)
    print(f'Size: {corridor_size_dict[size_key]}')

def gen_chamber():
    CHAMBER_TYPE_INDEX = 0
    CHAMBER_SIZE_INDEX = 1
    '''Randomly gets a size and shape for the chamber, then gets the number of exits.'''
    chamber_dict = read_data_from_csv_into_dictionary("dnd_map_generator/dnd_chamber_d.csv", 2)
    chamber_list = read_data_from_csv_into_list("dnd_map_generator/dnd_chamber_l.csv")
    # Currently returning None
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

def gen_chamber_exits(chamber_size):
    '''Intakes the size of the chamber it is making exits for.'''
    
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
    ''''''
    door_type_dict = read_data_from_csv_into_dictionary("dnd_map_generator/dnd_door_type_d.csv")
    door_type_list = read_data_from_csv_into_list("dnd_map_generator/dnd_door_type_l.csv")
    
    key = get_random_key(door_type_list, 20)
    print(door_type_dict[key])

def gen_stairs():
    ''''''

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
        print("#5 Doors- Just for testing")
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
            gen_doors()
        
        elif called_gen == "6":
            ''''''
            gen_exit_types(range(1, 10))

if __name__ == '__main__':
    main()
'''
user gives an input
function is called
random number is made
'1, 5, 1-5'
if number in range(list[START_INDEX], list[END_INDEX])
    print(dictionary[list[RANGE]])
'''





