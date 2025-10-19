

import csv
from datetime import datetime
import random


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

def process_requested_items(product_dict, request_list):
    '''For each request find the item's information, and print it all'''
    L_NAME_INDEX = 0
    L_PRICE_INDEX = 1
    print("Requested Items")
    total_quantity = 0
    subtotal = 0
    for item in request_list:
        code = item[PRODUCT_NUMBER_INDEX]
        quantity = int(item[QUANTITY_INDEX])
        item_name = product_dict[code][L_NAME_INDEX]
        item_price = float(product_dict[code][L_PRICE_INDEX])
        total_quantity += quantity
        subtotal += item_price * quantity
        print(f'{item_name}: {quantity} @ {item_price}')
    subtotal = round(subtotal, 2)
    return total_quantity, subtotal

def main():
    ''''''
    try:
        product_dict = make_dictionary_from_products_csv()
        request_list = make_com_list_from_request_csv()
        print("Inkom Emporium")
        print()
        total_quantity, subtotal = process_requested_items(product_dict, request_list)
        sales_tax = round(subtotal * 0.06, 2)
        print()
        print(f'Number of items: {total_quantity}')
        print(f'Subtotal: {subtotal}')
        print(f'Sales Tax: {sales_tax}')
        print(f'Total: {subtotal + sales_tax}')
        print()
        print("Thank you for shopping at the Inkom Emporium.")
        print()
        print("Go to in.kom to fill out a survey!")
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b  %d %I:%M:%S %Y}")
        
    except FileNotFoundError as error:
        print(f'Error: missing file {error}')
    except KeyError as error:
        print(f'Error: unknown product ID in the request.csv file {error}')


if __name__ == '__main__':
    main()
