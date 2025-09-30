

def calculate_rectangle_area(width, height):
    assert width > 0
    assert height > 0
    return width * height


def main():
    # print(calculate_rectangle_area(10, 10))
    show_floating_point_values()


def show_floating_point_values():
    for i in range(11):
        value = i / 10
        if abs(value - 0.599999999) < 0.00001 :
            print('They are equal')
        print(f"{value:.17f}")
if __name__ == '__main__':
    main()