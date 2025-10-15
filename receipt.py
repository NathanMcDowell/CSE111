import csv
PRODUCT_NUMBER_INDEX = 0

def make_dictionary_from_csv(filename):
    ''''''
    dictionary = {}
    with open (filename, "rt") as filehandle:
        reader = csv.reader(filehandle)
        next(reader)
        for line in reader:
            ''''''
            print(line[PRODUCT_NUMBER_INDEX])

def main():
    ''''''
    make_dictionary_from_csv('request.csv')

if __name__ == '__main__':
    main()
