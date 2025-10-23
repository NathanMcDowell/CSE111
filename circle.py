

class circle:
    radius = 0.0

    def __init__(self, r):
        self.radius = r

    def get_radius(self):
        return self.radius

def main():
    # x = 65535
    
    # bytes = x.to_bytes(2, 'big')
    # print(bytes)

    # name = 'bob'
    # name = name.capitalize()
    # print(name)

    my_circle = circle(10)
    
    print(my_circle.get_radius())



main()