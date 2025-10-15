import csv

PRODUCT_NUMBER_INDEX = 0

QUANTITY_INDEX = 1

NAME_INDEX = 1
PRICE_INDEX = 2


def make_dictionary_from_products_csv():
    ''''''
    dictionary = {}
    with open ('products.csv', "rt") as filehandle:
        reader = csv.reader(filehandle)
        next(reader)
        for line in reader:
            ''''''
            dictionary[line[PRODUCT_NUMBER_INDEX]] = line[NAME_INDEX], line[PRICE_INDEX]
            print(dictionary[line[PRODUCT_NUMBER_INDEX]])

def make_dictionary_from_request_csv():
    ''''''
    dictionary = {}
    with open ('request.csv', "rt") as filehandle:
        reader = csv.reader(filehandle)
        next(reader)
        for line in reader:
            ''''''
            dictionary[line[PRODUCT_NUMBER_INDEX]] = line[QUANTITY_INDEX]
            print(dictionary[line[PRODUCT_NUMBER_INDEX]])

def main():
    ''''''
    make_dictionary_from_products_csv()
    make_dictionary_from_request_csv()


if __name__ == '__main__':
    main()
