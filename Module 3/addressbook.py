class Person(object):
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.address = ""
        self.phone = ""

    def print_information(self):
        print "First Name:", self.first_name
        print "Last Name:", self.last_name
        print "Address:", self.address
        print "Phone:", self.phone

    def get_information(self):
        self.first_name = raw_input("Please enter the fist name: ")
        self.last_name = raw_input("Please enter the last name: ")
        self.address = raw_input("Please enter the address: ")
        self.phone = raw_input("Please enter the phone number: ")
        self.email = raw_input("Please enter the email address: ")


class AddressBook(object):
    def __init__(self):
        self.addresses = list()

    def add_person(self):
        print "\nAdding a new person to the address book"
        new_person = Person()
        new_person.get_information()
        self.addresses.append(new_person)
        
    def find_person(self):
        print "\nSearching for a person"
        needle = raw_input("Please enter the last name: ")

        for person in self.addresses:
            if person.last_name.startswith(needle):
                person.print_information()
                return

        print "\nNo results!"


def main():
    ab = AddressBook()
    print "Welcome to my address book"

    while True:
        print "\nMain Menu:"
        print "\t1 to find a person"
        print "\t2 to add a Person"
        print "\t3 to exit"

        selection = int(raw_input("Enter Selection: "))

        if selection == 1:
            ab.find_person()
        elif selection == 2:
            ab.add_person()
        elif selection == 3:
            break

    print "Cya!"

if __name__ == '__main__':
    main()
