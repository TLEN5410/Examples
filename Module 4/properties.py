class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height= height

    def get_area(self):
        return self.width * self.height

    area = property(get_area)

def main():
    r1 = Rectangle(4, 4)
    print "The area is", r1.area

if __name__ == '__main__':
    main()
