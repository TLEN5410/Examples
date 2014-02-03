def add_person(address_book):
    p = dict()
    p['first_name'] = raw_input("Please enter the fist name: ")
    p['last_name'] = raw_input("Please enter the last name: ")
    p['address'] = raw_input("Please enter the address: ")
    p['phone'] = raw_input("Please enter the phone number: ")
    p['email'] = raw_input("Please enter the email address: ")
    address_book.append(p)


def find_person(address_book):
    first_name = raw_input("Please enter the first name: ")
    last_name = raw_input("Please enter the last name: ")

    for person in address_book:
        if (first_name == person['first_name'] and
                last_name == person['last_name']):
            return person


def erase_person(address_book):
    person_to_remove = find_person(address_book)
    address_book.remove(person_to_remove)


def print_addressbook(address_book):
    for person in address_book:
        print "-"*20
        print "First Name: {0}".format(person['first_name'])
        print "Last Name: {0}".format(person['last_name'])
        print "Address: {0}".format(person['address'])
        print "Phone: {0}".format(person['phone'])
        print "Email: {0}".format(person['email'])


def main():
    address_book = list()
    print "Welcome to my address book"

    while True:
        print "\nMain Menu:"
        print "\t1 to print address book"
        print "\t2 to add a person"
        print "\t3 to erase a person"
        print "\t4 to exit"

        selection = int(raw_input("Enter Selection: "))

        if selection == 1:
            print_addressbook(address_book)
        elif selection == 2:
            add_person(address_book)
        elif selection == 3:
            erase_person(address_book)
        elif selection == 4:
            break

    print "Cya!"

if __name__ == '__main__':
    main()
