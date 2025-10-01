

def water_column_height(tower_height, tank_height):
    height = tower_height + 3 * tank_height / 4
    return height

def main():
    print(water_column_height(10,20))

if __name__ == "__main__":
    main()