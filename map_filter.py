
import math

def calculate_fahrenheit_temperature(celsius):
    '''Transform celsius into fahrenheit'''
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

def map_data(calculate_function, data):
    '''Run through the data in data and call a function and return the transformed data'''
    tranformed_data = []
    for item in data:
        tranformed_data.append(calculate_function(item))
    return tranformed_data

def is_prime(number):
    for i in range(2,int(math.sqrt(number)) + 1, 1):
        if number % i == 0:
            return False
    return True

def print_students(students):
    for student in students:
        print(student)

def main():
    '''celsius_temperatures = [0, 1, 2, 3, 4, 5, 6, 7, 25, 245, 2, 35431]
    # farhenheit_temperatures = map_data(calculate_fahrenheit_temperature, celsius_temperatures)
    # print(farhenheit_temperatures)

    # farhenheit_temperatures2 = list(map(calculate_fahrenheit_temperature, celsius_temperatures))
    # print(farhenheit_temperatures2)

    # farhenheit_temperatures3 = list(map(lambda c : c * 9 / 5 + 32, celsius_temperatures))
    # print(farhenheit_temperatures3)

    # odd_numbers = list(filter(lambda x : x % 2, celsius_temperatures))
    # print(odd_numbers)
    numbers = list(range(1,100))
    prime_numbers = list(filter(is_prime, numbers))
    print(prime_numbers)

    print(list(filter(is_prime, range(1000000, 1100000))))'''
    FIRST_NAME_INDEX = 0
    LAST_NAME_INDEX = 1
    READING_LEVEL_INDEX = 2
    students = [ 
        ["Robert", "Smith", 6.7], ["Annie", "Smith", 6.2], 
        ["Robert", "Lopez", 7.1], ["Sean", "Li", 5.6], 
        ["Sofia", "Lopez", 5.3], ["Lily", "Harris", 6.7], 
        ["Alex", "Harris", 5.8], ["Billy", "Bob", 6.3], 
        ["Jeannie", "Roberts", 5.9], ["Bubba", "Bob", 7.9], 
        ["Lilly", "Smith", 4.9]]
    sorted_students_by_level = sorted(students, key = lambda x : x[READING_LEVEL_INDEX], reverse= True)
    print_students(sorted_students_by_level)

if __name__ == '__main__':
    main()