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
            dictionary[int(line[CHANCE_INDEX])] = line[RESULT_INDEX]
    return dictionary

def gen_starting_area():
    '''Chooses a starting area.'''
    starting_area_dict = read_data_from_csv_into_dictionary('dnd_starting_area.csv')
    num = random.choice(range(1, 10))
    starting_area = starting_area_dict[num]
    return starting_area

def gen_corridor():
    '''Makes a random corridor.
    Optional parameter that decides if the hallway size is predefined.'''

def gen_chamber():
    ''''''

def gen_door():
    ''''''

def gen_stairs():
    ''''''

def main():
    ''''''
    
    print("Here is a random start area!")
    starting_area = gen_starting_area()
    print(starting_area)
    # running = True
    # while running:
    #     ''''''

if __name__ == '__main__':
    main()
