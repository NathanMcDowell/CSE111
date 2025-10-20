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

def read_data_from_csv_into_dictionary(filename):
    '''Read date from the file poited to by filename and 
    place that data in a dictionary and return it.'''
    dictionary = {}
    with open (filename, 'rt') as filehandle:
        reader = csv.reader(filehandle)
        next(reader)
        for line in reader:
            dictionary[line[CHANCE_INDEX]] = line[RESULT_INDEX]
    return dictionary

def read_data_from_csv_into_list(filename):
    '''Read date from the file poited to by filename and 
    place that data in a dictionary and return it.'''
    final_list = []
    with open (filename, 'rt') as filehandle:
        reader = csv.reader(filehandle)
        
        for line in reader:
            final_list.append(line)
    # with open (filename, 'rt') as filehandle:
    #     # header_line = next(filehandle)
    #     for line in filehandle:
    #         list.append(line)
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
    starting_area_dict = read_data_from_csv_into_dictionary('dnd_map_generator\dnd_starting_area_d.csv')
    num = str(random.choice(range(1, 11)))
    starting_area = starting_area_dict[num]
    return starting_area

def gen_corridor():
    '''Makes a random corridor.
    Optional parameter that decides if the hallway size is predefined.'''
    corridor_dict = read_data_from_csv_into_dictionary("dnd_map_generator\dnd_corridor_d.csv")
    corridor_list = read_data_from_csv_into_list("dnd_map_generator\dnd_corridor_l.csv")
    # corridor_width_dict = read_data_from_csv_into_dictionary("dnd_map_generator\dnd_corridor_size_d.csv")
    # corridor_width_list = read_data_from_csv_into_list("dnd_map_generator\dnd_corridor_size_l.csv")
    key = get_random_key(corridor_list, 20)
    print(corridor_dict[key])
    # if key 
        # width_key = get_random_key(corridor_width_list, 20)
        # print(corridor_width_dict[width_key])

def gen_chamber():
    ''''''
    

def gen_door():
    ''''''

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
        print("What would you like to generate?")
        called_gen = input("# ")
        if called_gen == "0":
            running = False
            print("You have quit.")
        elif called_gen == "1":
            print(gen_starting_area())
        elif called_gen == "2":
            gen_corridor()


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





