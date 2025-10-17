import random
import csv


'''This program will generate instructions for building a random dungeons and dragons map.'''
CHANCE_INDEX = 0
RESULT_INDEX = 1
RESULT_TWO_INDEX = 2

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
            print(line)
    # with open (filename, 'rt') as filehandle:
    #     # header_line = next(filehandle)
    #     for line in filehandle:
    #         list.append(line)
    return final_list

def gen_starting_area():
    '''Chooses a starting area.'''
    starting_area_dict = read_data_from_csv_into_dictionary('dnd_starting_area_d.csv')
    num = str(random.choice(range(1, 10)))
    starting_area = starting_area_dict[num]
    return starting_area

def gen_corridor():
    '''Makes a random corridor.
    Optional parameter that decides if the hallway size is predefined.'''
    corridor_dict = read_data_from_csv_into_dictionary("dnd_corridor_d.csv")
    corridor_list = read_data_from_csv_into_list("dnd_corridor_l.csv")
    print(f"Corridor dictionary: {corridor_dict}")
    print(f"Corridor list: {corridor_list}")
    num = random.choice(range(1, 20))
    print(f"Random number : {num}")
    for list in corridor_list:
        for i in range(int(list[0]), (int(list[1])+1)):
            if num == i:
                chosen = list
    print(chosen)
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





