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
    
    return dictionary

def make_com_list_from_request_csv():
    ''''''
    new_list = []
    with open ('request.csv', "rt") as filehandle:
        reader = csv.reader(filehandle)
        next(reader)
        for line in reader:
            ''''''
            new_list.append(line)
    return new_list

def find_requested_item(product_dict, request_list):
    '''For each request find the item's information, and print it all'''
    L_NAME_INDEX = 0
    L_PRICE_INDEX = 1
    print("Requested Items")
    for item in request_list:
        code = item[PRODUCT_NUMBER_INDEX]
        quantity = item[QUANTITY_INDEX]
        item_name = product_dict[code][L_NAME_INDEX]
        item_price = product_dict[code][L_PRICE_INDEX]
        print(f'{item_name}: {quantity} @ {item_price}')

def main():
    ''''''
    product_dict = make_dictionary_from_products_csv()
    request_list = make_com_list_from_request_csv()
    find_requested_item(product_dict, request_list)


if __name__ == '__main__':
    main()
