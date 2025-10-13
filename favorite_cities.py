
import csv

CITY_NAME_INDEX = 0
COUNTRY_INDEX = 1
POPULATION_INDEX = 2

def read_data_from_file_into_list(filename):
    '''Read date from the file poited to by filename and 
    place that data in a list and return it.'''
    with open (filename, 'rt') as filehandle:
        header_line = next(filehandle)
        for line in filehandle:
            print(line.strip().split(','))

def read_data_from_file_into_list_using_csv(filename):
    '''Read date from the file poited to by filename and 
    place that data in a list and return it.'''
    city_data = []
    with open (filename, 'rt') as filehandle:
        reader = csv.reader(filehandle)
        next(reader)
        for line in reader:
            city_data.append(line)
    return city_data  

def read_data_from_file_into_dictionary_using_csv(filename):
    '''Read date from the file poited to by filename and 
    place that data in a dictionary and return it.'''
    city_data = {}
    with open (filename, 'rt') as filehandle:
        reader = csv.reader(filehandle)
        next(reader)
        for line in reader:
            city_data[line[CITY_NAME_INDEX]] = [line[COUNTRY_INDEX], line[POPULATION_INDEX]]
    return city_data   

def main():
    print("Hi")
    filename = 'favorite_cities.csv'
    city_data = read_data_from_file_into_dictionary_using_csv(filename)
    
    # for city in city_data.items():
    #     print(city)
    print(city_data)
if __name__ == '__main__':
    main()

