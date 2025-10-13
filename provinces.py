# import provinces.txt


def txt_into_list(file_name):
    province_list = []
    with open (file_name, 'rt') as filehandle:
        first_line = next(filehandle)
        for line in filehandle:
            if line.strip() == "AB":
                line = "Alberta"
            province_list.append(line.strip())
        province_list.pop()
    return province_list   

def count_occurances(list, item):
    counter = 0
    for i in list:
        if i == item:
            counter += 1
    return counter

def main():
    file_name = "provinces.txt"
    province_list = txt_into_list(file_name)
    alberta_count = count_occurances(province_list, "Alberta")
    print(alberta_count)

if __name__ == '__main__':
    main()
